# Copyright (c) 2023, venkatesh nayak and contributors
# For license information, please see license.txt

# import frappe
from __future__ import unicode_literals
import frappe
import json
from frappe import _, msgprint
from frappe.model.mapper import get_mapped_doc
from frappe.query_builder.functions import Sum
from frappe.utils import cint, cstr, flt, get_link_to_form, getdate, new_line_sep, nowdate
from frappe.model.document import Document
from frappe.utils import (
    add_days,
    ceil,
    cint,
    comma_and,
    flt,
    get_link_to_form,
    getdate,
    now_datetime,
    nowdate,today,formatdate, get_first_day, get_last_day 
)
from datetime import date,timedelta
from frappe.model.document import Document

class MaterialRequestForm(Document):
	pass


@frappe.whitelist()
def search_item(item):
    item_data = search_serial_or_batch_or_barcode_number(item)
    if item_data != 0:
        # stock = frappe.db.sql("""SELECT batch_no,item_code,warehouse, sum(actual_qty) as qty,stock_uom from `tabStock Ledger Entry` WHERE is_cancelled = 0 and item_code = '%(item_code)s' and warehouse = '%(warehouse)s' group by warehouse,batch_no """%{"item_code": item_data['item_code'],"warehouse": warehouse}, as_dict = 1)
        # return stock
        stock = frappe.db.sql("""SELECT item_code,item_name,stock_uom,item_group,description,brand from `tabItem` WHERE disabled = 0 and item_code = '%(item_code)s' """%{"item_code": item_data['item_code']}, as_dict = 1)
        return stock
    
    return "Item/Price not found"
def search_serial_or_batch_or_barcode_number(search_value):
    # search barcode no
    barcode_data = frappe.db.get_value('Item Barcode', {'barcode': search_value}, ['barcode', 'parent as item_code'], as_dict=True)
    if barcode_data:
        barcode_data["type"] = "item_barcode"
        return barcode_data

    #confirm item code
    item_code_data = frappe.db.get_value('Item', search_value, ['name as item_code'], as_dict=True)
    if item_code_data:
        item_code_data["type"] = "item_code"
        # item_code_data["posa_uom"] = ""
        return item_code_data
    
    # search batch no
    batch_no_data = frappe.db.get_value('Batch', search_value, ['name as batch_no', 'item as item_code'], as_dict=True)
    # batch_no_data=frappe.db.sql("""SELECT name as batch_no,item as item_code from `tabBatch` WHERE name = '%(search_value)s' """%{"search_value": search_value}, as_dict = 1)
    if batch_no_data:
        batch_no_data["type"] = "batch"
        return batch_no_data

    # search serial no
    serial_no_data = frappe.db.get_value('Serial No', search_value, ['name as serial_no', 'item_code'], as_dict=True)
    if serial_no_data:
        serial_no_data["type"] = "item_serial"
        return serial_no_data

def update_item(obj, target, source_parent):
	target.conversion_factor = obj.conversion_factor
	target.qty = flt(flt(obj.stock_qty) - flt(obj.ordered_qty)) / target.conversion_factor
	target.stock_qty = target.qty * target.conversion_factor
	if getdate(target.schedule_date) < getdate(nowdate()):
		target.schedule_date = None

@frappe.whitelist()
def make_purchase_order(source_name, target_doc=None, args=None):
	if args is None:
		args = {}
	if isinstance(args, str):
		args = json.loads(args)

	def postprocess(source, target_doc):
		if frappe.flags.args and frappe.flags.args.default_supplier:
			# items only for given default supplier
			supplier_items = []
			for d in target_doc.items:
				default_supplier = get_item_defaults(d.item_code, target_doc.company).get("default_supplier")
				# if frappe.flags.args.default_supplier == default_supplier:
				supplier_items.append(d)
			target_doc.items = supplier_items

		# set_missing_values(source, target_doc)

	def select_item(d):
		filtered_items = args.get("filtered_children", [])
		child_filter = d.name in filtered_items if filtered_items else True

		return d.ordered_qty < d.stock_qty and child_filter

	doclist = get_mapped_doc(
		"Material Request Form",
		source_name,
		{
			"Material Request Form": {
				"doctype": "Purchase Order",
				"validation": {"docstatus": ["=", 1], "material_request_type": ["=", "Purchase"]},
			},
			"Material Request Form Item": {
				"doctype": "Purchase Order Item",
				"field_map": [
					["name", "material_request__form_item"],
					["parent", "material_request_form"],
					["uom", "stock_uom"],
					["uom", "uom"],
					["sales_order", "sales_order"],
					["sales_order_item", "sales_order_item"],
				],
				"postprocess": update_item,
				"condition": select_item,
			},
		},
		target_doc,
		postprocess,
	)

	return doclist

@frappe.whitelist()
def make_stock_entry(source_name, target_doc=None):
	def update_item(obj, target, source_parent):
		qty = (
			flt(flt(obj.stock_qty) - flt(obj.ordered_qty)) / target.conversion_factor
			if flt(obj.stock_qty) > flt(obj.ordered_qty)
			else 0
		)
		target.qty = qty
		target.transfer_qty = qty * obj.conversion_factor
		target.conversion_factor = obj.conversion_factor

		if (
			source_parent.material_request_type == "Material Transfer"
			or source_parent.material_request_type == "Customer Provided"
		):
			target.t_warehouse = obj.warehouse
		else:
			target.s_warehouse = obj.warehouse

		if source_parent.material_request_type == "Customer Provided":
			target.allow_zero_valuation_rate = 1

		if source_parent.material_request_type == "Material Transfer":
			target.s_warehouse = obj.from_warehouse

	def set_missing_values(source, target):
		target.purpose = source.material_request_type
		target.from_warehouse = source.set_from_warehouse
		target.to_warehouse = source.set_warehouse

		if source.job_card:
			target.purpose = "Material Transfer for Manufacture"

		if source.material_request_type == "Customer Provided":
			target.purpose = "Material Receipt"

		target.set_transfer_qty()
		target.set_actual_qty()
		target.calculate_rate_and_amount(raise_error_if_no_rate=False)
		target.stock_entry_type = target.purpose
		target.set_job_card_data()

	doclist = get_mapped_doc(
		"Material Request",
		source_name,
		{
			"Material Request": {
				"doctype": "Stock Entry",
				"validation": {
					"docstatus": ["=", 1],
					"material_request_type": ["in", ["Material Transfer", "Material Issue", "Customer Provided"]],
				},
			},
			"Material Request Item": {
				"doctype": "Stock Entry Detail",
				"field_map": {
					"name": "material_request_item",
					"parent": "material_request",
					"uom": "stock_uom",
					"job_card_item": "job_card_item",
				},
				"postprocess": update_item,
				"condition": lambda doc: doc.ordered_qty < doc.stock_qty,
			},
		},
		target_doc,
		set_missing_values,
	)

	return doclist


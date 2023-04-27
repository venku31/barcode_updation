# Copyright (c) 2023, venkatesh nayak and contributors
# For license information, please see license.txt

# import frappe
from __future__ import unicode_literals
import frappe
import json
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
class StockCheck(Document):
	pass


@frappe.whitelist()
def search_item(item,warehouse):
    item_data = search_serial_or_batch_or_barcode_number(item)
    if item_data != 0:
        # stock = frappe.db.sql("""SELECT batch_no,item_code,warehouse, sum(actual_qty) as qty,stock_uom from `tabStock Ledger Entry` WHERE is_cancelled = 0 and item_code = '%(item_code)s' and warehouse = '%(warehouse)s' group by warehouse,batch_no """%{"item_code": item_data['item_code'],"warehouse": warehouse}, as_dict = 1)
        # return stock
        stock = frappe.db.sql("""SELECT item_code,item_name,stock_uom from `tabItem` WHERE disabled = 0 and item_code = '%(item_code)s' """%{"item_code": item_data['item_code']}, as_dict = 1)
        return stock
    
    return "Item/Price not found"
def search_serial_or_batch_or_barcode_number(search_value):
    # search barcode no
    barcode_data = frappe.db.get_value('Item Barcode', {'barcode': search_value}, ['barcode', 'parent as item_code', 'posa_uom'], as_dict=True)
    if barcode_data:
        barcode_data["type"] = "item_barcode"
        return barcode_data

    #confirm item code
    item_code_data = frappe.db.get_value('Item', search_value, ['name as item_code'], as_dict=True)
    if item_code_data:
        item_code_data["type"] = "item_code"
        item_code_data["posa_uom"] = ""
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

    return 0
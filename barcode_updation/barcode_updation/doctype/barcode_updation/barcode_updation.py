# Copyright (c) 2023, venkatesh nayak and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe
from erpnext.controllers.item_variant import enqueue_multiple_variant_creation
from erpnext.stock.utils import get_stock_balance, get_stock_value_on
import json
from six import string_types
from frappe import _
class BarcodeUpdation(Document):
    pass

@frappe.whitelist()
def add_item_barcode(item_code,barcode,posa_uom):
    item = frappe.get_doc('Item', item_code)
   
    item.append(
        "barcodes",
        {
             "barcode": barcode,
             "posa_uom": posa_uom,
        },
    )
    item.save(ignore_permissions=True)
    frappe.db.commit()
    frappe.msgprint(
        _("Barcodes successfully updated for Item: " + item.item_name), alert=True
    )
@frappe.whitelist()
def add_item_image(item_code,image):
    item = frappe.get_doc('Item', item_code)
   
    item.image = image
    item.save(ignore_permissions=True)
    frappe.db.commit()
    frappe.msgprint(
        _("Image successfully updated for Item: " + item.item_name), alert=True
    )

@frappe.whitelist()
def get_stock_item_details(warehouse, date, item=None, barcode=None):
    out = {}
    if barcode:
        out["item"] = frappe.db.get_value(
            "Item Barcode", filters={"barcode": barcode}, fieldname=["parent"]
        )
        if not out["item"]:
            frappe.throw(_("Invalid Barcode. There is no Item attached to this barcode."))
    else:
        out["item"] = item

    barcodes = frappe.db.get_values(
        "Item Barcode", filters={"parent": out["item"]}, fieldname=["barcode"]
    )

    out["barcodes"] = [x[0] for x in barcodes]
    out["qty"] = get_stock_balance(out["item"], warehouse, date)
    out["value"] = get_stock_value_on(warehouse, date, out["item"])
    out["image"] = frappe.db.get_value("Item", filters={"name": out["item"]}, fieldname=["image"])
    return out
    
@frappe.whitelist()
def get_item_price(item):
    fields = frappe.get_all('Item Price', filters={'item_code':item,"uom":"Pcs","price_list":"Premium Shop Selling"}, fields=['price_list','price_list_rate',],limit =1)
    return fields

@frappe.whitelist()
def get_price(item,price_list,uom):
    fields = frappe.get_all('Item Price', filters={'item_code':item,"uom":uom,"price_list":price_list}, fields=['price_list_rate',],limit =1)
    return fields

@frappe.whitelist()
def update_price(item,price_list,uom,price_list_rate,price):
    # item = frappe.get_doc('Item Price', {"item_code":item,"price_list":price_list,"uom":uom})
    if (int(price)>0) :
        item = frappe.get_doc('Item Price', {"item_code":item,"price_list":price_list,"uom":uom})
        item.price_list_rate = price_list_rate
        item.save(ignore_permissions=True)
        frappe.db.commit()
        frappe.msgprint(
            _("Price successfully updated for Item: " + item.item_code), alert=True
         )
    else :
        item_price = frappe.new_doc('Item Price')
        item_price.item_code = item
        item_price.price_list = price_list
        item_price.uom = uom
        item_price.price_list_rate = price_list_rate
        item_price.save(ignore_permissions=True)
        frappe.db.commit()
        frappe.msgprint(
            ("Price successfully Created for Item: " + item), alert=True
            )

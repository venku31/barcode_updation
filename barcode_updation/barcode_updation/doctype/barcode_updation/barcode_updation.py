# Copyright (c) 2023, venkatesh nayak and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe
from erpnext.controllers.item_variant import enqueue_multiple_variant_creation
import json
from six import string_types
from frappe import _
class BarcodeUpdation(Document):
    pass

@frappe.whitelist()
def add_item_barcode(item_code,barcode):
    item = frappe.get_doc('Item', item_code)
   
    item.append(
        "barcodes",
        {
             "barcode": barcode,
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

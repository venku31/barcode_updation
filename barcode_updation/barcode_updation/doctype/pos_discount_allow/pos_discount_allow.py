# Copyright (c) 2023, venkatesh nayak and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document

class POSDiscountAllow(Document):
    pass

@frappe.whitelist()
def pos_discount_allow(doc,handler=""):
    if doc.allow_discount or doc.allow_edit_rate or doc.item.posa_allow_return:
        item = frappe.get_doc('POS Profile', {"name":doc.pos_profile})
        item.posa_allow_user_to_edit_additional_discount = doc.allow_discount
        item.posa_use_percentage_discount = doc.allow_discount
        item.posa_allow_user_to_edit_item_discount = doc.allow_discount
        item.posa_apply_customer_discount = doc.allow_discount
        item.allow_discount_change = doc.allow_discount
        item.posa_allow_user_to_edit_rate = doc.allow_edit_rate
        item.allow_rate_change = doc.allow_edit_rate
        item.posa_allow_return = doc.allow_return
        item.save(ignore_permissions=True)
        frappe.db.commit()
        frappe.msgprint(
            _("Allowed for pos profile: " + item.name), alert=True
        )
@frappe.whitelist()
def pos_discount_disable(doc,handler=""):
    exists = frappe.db.get_value('POS Discount Allow', {'pos_profile':doc.pos_profile,'date':doc.posting_date}, 'name')
    if exists :
        if doc.pos_profile :
            item = frappe.get_doc('POS Profile', {"name":doc.pos_profile})
            item.posa_allow_user_to_edit_additional_discount = 0
            item.posa_use_percentage_discount = 0
            item.posa_allow_user_to_edit_item_discount = 0
            item.posa_apply_customer_discount = 0
            item.allow_discount_change = 0
            item.posa_allow_user_to_edit_rate = 0
            item.allow_rate_change = 0
            item.posa_allow_return = 0
            item.save(ignore_permissions=True)
            frappe.db.commit()
            # frappe.msgprint(
            # _("Allowed for pos profile: " + item.name), alert=True
            # )
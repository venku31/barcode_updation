# Copyright (c) 2023, venkatesh nayak and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ItemTagPrint(Document):
	pass

@frappe.whitelist()
def get_fields_details(item_group):
	fields = frappe.db.sql("""select name as website_item,item_code,web_item_name,website_image from `tabWebsite Item` where item_group = %s""",(item_group), as_dict=1)
	return fields
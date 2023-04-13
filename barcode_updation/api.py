# Copyright (c) 2023, venkatesh nayak and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

@frappe.whitelist()
def get_fields_details(item_group):
	fields = frappe.db.sql("""select name as website_item,item_code,web_item_name,website_image from `tabWebsite Item` where item_group = %s""",(item_group), as_dict=1)
	return fields


@frappe.whitelist()
def get_barcode(item):
	# barcode = frappe.db.get_value("Item Barcode",{"parent": item}, "barcode")
	barcode = frappe.get_all('Item Barcode', filters={'parent':item}, fields=['barcode'],limit =1)
	return barcode

@frappe.whitelist()
def get_country_fields_details(country):
	fields = frappe.db.sql("""select `tabWebsite Item`.name as website_item,`tabWebsite Item`.item_code,`tabWebsite Item`.web_item_name,`tabWebsite Item`.website_image,`tabItem`.country_of_origin from `tabWebsite Item` left join `tabItem` ON(`tabWebsite Item`.item_code=`tabItem`.item_code) where `tabItem`.country_of_origin = %s """,(country), as_dict=1)
	return fields
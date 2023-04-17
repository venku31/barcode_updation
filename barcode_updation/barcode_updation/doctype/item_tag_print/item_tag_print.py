# Copyright (c) 2023, venkatesh nayak and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ItemTagPrint(Document):
	pass

@frappe.whitelist()
def get_fields_details(item_group):
	fields = frappe.db.sql("""select `tabWebsite Item`.name as website_item,`tabWebsite Item`.item_code,`tabWebsite Item`.web_item_name,`tabWebsite Item`.website_image,`tabItem Price`.uom,`tabItem Price`.price_list_rate from `tabWebsite Item`,`tabItem Price` where `tabWebsite Item`.item_code=`tabItem Price`.item_code and `tabItem Price`.price_list="Premium Shop Item Price"  and `tabWebsite Item`.item_group = %s""",(item_group), as_dict=1)
	return fields
	
@frappe.whitelist()
def get_country_fields_details(country):
	fields = frappe.db.sql("""select `tabWebsite Item`.name as website_item,`tabWebsite Item`.item_code,`tabWebsite Item`.web_item_name,`tabWebsite Item`.website_image,`tabItem`.country_of_origin from `tabWebsite Item` left join `tabItem` ON(`tabWebsite Item`.item_code=`tabItem`.item_code) where `tabItem`.country_of_origin = %s """,(item_group), as_dict=1)
	return fields
# Copyright (c) 2023, venkatesh nayak and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

# @frappe.whitelist()
# def get_fields_details(item_group):
#     fields = frappe.db.sql("""select name as website_item,item_code,web_item_name,website_image from `tabWebsite Item` where item_group = %s""",(item_group), as_dict=1)
#     return fields
@frappe.whitelist()
def get_fields_details(item_group=None,country=None):
    if country:
        # fields = frappe.db.sql("""select `tabWebsite Item`.name as website_item,`tabWebsite Item`.item_code,`tabWebsite Item`.web_item_name,`tabWebsite Item`.website_image,`tabItem`.country_of_origin from `tabWebsite Item` left join `tabItem` ON(`tabWebsite Item`.item_code=`tabItem`.item_code) where `tabItem`.country_of_origin = %s and `tabWebsite Item`.item_group = %s""",(country,item_group), as_dict=1)
        fields = frappe.db.sql("""Select a.website_item,a.item_code,a.web_item_name,a.website_image,a.uom,a.price_list_rate,b.country
        From (select `tabWebsite Item`.name as website_item,`tabWebsite Item`.item_code,`tabWebsite Item`.web_item_name,`tabWebsite Item`.website_image,`tabWebsite Item`.item_group,`tabItem Price`.uom,`tabItem Price`.price_list_rate 
        from `tabWebsite Item`,`tabItem Price` 
        where `tabWebsite Item`.item_code=`tabItem Price`.item_code and `tabItem Price`.price_list="Premium Shop Item Price")a
        LEFT JOIN 
        (select name,country_of_origin as country from `tabItem`)b ON (b.name=a.item_code) where b.country=%s and a.item_group=%s """,(country,item_group), as_dict=1)
        return fields
    if not country:
        # fields = frappe.db.sql("""select `tabWebsite Item`.name as website_item,`tabWebsite Item`.item_code,`tabWebsite Item`.web_item_name,`tabWebsite Item`.website_image,`tabItem`.country_of_origin from `tabWebsite Item` left join `tabItem` ON(`tabWebsite Item`.item_code=`tabItem`.item_code) where `tabWebsite Item`.item_group = %s """,(item_group), as_dict=1)
        fields = frappe.db.sql("""Select a.website_item,a.item_code,a.web_item_name,a.website_image,a.uom,a.price_list_rate,b.country
        From (select `tabWebsite Item`.name as website_item,`tabWebsite Item`.item_code,`tabWebsite Item`.web_item_name,`tabWebsite Item`.website_image,`tabWebsite Item`.item_group,`tabItem Price`.uom,`tabItem Price`.price_list_rate 
        from `tabWebsite Item`,`tabItem Price` 
        where `tabWebsite Item`.item_code=`tabItem Price`.item_code and `tabItem Price`.price_list="Premium Shop Item Price")a
        LEFT JOIN 
        (select name,country_of_origin as country from `tabItem`)b ON (b.name=a.item_code) where a.item_group=%s """,(item_group), as_dict=1)
        return fields

@frappe.whitelist()
def get_barcode(item):
    # barcode = frappe.db.get_value("Item Barcode",{"parent": item}, "barcode")
    barcode = frappe.get_all('Item Barcode', filters={'parent':item}, fields=['barcode'],limit =1)
    return barcode


@frappe.whitelist()
def get_country_fields_details(item_group=None,country=None):
    if item_group:
        # fields = frappe.db.sql("""select `tabWebsite Item`.name as website_item,`tabWebsite Item`.item_code,`tabWebsite Item`.web_item_name,`tabWebsite Item`.website_image,`tabItem`.country_of_origin from `tabWebsite Item` left join `tabItem` ON(`tabWebsite Item`.item_code=`tabItem`.item_code) where `tabItem`.country_of_origin = %s and `tabWebsite Item`.item_group = %s""",(country,item_group), as_dict=1)
        fields = frappe.db.sql("""Select a.website_item,a.item_code,a.web_item_name,a.website_image,a.uom,a.price_list_rate,b.country
        From (select `tabWebsite Item`.name as website_item,`tabWebsite Item`.item_code,`tabWebsite Item`.web_item_name,`tabWebsite Item`.website_image,`tabWebsite Item`.item_group,`tabItem Price`.uom,`tabItem Price`.price_list_rate 
        from `tabWebsite Item`,`tabItem Price` 
        where `tabWebsite Item`.item_code=`tabItem Price`.item_code and `tabItem Price`.price_list="Premium Shop Item Price")a
        LEFT JOIN 
        (select name,country_of_origin as country from `tabItem`)b ON (b.name=a.item_code) where b.country=%s and a.item_group=%s """,(country,item_group), as_dict=1)
        return fields
    if not item_group:
        # fields = frappe.db.sql("""select `tabWebsite Item`.name as website_item,`tabWebsite Item`.item_code,`tabWebsite Item`.web_item_name,`tabWebsite Item`.website_image,`tabItem`.country_of_origin from `tabWebsite Item` left join `tabItem` ON(`tabWebsite Item`.item_code=`tabItem`.item_code) where `tabItem`.country_of_origin = %s """,(country), as_dict=1)
        fields = frappe.db.sql("""Select a.website_item,a.item_code,a.web_item_name,a.website_image,a.uom,a.price_list_rate,b.country
        From (select `tabWebsite Item`.name as website_item,`tabWebsite Item`.item_code,`tabWebsite Item`.web_item_name,`tabWebsite Item`.website_image,`tabWebsite Item`.item_group,`tabItem Price`.uom,`tabItem Price`.price_list_rate 
        from `tabWebsite Item`,`tabItem Price` 
        where `tabWebsite Item`.item_code=`tabItem Price`.item_code and `tabItem Price`.price_list="Premium Shop Item Price")a
        LEFT JOIN 
        (select name,country_of_origin as country from `tabItem`)b ON (b.name=a.item_code) where b.country=%s """,(country), as_dict=1)
        return fields
    else :
        # fields = frappe.db.sql("""select `tabWebsite Item`.name as website_item,`tabWebsite Item`.item_code,`tabWebsite Item`.web_item_name,`tabWebsite Item`.website_image,`tabItem`.country_of_origin from `tabWebsite Item` left join `tabItem` ON(`tabWebsite Item`.item_code=`tabItem`.item_code) where `tabWebsite Item`.item_group = %s""",(item_group), as_dict=1)
        fields = frappe.db.sql("""Select a.website_item,a.item_code,a.web_item_name,a.website_image,a.uom,a.price_list_rate,b.country
        From (select `tabWebsite Item`.name as website_item,`tabWebsite Item`.item_code,`tabWebsite Item`.web_item_name,`tabWebsite Item`.website_image,`tabWebsite Item`.item_group,`tabItem Price`.uom,`tabItem Price`.price_list_rate 
        from `tabWebsite Item`,`tabItem Price` 
        where `tabWebsite Item`.item_code=`tabItem Price`.item_code and `tabItem Price`.price_list="Premium Shop Item Price")a
        LEFT JOIN 
        (select name,country_of_origin as country from `tabItem`)b ON (b.name=a.item_code) where a.item_group=%s """,(item_group), as_dict=1)
        return fields

@frappe.whitelist()
def get_item_details(item):
    # fields = frappe.db.sql("""select name as website_item,item_code,web_item_name,website_image from `tabWebsite Item` where item_code = %s""",(item), as_dict=1)
        fields = frappe.db.sql("""Select a.website_item,a.item_code,a.web_item_name,a.website_image,a.uom,a.price_list_rate,b.country
        From (select `tabWebsite Item`.name as website_item,`tabWebsite Item`.item_code,`tabWebsite Item`.web_item_name,`tabWebsite Item`.website_image,`tabWebsite Item`.item_group,`tabItem Price`.uom,`tabItem Price`.price_list_rate 
        from `tabWebsite Item`,`tabItem Price` 
        where `tabWebsite Item`.item_code=`tabItem Price`.item_code and `tabItem Price`.price_list="Premium Shop Item Price")a
        LEFT JOIN 
        (select name,country_of_origin as country from `tabItem`)b ON (b.name=a.item_code) where a.item_code=%s """,(item), as_dict=1)
        return fields
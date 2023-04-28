# Copyright (c) 2023, venkatesh nayak and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ItemTagOfferPrint(Document):
	pass
@frappe.whitelist()
def search_item_offer_details(item_group=None,country=None):
    if country :
        fields = frappe.db.sql("""Select a.website_item,a.item_code,a.web_item_name,a.website_image,a.uom,a.price_list_rate,a.before,b.country
        From (select `tabWebsite Item`.name as website_item,`tabWebsite Item`.item_code,`tabWebsite Item`.web_item_name,`tabWebsite Item`.website_image,`tabWebsite Item`.item_group,`tabItem Price`.uom,`tabItem Price`.price_list_rate,`tabItem Price`.before
        from `tabWebsite Item`,`tabItem Price` 
        where `tabWebsite Item`.item_code=`tabItem Price`.item_code and `tabItem Price`.price_list="Premium Shop Selling")a
        LEFT JOIN 
        (select `tabItem`.name,`tabItem`.country_of_origin as country from `tabItem`,`tabPOS Offer`  where `tabItem`.name=`tabPOS Offer`.item and `tabPOS Offer`.warehouse="Premium Shop - PC")b ON (b.name=a.item_code and b.country=%s and a.item_group=%s) """,(country,item_group) , as_dict=1)
        return fields
    if not country:
        fields = frappe.db.sql("""Select a.website_item,a.item_code,a.web_item_name,a.website_image,a.uom,a.price_list_rate,a.before,b.country
        From (select `tabWebsite Item`.name as website_item,`tabWebsite Item`.item_code,`tabWebsite Item`.web_item_name,`tabWebsite Item`.website_image,`tabWebsite Item`.item_group,`tabItem Price`.uom,`tabItem Price`.price_list_rate,`tabItem Price`.before
        from `tabWebsite Item`,`tabItem Price` 
        where `tabWebsite Item`.item_code=`tabItem Price`.item_code and `tabItem Price`.price_list="Premium Shop Selling")a
        LEFT JOIN 
        (select `tabItem`.name,`tabItem`.country_of_origin as country from `tabItem`,`tabPOS Offer`  where `tabItem`.name=`tabPOS Offer`.item and `tabPOS Offer`.warehouse="Premium Shop - PC")b ON (b.name=a.item_code and a.item_group=%s) """,(item_group) , as_dict=1)
        return fields

@frappe.whitelist()
def search_country_offer_details(item_group=None,country=None):
    if item_group :
        fields = frappe.db.sql("""Select a.website_item,a.item_code,a.web_item_name,a.website_image,a.uom,a.price_list_rate,a.before,b.country
        From (select `tabWebsite Item`.name as website_item,`tabWebsite Item`.item_code,`tabWebsite Item`.web_item_name,`tabWebsite Item`.website_image,`tabWebsite Item`.item_group,`tabItem Price`.uom,`tabItem Price`.price_list_rate,`tabItem Price`.before 
        from `tabWebsite Item`,`tabItem Price` 
        where `tabWebsite Item`.item_code=`tabItem Price`.item_code and `tabItem Price`.price_list="Premium Shop Selling")a
        LEFT JOIN 
        (select `tabItem`.name,`tabItem`.country_of_origin as country from `tabItem`,`tabPOS Offer`  where `tabItem`.name=`tabPOS Offer`.item and `tabPOS Offer`.warehouse="Premium Shop - PC")b ON (b.name=a.item_code and b.country=%s and a.item_group=%s) """,(country,item_group) , as_dict=1)
        return fields
    if not item_group:
        fields = frappe.db.sql("""Select a.website_item,a.item_code,a.web_item_name,a.website_image,a.uom,a.price_list_rate,a.before,b.country
        From (select `tabWebsite Item`.name as website_item,`tabWebsite Item`.item_code,`tabWebsite Item`.web_item_name,`tabWebsite Item`.website_image,`tabWebsite Item`.item_group,`tabItem Price`.uom,`tabItem Price`.price_list_rate,`tabItem Price`.before
        from `tabWebsite Item`,`tabItem Price` 
        where `tabWebsite Item`.item_code=`tabItem Price`.item_code and `tabItem Price`.price_list="Premium Shop Selling")a
        LEFT JOIN 
        (select `tabItem`.name,`tabItem`.country_of_origin as country from `tabItem`,`tabPOS Offer`  where `tabItem`.name=`tabPOS Offer`.item and `tabPOS Offer`.warehouse="Premium Shop - PC")b ON (b.name=a.item_code and b.country=%s) """,(country) , as_dict=1)
        return fields

@frappe.whitelist()
def get_offer_item_details(item):
    fields = frappe.db.sql("""Select a.website_item,a.item_code,a.web_item_name,a.website_image,a.uom,a.price_list_rate,a.before,b.country
        From (select `tabWebsite Item`.name as website_item,`tabWebsite Item`.item_code,`tabWebsite Item`.web_item_name,`tabWebsite Item`.website_image,`tabWebsite Item`.item_group,`tabItem Price`.uom,`tabItem Price`.price_list_rate,`tabItem Price`.before
        from `tabWebsite Item`,`tabItem Price` 
        where `tabWebsite Item`.item_code=`tabItem Price`.item_code and `tabItem Price`.price_list="Premium Shop Selling")a
        RIGHT JOIN 
        (select `tabItem`.name,`tabItem`.country_of_origin as country from `tabItem`,`tabPOS Offer`  where `tabItem`.name=`tabPOS Offer`.item and `tabPOS Offer`.warehouse="Premium Shop - PC")b ON (b.name=a.item_code and a.item_code=%s) """,(item) , as_dict=1)
    return fields

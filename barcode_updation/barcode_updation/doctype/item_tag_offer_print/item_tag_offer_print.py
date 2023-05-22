# Copyright (c) 2023, venkatesh nayak and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ItemTagOfferPrint(Document):
	pass
@frappe.whitelist()
def search_item_offer_details(item_group=None,country=None):
    # default_price_list = frappe.db.get_single_value("Barcode Updation Settings", "default_price_list")
    # if country:
    #     fields = frappe.db.sql("""Select a.website_item,a.item_code,a.web_item_name,a.website_image,a.uom,round(a.price_list_rate,2) as price_list_rate,b.country,a.before
    #     From (select `tabWebsite Item`.name as website_item,`tabWebsite Item`.item_code,`tabWebsite Item`.web_item_name,`tabWebsite Item`.website_image,`tabWebsite Item`.item_group,`tabItem Price`.uom,`tabItem Price`.before,round(`tabItem Price`.price_list_rate,2) as price_list_rate
    #     from `tabWebsite Item`,`tabItem Price` 
    #     where `tabWebsite Item`.item_code=`tabItem Price`.item_code and `tabItem Price`.price_list='%(default_price_list)s')a
    #     LEFT JOIN 
    #     (select name,country_of_origin as country from `tabItem`)b ON (b.name=a.item_code) where b.country='%(country)s' and a.item_group='%(item_group)s' """%{"default_price_list":default_price_list,"country":country,"item_group":item_group}, as_dict=1)
    #     return fields
    # if not country:
    #     fields = frappe.db.sql("""Select a.website_item,a.item_code,a.web_item_name,a.website_image,a.uom,round(a.price_list_rate,2) as price_list_rate,b.country,a.before
    #     From (select `tabWebsite Item`.name as website_item,`tabWebsite Item`.item_code,`tabWebsite Item`.web_item_name,`tabWebsite Item`.website_image,`tabWebsite Item`.item_group,`tabItem Price`.uom,round(`tabItem Price`.price_list_rate,2) as price_list_rate,`tabItem Price`.before
    #     from `tabWebsite Item`,`tabItem Price` 
    #     where `tabWebsite Item`.item_code=`tabItem Price`.item_code and `tabItem Price`.price_list='%(default_price_list)s')a
    #     LEFT JOIN 
    #     (select name,country_of_origin as country from `tabItem`)b ON (b.name=a.item_code) where a.item_group='%(item_group)s' """%{"default_price_list":default_price_list,"item_group":item_group}, as_dict=1)
    #     return fields
    default_price_list = frappe.db.get_single_value("Barcode Updation Settings", "default_price_list")
    if country:
        fields = frappe.db.sql("""Select item.item_code,item.item_name,off.name as posoffer,off.title,off.description,off.apply_on,off.offer,off.warehouse,off.item,off.item_group,off.valid_upto,off.discount_type,off.discount_amount,off.discount_percentage,
        item.country_of_origin as country,item.stock_uom,item.image,price.price_list,price.price_list_rate,price.before
        from `tabPOS Offer` off LEFT JOIN `tabItem` item ON(off.item=item.name) 
        LEFT JOIN `tabItem Price` price ON (price.item_code=off.item) where off.disable=0 and price.price_list='%(default_price_list)s' and item.country_of_origin='%(country)s' and off.item_group='%(item_group)s' """%{"default_price_list":default_price_list,"country":country,"item_group":item_group}, as_dict=1)
        return fields
    if not country:
        fields = frappe.db.sql("""Select item.item_code,item.item_name,off.name as posoffer,off.title,off.description,off.apply_on,off.offer,off.warehouse,off.item,off.item_group,off.valid_upto,off.discount_type,off.discount_amount,off.discount_percentage,
        item.country_of_origin as country,item.stock_uom,item.image,price.price_list,price.price_list_rate,price.before
        from `tabPOS Offer` off LEFT JOIN `tabItem` item ON(off.item=item.name) 
        LEFT JOIN `tabItem Price` price ON (price.item_code=off.item) where off.disable=0 and price.price_list='%(default_price_list)s' and off.item_group='%(item_group)s' """%{"default_price_list":default_price_list,"item_group":item_group}, as_dict=1)
        return fields

@frappe.whitelist()
def search_country_offer_details(item_group=None,country=None):
    # if item_group :
    #     fields = frappe.db.sql("""Select a.website_item,a.item_code,a.web_item_name,a.website_image,a.uom,a.price_list_rate,a.before,b.country
    #     From (select `tabWebsite Item`.name as website_item,`tabWebsite Item`.item_code,`tabWebsite Item`.web_item_name,`tabWebsite Item`.website_image,`tabWebsite Item`.item_group,`tabItem Price`.uom,`tabItem Price`.price_list_rate,`tabItem Price`.before 
    #     from `tabWebsite Item`,`tabItem Price` 
    #     where `tabWebsite Item`.item_code=`tabItem Price`.item_code and `tabItem Price`.price_list="Premium Shop Selling")a
    #     LEFT JOIN 
    #     (select `tabItem`.name,`tabItem`.country_of_origin as country from `tabItem`,`tabPOS Offer`  where `tabItem`.name=`tabPOS Offer`.item and `tabPOS Offer`.warehouse="Premium Shop - PC")b ON (b.name=a.item_code and b.country=%s and a.item_group=%s) """,(country,item_group) , as_dict=1)
    #     return fields
    # if not item_group:
    #     fields = frappe.db.sql("""Select a.website_item,a.item_code,a.web_item_name,a.website_image,a.uom,a.price_list_rate,a.before,b.country
    #     From (select `tabWebsite Item`.name as website_item,`tabWebsite Item`.item_code,`tabWebsite Item`.web_item_name,`tabWebsite Item`.website_image,`tabWebsite Item`.item_group,`tabItem Price`.uom,`tabItem Price`.price_list_rate,`tabItem Price`.before
    #     from `tabWebsite Item`,`tabItem Price` 
    #     where `tabWebsite Item`.item_code=`tabItem Price`.item_code and `tabItem Price`.price_list="Premium Shop Selling")a
    #     LEFT JOIN 
    #     (select `tabItem`.name,`tabItem`.country_of_origin as country from `tabItem`,`tabPOS Offer`  where `tabItem`.name=`tabPOS Offer`.item and `tabPOS Offer`.warehouse="Premium Shop - PC")b ON (b.name=a.item_code and b.country=%s) """,(country) , as_dict=1)
    #     return fields
    default_price_list = frappe.db.get_single_value("Barcode Updation Settings", "default_price_list")
    if item_group:
        # fields = frappe.db.sql("""select `tabWebsite Item`.name as website_item,`tabWebsite Item`.item_code,`tabWebsite Item`.web_item_name,`tabWebsite Item`.website_image,`tabItem`.country_of_origin from `tabWebsite Item` left join `tabItem` ON(`tabWebsite Item`.item_code=`tabItem`.item_code) where `tabItem`.country_of_origin = %s and `tabWebsite Item`.item_group = %s""",(country,item_group), as_dict=1)
        fields = frappe.db.sql("""Select a.website_item,a.item_code,a.web_item_name,a.website_image,a.uom,a.price_list_rate,b.country,a.before
        From (select `tabWebsite Item`.name as website_item,`tabWebsite Item`.item_code,`tabWebsite Item`.web_item_name,`tabWebsite Item`.website_image,`tabWebsite Item`.item_group,`tabItem Price`.uom,`tabItem Price`.price_list_rate,`tabItem Price`.before 
        from `tabWebsite Item`,`tabItem Price` 
        where `tabWebsite Item`.item_code=`tabItem Price`.item_code and `tabItem Price`.price_list='%(default_price_list)s')a
        LEFT JOIN 
        (select name,country_of_origin as country from `tabItem`)b ON (b.name=a.item_code) where b.country='%(country)s' and a.item_group='%(item_group)s' """ %{"default_price_list":default_price_list,"country":country,"item_group":item_group}, as_dict=1)
        return fields
    if not item_group:
        # fields = frappe.db.sql("""select `tabWebsite Item`.name as website_item,`tabWebsite Item`.item_code,`tabWebsite Item`.web_item_name,`tabWebsite Item`.website_image,`tabItem`.country_of_origin from `tabWebsite Item` left join `tabItem` ON(`tabWebsite Item`.item_code=`tabItem`.item_code) where `tabItem`.country_of_origin = %s """,(country), as_dict=1)
        fields = frappe.db.sql("""Select a.website_item,a.item_code,a.web_item_name,a.website_image,a.uom,a.price_list_rate,b.country,a.before
        From (select `tabWebsite Item`.name as website_item,`tabWebsite Item`.item_code,`tabWebsite Item`.web_item_name,`tabWebsite Item`.website_image,`tabWebsite Item`.item_group,`tabItem Price`.uom,`tabItem Price`.price_list_rate 
        from `tabWebsite Item`,`tabItem Price` 
        where `tabWebsite Item`.item_code=`tabItem Price`.item_code and `tabItem Price`.price_list='%(default_price_list)s')a
        LEFT JOIN 
        (select name,country_of_origin as country from `tabItem`)b ON (b.name=a.item_code) where b.country='%(country)s' """ %{"default_price_list":default_price_list,"country":country}, as_dict=1)
        return fields
    else :
        # fields = frappe.db.sql("""select `tabWebsite Item`.name as website_item,`tabWebsite Item`.item_code,`tabWebsite Item`.web_item_name,`tabWebsite Item`.website_image,`tabItem`.country_of_origin from `tabWebsite Item` left join `tabItem` ON(`tabWebsite Item`.item_code=`tabItem`.item_code) where `tabWebsite Item`.item_group = %s""",(item_group), as_dict=1)
        fields = frappe.db.sql("""Select a.website_item,a.item_code,a.web_item_name,a.website_image,a.uom,a.price_list_rate,b.country,a.before
        From (select `tabWebsite Item`.name as website_item,`tabWebsite Item`.item_code,`tabWebsite Item`.web_item_name,`tabWebsite Item`.website_image,`tabWebsite Item`.item_group,`tabItem Price`.uom,`tabItem Price`.price_list_rate,`tabItem Price`.before 
        from `tabWebsite Item`,`tabItem Price` 
        where `tabWebsite Item`.item_code=`tabItem Price`.item_code and `tabItem Price`.price_list='%(default_price_list)s')a
        LEFT JOIN 
        (select name,country_of_origin as country from `tabItem`)b ON (b.name=a.item_code) where a.item_group='%(item_group)s' """ %{"default_price_list":default_price_list,"item_group":item_group}, as_dict=1)
        return fields

@frappe.whitelist()
def get_offer_item_details(item):
    # fields = frappe.db.sql("""Select a.website_item,a.item_code,a.web_item_name,a.website_image,a.uom,a.price_list_rate,a.before,b.country
    #     From (select `tabWebsite Item`.name as website_item,`tabWebsite Item`.item_code,`tabWebsite Item`.web_item_name,`tabWebsite Item`.website_image,`tabWebsite Item`.item_group,`tabItem Price`.uom,`tabItem Price`.price_list_rate,`tabItem Price`.before
    #     from `tabWebsite Item`,`tabItem Price` 
    #     where `tabWebsite Item`.item_code=`tabItem Price`.item_code and `tabItem Price`.price_list="Premium Shop Selling")a
    #     RIGHT JOIN 
    #     (select `tabItem`.name,`tabItem`.country_of_origin as country from `tabItem`,`tabPOS Offer`  where `tabItem`.name=`tabPOS Offer`.item and `tabPOS Offer`.warehouse="Premium Shop - PC")b ON (b.name=a.item_code and a.item_code=%s) """,(item) , as_dict=1)
    # return fields
    default_price_list = frappe.db.get_single_value("Barcode Updation Settings", "default_price_list")
    # fields = frappe.db.sql("""Select a.website_item,a.item_code,a.web_item_name,a.website_image,a.uom,a.price_list_rate,b.country
    #     From (select `tabWebsite Item`.name as website_item,`tabWebsite Item`.item_code,`tabWebsite Item`.web_item_name,`tabWebsite Item`.website_image,`tabWebsite Item`.item_group,`tabItem Price`.uom,`tabItem Price`.price_list_rate 
    #     from `tabWebsite Item`,`tabItem Price` 
    #     where `tabWebsite Item`.item_code=`tabItem Price`.item_code and `tabItem Price`.price_list='%(default_price_list)s')a
    #     LEFT JOIN 
    #     (select name,country_of_origin as country from `tabItem`)b ON (b.name=a.item_code) where a.item_code='%(item)s' """%{"default_price_list":default_price_list,"item":item}, as_dict=1)
    fields = frappe.db.sql("""Select item.item_code,item.item_name,off.name as posoffer,off.title,off.description,off.apply_on,off.offer,off.warehouse,off.item,off.item_group,off.valid_upto,off.discount_type,off.discount_amount,off.discount_percentage,
        item.country_of_origin as country,item.stock_uom,item.image,price.price_list,price.price_list_rate,price.before
        from `tabPOS Offer` off LEFT JOIN `tabItem` item ON(off.item=item.name) 
        LEFT JOIN `tabItem Price` price ON (price.item_code=off.item) where off.disable=0 and price.price_list='%(default_price_list)s' and item.item_code='%(item)s' """%{"default_price_list":default_price_list,"item":item}, as_dict=1)
    return fields
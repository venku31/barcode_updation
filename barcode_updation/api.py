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
        where `tabWebsite Item`.item_code=`tabItem Price`.item_code and `tabItem Price`.price_list="Premium Shop Selling")a
        LEFT JOIN 
        (select name,country_of_origin as country from `tabItem`)b ON (b.name=a.item_code) where b.country=%s and a.item_group=%s """,(country,item_group), as_dict=1)
        return fields
    if not country:
        # fields = frappe.db.sql("""select `tabWebsite Item`.name as website_item,`tabWebsite Item`.item_code,`tabWebsite Item`.web_item_name,`tabWebsite Item`.website_image,`tabItem`.country_of_origin from `tabWebsite Item` left join `tabItem` ON(`tabWebsite Item`.item_code=`tabItem`.item_code) where `tabWebsite Item`.item_group = %s """,(item_group), as_dict=1)
        fields = frappe.db.sql("""Select a.website_item,a.item_code,a.web_item_name,a.website_image,a.uom,a.price_list_rate,b.country
        From (select `tabWebsite Item`.name as website_item,`tabWebsite Item`.item_code,`tabWebsite Item`.web_item_name,`tabWebsite Item`.website_image,`tabWebsite Item`.item_group,`tabItem Price`.uom,`tabItem Price`.price_list_rate 
        from `tabWebsite Item`,`tabItem Price` 
        where `tabWebsite Item`.item_code=`tabItem Price`.item_code and `tabItem Price`.price_list="Premium Shop Selling")a
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
        where `tabWebsite Item`.item_code=`tabItem Price`.item_code and `tabItem Price`.price_list="Premium Shop Selling")a
        LEFT JOIN 
        (select name,country_of_origin as country from `tabItem`)b ON (b.name=a.item_code) where b.country=%s and a.item_group=%s """,(country,item_group), as_dict=1)
        return fields
    if not item_group:
        # fields = frappe.db.sql("""select `tabWebsite Item`.name as website_item,`tabWebsite Item`.item_code,`tabWebsite Item`.web_item_name,`tabWebsite Item`.website_image,`tabItem`.country_of_origin from `tabWebsite Item` left join `tabItem` ON(`tabWebsite Item`.item_code=`tabItem`.item_code) where `tabItem`.country_of_origin = %s """,(country), as_dict=1)
        fields = frappe.db.sql("""Select a.website_item,a.item_code,a.web_item_name,a.website_image,a.uom,a.price_list_rate,b.country
        From (select `tabWebsite Item`.name as website_item,`tabWebsite Item`.item_code,`tabWebsite Item`.web_item_name,`tabWebsite Item`.website_image,`tabWebsite Item`.item_group,`tabItem Price`.uom,`tabItem Price`.price_list_rate 
        from `tabWebsite Item`,`tabItem Price` 
        where `tabWebsite Item`.item_code=`tabItem Price`.item_code and `tabItem Price`.price_list="Premium Shop Selling")a
        LEFT JOIN 
        (select name,country_of_origin as country from `tabItem`)b ON (b.name=a.item_code) where b.country=%s """,(country), as_dict=1)
        return fields
    else :
        # fields = frappe.db.sql("""select `tabWebsite Item`.name as website_item,`tabWebsite Item`.item_code,`tabWebsite Item`.web_item_name,`tabWebsite Item`.website_image,`tabItem`.country_of_origin from `tabWebsite Item` left join `tabItem` ON(`tabWebsite Item`.item_code=`tabItem`.item_code) where `tabWebsite Item`.item_group = %s""",(item_group), as_dict=1)
        fields = frappe.db.sql("""Select a.website_item,a.item_code,a.web_item_name,a.website_image,a.uom,a.price_list_rate,b.country
        From (select `tabWebsite Item`.name as website_item,`tabWebsite Item`.item_code,`tabWebsite Item`.web_item_name,`tabWebsite Item`.website_image,`tabWebsite Item`.item_group,`tabItem Price`.uom,`tabItem Price`.price_list_rate 
        from `tabWebsite Item`,`tabItem Price` 
        where `tabWebsite Item`.item_code=`tabItem Price`.item_code and `tabItem Price`.price_list="Premium Shop Selling")a
        LEFT JOIN 
        (select name,country_of_origin as country from `tabItem`)b ON (b.name=a.item_code) where a.item_group=%s """,(item_group), as_dict=1)
        return fields

@frappe.whitelist()
def get_item_details(item):
    # fields = frappe.db.sql("""select name as website_item,item_code,web_item_name,website_image from `tabWebsite Item` where item_code = %s""",(item), as_dict=1)
        fields = frappe.db.sql("""Select a.website_item,a.item_code,a.web_item_name,a.website_image,a.uom,a.price_list_rate,b.country
        From (select `tabWebsite Item`.name as website_item,`tabWebsite Item`.item_code,`tabWebsite Item`.web_item_name,`tabWebsite Item`.website_image,`tabWebsite Item`.item_group,`tabItem Price`.uom,`tabItem Price`.price_list_rate 
        from `tabWebsite Item`,`tabItem Price` 
        where `tabWebsite Item`.item_code=`tabItem Price`.item_code and `tabItem Price`.price_list="Premium Shop Selling")a
        LEFT JOIN 
        (select name,country_of_origin as country from `tabItem`)b ON (b.name=a.item_code) where a.item_code=%s """,(item), as_dict=1)
        return fields
@frappe.whitelist()
def search_barcode():
    # if not item_group and not country:
        # fields = frappe.db.sql("""select `tabWebsite Item`.name as website_item,`tabWebsite Item`.item_code,`tabWebsite Item`.web_item_name,`tabWebsite Item`.website_image,`tabItem`.country_of_origin from `tabWebsite Item` left join `tabItem` ON(`tabWebsite Item`.item_code=`tabItem`.item_code) where `tabItem`.country_of_origin = %s and `tabWebsite Item`.item_group = %s""",(country,item_group), as_dict=1)
    fields = frappe.db.sql("""Select a.website_item,a.item_code,a.web_item_name,a.website_image,a.uom,a.price_list_rate,b.country
        From (select `tabWebsite Item`.name as website_item,`tabWebsite Item`.item_code,`tabWebsite Item`.web_item_name,`tabWebsite Item`.website_image,`tabWebsite Item`.item_group,`tabItem Price`.uom,`tabItem Price`.price_list_rate 
        from `tabWebsite Item`,`tabItem Price` 
        where `tabWebsite Item`.item_code=`tabItem Price`.item_code and `tabItem Price`.price_list="Premium Shop Selling")a
        RIGHT JOIN 
        (select `tabItem`.name,`tabItem`.country_of_origin as country from `tabItem`,`tabPOS Offer`  where `tabItem`.name=`tabPOS Offer`.item and `tabPOS Offer`.warehouse="Premium Shop - PC")b ON (b.name=a.item_code) """, as_dict=1)
    return fields

@frappe.whitelist()
def get_item_summary(item_group):
    # fields = frappe.db.sql("""Select a.website_item,a.item_code,a.web_item_name,a.website_image,a.uom,a.price_list_rate,b.country
    #     From (select `tabWebsite Item`.name as website_item,`tabWebsite Item`.item_code,`tabWebsite Item`.web_item_name,`tabWebsite Item`.website_image,`tabWebsite Item`.item_group,`tabItem Price`.uom,`tabItem Price`.price_list_rate 
    #     from `tabWebsite Item`,`tabItem Price` 
    #     where `tabWebsite Item`.item_code=`tabItem Price`.item_code and `tabItem Price`.price_list="Premium Shop Selling")a
    #     LEFT JOIN 
    #     (select name,country_of_origin as country from `tabItem`)b ON (b.name=a.item_code) where a.item_group=%s """,(item_group), as_dict=1)
    # return fields
    fields = frappe.db.sql("""Select item.website_item as website_item,item.item_code,item.web_item_name,item.website_image,item.item_group,uom_price.uom1,
    uom_price.uom_price1,uom_price.uom2,uom_price.uom_price2,uom_price.uom3,uom_price.uom_price3,uom_price.uom4,uom_price.uom_price4
    From
(select name as website_item,item_code,web_item_name,website_image,item_group
from `tabWebsite Item`) item
LEFT JOIN        
(Select u1.parent,u1.uom1,u1.uom_price1,u2.uom2,u2.uom_price2,u3.uom3,u3.uom_price3,u4.uom4,u4.uom_price4
From
(Select a.parent,a.uom as uom1,b.price_list_rate as uom_price1 FROM `tabUOM Conversion Detail` a
LEFT JOIN `tabItem Price` b ON (a.parent=b.item_code and b.selling=1 and a.uom=b.uom and b.price_list="Premium Shop Selling") where a.idx=1)u1
LEFT JOIN
(Select a.parent as parent2,a.uom as uom2,b.price_list_rate as uom_price2 FROM `tabUOM Conversion Detail` a
LEFT JOIN `tabItem Price` b ON (a.parent=b.item_code and b.selling=1 and a.uom=b.uom and b.price_list="Premium Shop Selling") where a.idx=2)u2
ON(u1.parent=u2.parent2)
LEFT JOIN
(Select a.parent as parent3,a.uom as uom3,b.price_list_rate as uom_price3 FROM `tabUOM Conversion Detail` a
LEFT JOIN `tabItem Price` b ON (a.parent=b.item_code and b.selling=1 and a.uom=b.uom and b.price_list="Premium Shop Selling") where a.idx=3)u3
ON(u1.parent=u3.parent3)
LEFT JOIN
(Select a.parent as parent4,a.uom as uom4,b.price_list_rate as uom_price4 FROM `tabUOM Conversion Detail` a
LEFT JOIN `tabItem Price` b ON (a.parent=b.item_code and b.selling=1 and a.uom=b.uom and b.price_list="Premium Shop Selling") where a.idx=4)u4
ON(u1.parent=u4.parent4))uom_price
ON(item.item_code=uom_price.parent) where item.item_group=%s """,(item_group), as_dict=1)
    return fields

@frappe.whitelist()
def get_itemwise_summary(item):
    # fields = frappe.db.sql("""Select a.website_item,a.item_code,a.web_item_name,a.website_image,a.uom,a.price_list_rate,b.country
    #     From (select `tabWebsite Item`.name as website_item,`tabWebsite Item`.item_code,`tabWebsite Item`.web_item_name,`tabWebsite Item`.website_image,`tabWebsite Item`.item_group,`tabItem Price`.uom,`tabItem Price`.price_list_rate 
    #     from `tabWebsite Item`,`tabItem Price` 
    #     where `tabWebsite Item`.item_code=`tabItem Price`.item_code and `tabItem Price`.price_list="Premium Shop Selling")a
    #     LEFT JOIN 
    #     (select name,country_of_origin as country from `tabItem`)b ON (b.name=a.item_code) where a.item_group=%s """,(item_group), as_dict=1)
    # return fields
    fields = frappe.db.sql("""Select item.website_item as website_item,item.item_code,item.web_item_name,item.website_image,item.item_group,uom_price.uom1,
    uom_price.uom_price1,uom_price.uom2,uom_price.uom_price2,uom_price.uom3,uom_price.uom_price3,uom_price.uom4,uom_price.uom_price4
    From
(select name as website_item,item_code,web_item_name,website_image,item_group
from `tabWebsite Item`) item
LEFT JOIN        
(Select u1.parent,u1.uom1,u1.uom_price1,u2.uom2,u2.uom_price2,u3.uom3,u3.uom_price3,u4.uom4,u4.uom_price4
From
(Select a.parent,a.uom as uom1,b.price_list_rate as uom_price1 FROM `tabUOM Conversion Detail` a
LEFT JOIN `tabItem Price` b ON (a.parent=b.item_code and b.selling=1 and a.uom=b.uom and b.price_list="Premium Shop Selling") where a.idx=1)u1
LEFT JOIN
(Select a.parent as parent2,a.uom as uom2,b.price_list_rate as uom_price2 FROM `tabUOM Conversion Detail` a
LEFT JOIN `tabItem Price` b ON (a.parent=b.item_code and b.selling=1 and a.uom=b.uom and b.price_list="Premium Shop Selling") where a.idx=2)u2
ON(u1.parent=u2.parent2)
LEFT JOIN
(Select a.parent as parent3,a.uom as uom3,b.price_list_rate as uom_price3 FROM `tabUOM Conversion Detail` a
LEFT JOIN `tabItem Price` b ON (a.parent=b.item_code and b.selling=1 and a.uom=b.uom and b.price_list="Premium Shop Selling") where a.idx=3)u3
ON(u1.parent=u3.parent3)
LEFT JOIN
(Select a.parent as parent4,a.uom as uom4,b.price_list_rate as uom_price4 FROM `tabUOM Conversion Detail` a
LEFT JOIN `tabItem Price` b ON (a.parent=b.item_code and b.selling=1 and a.uom=b.uom and b.price_list="Premium Shop Selling") where a.idx=4)u4
ON(u1.parent=u4.parent4))uom_price
ON(item.item_code=uom_price.parent) where item.item_code=%s """,(item), as_dict=1)
    return fields
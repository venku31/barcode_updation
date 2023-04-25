# Copyright (c) 2023, venkatesh nayak and Contributors
# See license.txt

import frappe
import unittest

# class TestItemTagOfferPrint(unittest.TestCase):
# 	pass
@frappe.whitelist()
def search_item_offer_details():
    fields = frappe.db.sql("""Select a.website_item,a.item_code,a.web_item_name,a.website_image,a.uom,a.price_list_rate,b.country
        From (select `tabWebsite Item`.name as website_item,`tabWebsite Item`.item_code,`tabWebsite Item`.web_item_name,`tabWebsite Item`.website_image,`tabWebsite Item`.item_group,`tabItem Price`.uom,`tabItem Price`.price_list_rate 
        from `tabWebsite Item`,`tabItem Price` 
        where `tabWebsite Item`.item_code=`tabItem Price`.item_code and `tabItem Price`.price_list="Premium Shop Selling")a
        RIGHT JOIN 
        (select `tabItem`.name,`tabItem`.country_of_origin as country from `tabItem`,`tabPOS Offer`  where `tabItem`.name=`tabPOS Offer`.item and `tabPOS Offer`.warehouse="Premium Shop - PC")b ON (b.name=a.item_code) """, as_dict=1)
    return fields
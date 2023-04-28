# Copyright (c) 2023, venkatesh nayak and Contributors
# See license.txt

# import frappe
import unittest

class TestStockCheckSummaryDetails(unittest.TestCase):
	pass

# @frappe.whitelist()
# def get_stock_check_data(warehouse,transaction_date):
#     fields = frappe.db.sql("""Select `tabStock Check Details`.item_code,`tabStock Check Details`.item_name,`tabStock Check Details`.warehouse,sum(`tabStock Check Details`.qty) as qty,`tabStock Check Details`.stock_uom,`tabStock Check`.transaction_date 
# 	From `tabStock Check Details` LEFT JOIN `tabStock Check` 
# 	ON (`tabStock Check Details`.parent=`tabStock Check`.name and `tabStock Check`.docstatus=1) group by `tabStock Check Details`.item_code,`tabStock Check Details`.stock_uom,`tabStock Check Details`.warehouse
# 	having `tabStock Check Details`.warehouse = %(warehouse)s and `tabStock Check`.transaction_date = %(transaction_date)s) """,("warehouse":warehouse,"transaction_date":transaction_date) , as_dict=1)
#     return fields
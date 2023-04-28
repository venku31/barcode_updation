# Copyright (c) 2023, venkatesh nayak and contributors
# For license information, please see license.txt

import frappe
import json
from erpnext.stock.utils import get_stock_balance
from frappe.model.document import Document

class StockCheckSummary(Document):
	pass
@frappe.whitelist()
def get_stock_check_data(warehouse,from_date,to_date):
    fields = frappe.db.sql("""Select `tabStock Check Details`.item_code,`tabStock Check Details`.item_name,`tabStock Check Details`.warehouse,sum(`tabStock Check Details`.qty) as qty,`tabStock Check Details`.stock_uom,`tabStock Check`.transaction_date,
	(select sum(actual_qty) from tabBin where item_code=`tabStock Check Details`.item_code and warehouse = `tabStock Check Details`.warehouse) as actual_qty
	From `tabStock Check Details` LEFT JOIN `tabStock Check` 
	ON (`tabStock Check Details`.parent=`tabStock Check`.name and `tabStock Check`.docstatus=1) group by `tabStock Check Details`.item_code,`tabStock Check Details`.stock_uom,`tabStock Check Details`.warehouse
	having `tabStock Check Details`.warehouse = %(warehouse)s and `tabStock Check`.transaction_date >= %(from_date)s and `tabStock Check`.transaction_date <= %(to_date)s """,{"warehouse":warehouse,"from_date":from_date,"to_date":to_date} , as_dict=1)
    return fields
	
@frappe.whitelist()
def create_stock_adjust(item_code,warehouse,qty,stock_uom):
	try:
		sa_doc = frappe.new_doc("Stock Reconciliation")
		sa_doc.purpose = "Stock Reconciliation"
		sa_doc.difference_amount = 0.0
		# product = json.loads(product_description)
		# for i in product:
		sa_doc.append("items", {
            "item_code":item_code,
            "warehouse":warehouse,
            "qty": qty,
            "stock_uom": stock_uom,
			"valuation_rate":  1,
    	})
		sa_doc.flags.ignore_mandatory = True
		sa_doc.set_missing_values()
		sa_doc.insert(ignore_permissions=True)
		sa_doc.submit()
		frappe.db.commit()
		return {"Stock Reconciliation Successfully Created ":sa_doc.name}
	except Exception as e:
            return {"error":e}
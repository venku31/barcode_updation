// Copyright (c) 2023, venkatesh nayak and contributors
// For license information, please see license.txt

frappe.ui.form.on('Stock Check Summary', {
	get_data: function(frm) {
		get_stock_check_data(frm);
	},
	validate: function(frm) {
		get_stock_check_data(frm);
	},
	on_submit: function(frm, cdt, cdn) {
		$.each(frm.doc.stock_check_summary_details || [], function(i, d) {
			frappe.call({
					method: "barcode_updation.barcode_updation.doctype.stock_check_summary.stock_check_summary.create_stock_adjust",
					args: { 
						item_code:d.item_code,
						warehouse:d.warehouse,
						qty:d.qty,
						stock_uom:d.stock_uom,
						// product_description:frm.doc.stock_check_summary_details
					},
					callback: function(r) {
						var pi = r.message
						alert("Stock Recociliation Created",r);
					}
				});	
			
		
		 })
		  refresh_field("stock_check_summary_details");
	}
});

function get_stock_check_data(frm) {
	console.log("1")
	frappe.call({
	  "method": "barcode_updation.barcode_updation.doctype.stock_check_summary.stock_check_summary.get_stock_check_data",
	  "args": {
		"warehouse": frm.doc.warehouse,
		"from_date": frm.doc.from_date,
		"to_date": frm.doc.to_date,
	   },
	  callback: function (r) {
		console.log(r)
		cur_frm.clear_table("stock_check_summary_details");
		r.message.forEach(fields => {
		  var child = cur_frm.add_child("stock_check_summary_details");
		  frappe.model.set_value(child.doctype, child.name, "item_code", fields.item_code)
		  frappe.model.set_value(child.doctype, child.name, "item_name", fields.item_name)
		  frappe.model.set_value(child.doctype, child.name, "warehouse", fields.warehouse)
		  frappe.model.set_value(child.doctype, child.name, "qty", fields.qty)
		  frappe.model.set_value(child.doctype, child.name, "balance_qty", fields.actual_qty)
		  frappe.model.set_value(child.doctype, child.name, "stock_uom", fields.stock_uom)
		  });
		cur_frm.refresh_fields()
			
	  }
	  
	});
// cur_frm.fields_dict.my_field.$input.on("click", function(evt){

// })

}


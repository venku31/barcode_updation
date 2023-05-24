// Copyright (c) 2023, venkatesh nayak and contributors
// For license information, please see license.txt

frappe.ui.form.on('Stock Check', {
	scan_barcode : function(frm, cdt, cdn){
		fetch_item_entry(frm, cdt, cdn);
		
	},
	validate : function(frm, cdt, cdn){
	cur_frm.set_value("created_by", frappe.session.user);
	total_qty(frm, cdt, cdn);
	}
});
function fetch_item_entry(frm, cdt, cdn) {
	console.log("1")
	frappe.call({
	  "method": "barcode_updation.barcode_updation.doctype.stock_check.stock_check.search_item",
	  "args": {
		"item": frm.doc.scan_barcode,
		"warehouse": frm.doc.warehouse,
	   },
	  callback: function (r) {
		console.log(r)
		// cur_frm.clear_table("details");
		r.message.forEach(stock => {
		  var child = cur_frm.add_child("items");
		  cur_frm.set_value("scan_barcode","")
		  frappe.model.set_value(child.doctype, child.name, "item_code", stock.item_code)
		  frappe.model.set_value(child.doctype, child.name, "warehouse",frm.doc.warehouse)
		  frappe.model.set_value(child.doctype, child.name, "qty", 1)
		  frappe.model.set_value(child.doctype, child.name, "stock_uom", stock.stock_uom)
		  frappe.model.set_value(child.doctype, child.name, "item_name", stock.item_name)
		  });
	    cur_frm.refresh_fields()
			
	  }
	  
	});
	cur_frm.fields_dict.my_field.$input.on("click", function(evt){

	})
};

frappe.ui.form.on('Stock Check Details', {
qty: function(frm, cdt, cdn) {
	total_qty(frm, cdt, cdn)
	frm.save();
	}
})
function total_qty(frm, cdt, cdn) {
    // estimated_amount: function(frm, cdt, cdn) {
    var d = locals[cdt][cdn];
    var total_qty = 0;
    frm.doc.items.forEach(function(d) { total_qty += d.qty});
    frm.set_value('total_qty', total_qty);
    }	
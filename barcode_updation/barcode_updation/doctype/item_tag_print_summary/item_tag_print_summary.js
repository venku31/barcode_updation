// Copyright (c) 2023, venkatesh nayak and contributors
// For license information, please see license.txt

frappe.ui.form.on('Item Tag Print Summary', {
	// refresh: function(frm) {
	item_group : function(frm){
		get_item_summary(frm);
		cur_frm.refresh_fields()
	},
	item : function(frm){
		get_itemwise_summary(frm);
		cur_frm.refresh_fields()
	},
	// }
});

function get_item_summary(frm) {
	console.log("1")
	frappe.call({
	  "method": "barcode_updation.api.get_item_summary",
	  "args": {
		"item_group": frm.doc.item_group,
		// "country": frm.doc.country,
	   },
	  callback: function (r) {
		console.log(r)
		cur_frm.clear_table("item_tag_details_summary");
		r.message.forEach(fields => {
		  var child = cur_frm.add_child("item_tag_details_summary");
		  frappe.model.set_value(child.doctype, child.name, "item_code", fields.item_code)
		  frappe.model.set_value(child.doctype, child.name, "website_item_name", fields.website_item)
		  frappe.model.set_value(child.doctype, child.name, "description", fields.web_item_name)
		  frappe.model.set_value(child.doctype, child.name, "website_image", fields.website_image)
		  frappe.model.set_value(child.doctype, child.name, "price1", fields.uom_price1)
		  frappe.model.set_value(child.doctype, child.name, "uom1", fields.uom1)
		  frappe.model.set_value(child.doctype, child.name, "price2", fields.uom_price2)
		  frappe.model.set_value(child.doctype, child.name, "uom2", fields.uom2)
		  frappe.model.set_value(child.doctype, child.name, "price3", fields.uom_price3)
		  frappe.model.set_value(child.doctype, child.name, "uom3", fields.uom3)
		  frappe.model.set_value(child.doctype, child.name, "price4", fields.uom_price4)
		  frappe.model.set_value(child.doctype, child.name, "uom4", fields.uom4)
		//   frappe.model.set_value(child.doctype, child.name, "country", fields.country)
		  });
		cur_frm.refresh_fields()
			
	  }
	  
	});
}
function get_itemwise_summary(frm) {
	console.log("1")
	frappe.call({
	  "method": "barcode_updation.api.get_itemwise_summary",
	  "args": {
		"item": frm.doc.item,
		// "country": frm.doc.country,
	   },
	  callback: function (r) {
		console.log(r)
		// cur_frm.clear_table("item_tag_details_summary");
		r.message.forEach(fields => {
		  var child = cur_frm.add_child("item_tag_details_summary");
		  frappe.model.set_value(child.doctype, child.name, "item_code", fields.item_code)
		  frappe.model.set_value(child.doctype, child.name, "website_item_name", fields.website_item)
		  frappe.model.set_value(child.doctype, child.name, "description", fields.web_item_name)
		  frappe.model.set_value(child.doctype, child.name, "website_image", fields.website_image)
		  frappe.model.set_value(child.doctype, child.name, "price1", fields.uom_price1)
		  frappe.model.set_value(child.doctype, child.name, "uom1", fields.uom1)
		  frappe.model.set_value(child.doctype, child.name, "price2", fields.uom_price2)
		  frappe.model.set_value(child.doctype, child.name, "uom2", fields.uom2)
		  frappe.model.set_value(child.doctype, child.name, "price3", fields.uom_price3)
		  frappe.model.set_value(child.doctype, child.name, "uom3", fields.uom3)
		  frappe.model.set_value(child.doctype, child.name, "price4", fields.uom_price4)
		  frappe.model.set_value(child.doctype, child.name, "uom4", fields.uom4)
		//   frappe.model.set_value(child.doctype, child.name, "country", fields.country)
		  });
		cur_frm.refresh_fields()
			
	  }
	  
	});
}
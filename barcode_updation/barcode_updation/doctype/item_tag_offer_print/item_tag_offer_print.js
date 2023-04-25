// Copyright (c) 2023, venkatesh nayak and contributors
// For license information, please see license.txt

frappe.ui.form.on('Item Tag Offer Print', {
	item_group : function(frm){
		get_offer_item(frm);
		cur_frm.refresh_fields()
		},
	country : function(frm){
		get_country_offer_item(frm);
		cur_frm.refresh_fields()
		},
	item : function(frm){
		get_offer_item_det(frm);
		cur_frm.refresh_fields()
		},
});


function get_offer_item(frm) {
	console.log("1")
	frappe.call({
	  "method": "barcode_updation.barcode_updation.doctype.item_tag_offer_print.item_tag_offer_print.search_item_offer_details",
	  "args": {
		"item_group": frm.doc.item_group,
		"country": frm.doc.country,
	   },
	  callback: function (r) {
		console.log(r)
		cur_frm.clear_table("item_tag_offer_details");
		r.message.forEach(fields => {
		  var child = cur_frm.add_child("item_tag_offer_details");
		  frappe.model.set_value(child.doctype, child.name, "item_code", fields.item_code)
		  frappe.model.set_value(child.doctype, child.name, "website_item_name", fields.website_item)
		  frappe.model.set_value(child.doctype, child.name, "description", fields.web_item_name)
		  frappe.model.set_value(child.doctype, child.name, "website_image", fields.website_image)
		  frappe.model.set_value(child.doctype, child.name, "price", fields.price_list_rate)
		  frappe.model.set_value(child.doctype, child.name, "before", fields.before)
		  frappe.model.set_value(child.doctype, child.name, "uom", fields.uom)
		  frappe.model.set_value(child.doctype, child.name, "country", fields.country)
		  });
		cur_frm.refresh_fields()
			
	  }
	  
	});
}

function get_country_offer_item(frm) {
	console.log("1")
	frappe.call({
	  "method": "barcode_updation.barcode_updation.doctype.item_tag_offer_print.item_tag_offer_print.search_country_offer_details",
	  "args": {
		"country": frm.doc.country,
		"item_group": frm.doc.item_group,
	   },
	  callback: function (r) {
		console.log(r)
		cur_frm.clear_table("item_tag_offer_details");
		r.message.forEach(fields => {
		  var child = cur_frm.add_child("item_tag_offer_details");
		  frappe.model.set_value(child.doctype, child.name, "item_code", fields.item_code)
		  frappe.model.set_value(child.doctype, child.name, "website_item_name", fields.website_item)
		  frappe.model.set_value(child.doctype, child.name, "description", fields.web_item_name)
		  frappe.model.set_value(child.doctype, child.name, "website_image", fields.website_image)
		  frappe.model.set_value(child.doctype, child.name, "price", fields.price_list_rate)
		  frappe.model.set_value(child.doctype, child.name, "before", fields.before)
		  frappe.model.set_value(child.doctype, child.name, "uom", fields.uom)
		  frappe.model.set_value(child.doctype, child.name, "country", fields.country)
		  });
		cur_frm.refresh_fields()
			
	  }
	  
	});
// cur_frm.fields_dict.my_field.$input.on("click", function(evt){

// })

}

function get_offer_item_det(frm) {
	console.log("1")
	frappe.call({
	  "method": "barcode_updation.barcode_updation.doctype.item_tag_offer_print.item_tag_offer_print.get_offer_item_details",
	  "args": {
		"item": frm.doc.item,
	   },
	  callback: function (r) {
		console.log(r)
		// cur_frm.clear_table("item_tag_details");
		r.message.forEach(fields => {
		  var child = cur_frm.add_child("item_tag_offer_details");
		  frappe.model.set_value(child.doctype, child.name, "item_code", fields.item_code)
		  frappe.model.set_value(child.doctype, child.name, "website_item_name", fields.website_item)
		  frappe.model.set_value(child.doctype, child.name, "description", fields.web_item_name)
		  frappe.model.set_value(child.doctype, child.name, "website_image", fields.website_image)
		  frappe.model.set_value(child.doctype, child.name, "price", fields.price_list_rate)
		  frappe.model.set_value(child.doctype, child.name, "before", fields.before)
		  frappe.model.set_value(child.doctype, child.name, "uom", fields.uom)
		  frappe.model.set_value(child.doctype, child.name, "country", fields.country)
		  });
		cur_frm.refresh_fields()
			
	  }
	  
	});
	// cur_frm.fields_dict.my_field.$input.on("click", function(evt){

	// })

}
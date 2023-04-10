// Copyright (c) 2023, venkatesh nayak and contributors
// For license information, please see license.txt

frappe.ui.form.on('Item Tag Print', {
	// refresh: function(frm) {

	// }
});
frappe.ui.form.on('Item Tag Print', {
	item_group : function(frm){
			get_website_item(frm);
	
		}
	
	})
	
		function get_website_item(frm) {
			console.log("1")
			frappe.call({
			  "method": "barcode_updation.barcode_updation.doctype.item_tag_print.item_tag_print.get_fields_details",
			  "args": {
				"item_group": frm.doc.item_group,
			   },
			  callback: function (r) {
				console.log(r)
				cur_frm.clear_table("item_tag_details");
				r.message.forEach(fields => {
				  var child = cur_frm.add_child("item_tag_details");
				  frappe.model.set_value(child.doctype, child.name, "item_code", fields.item_code)
				  frappe.model.set_value(child.doctype, child.name, "website_item_name", fields.website_item)
				  frappe.model.set_value(child.doctype, child.name, "description", fields.web_item_name)
				  frappe.model.set_value(child.doctype, child.name, "website_image", fields.website_image)
				 
				  });
				cur_frm.refresh_fields()
					
			  }
			  
			});
	// 	cur_frm.fields_dict.my_field.$input.on("click", function(evt){
	
	// 	})
	}
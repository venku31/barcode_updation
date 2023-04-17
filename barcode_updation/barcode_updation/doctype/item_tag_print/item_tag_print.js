// Copyright (c) 2023, venkatesh nayak and contributors
// For license information, please see license.txt

// frappe.ui.form.on('Item Tag Print', {
// 	// refresh: function(frm) {

// 	// }
// });
frappe.ui.form.on('Item Tag Print', {
	
	item_group : function(frm){
			get_website_item(frm);
			cur_frm.refresh_fields()
		},
	country : function(frm){
		get_country_item(frm);
		cur_frm.refresh_fields()
		},
	item : function(frm){
		get_item(frm);
			},
	refresh : function(frm){
			// get_country_item(frm);
			// get_website_item(frm);
			// cur_frm.save()
			},
	// validate : function(frm){
	// 	 get_country_item(frm);
	// 			}
	
	})
	
		function get_website_item(frm) {
			console.log("1")
			frappe.call({
			  "method": "barcode_updation.api.get_fields_details",
			  "args": {
				"item_group": frm.doc.item_group,
				"country": frm.doc.country,
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
				  frappe.model.set_value(child.doctype, child.name, "price", fields.price_list_rate)
				  frappe.model.set_value(child.doctype, child.name, "uom", fields.uom)
				  frappe.model.set_value(child.doctype, child.name, "country", fields.country)
				  });
				cur_frm.refresh_fields()
					
			  }
			  
			});
	// 	cur_frm.fields_dict.my_field.$input.on("click", function(evt){
	
	// 	})
	
	}
		
	function get_country_item(frm) {
		console.log("1")
		frappe.call({
		  "method": "barcode_updation.api.get_country_fields_details",
		  "args": {
			"country": frm.doc.country,
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
			  frappe.model.set_value(child.doctype, child.name, "price", fields.price_list_rate)
			  frappe.model.set_value(child.doctype, child.name, "uom", fields.uom)
			  frappe.model.set_value(child.doctype, child.name, "country", fields.country)
			  });
			cur_frm.refresh_fields()
				
		  }
		  
		});
// 	cur_frm.fields_dict.my_field.$input.on("click", function(evt){

// 	})

}
function get_item(frm) {
	console.log("1")
	frappe.call({
	  "method": "barcode_updation.api.get_item_details",
	  "args": {
		"item": frm.doc.item,
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
		  frappe.model.set_value(child.doctype, child.name, "price", fields.price_list_rate)
		  frappe.model.set_value(child.doctype, child.name, "uom", fields.uom)
		  frappe.model.set_value(child.doctype, child.name, "country", fields.country)
		  });
		cur_frm.refresh_fields()
			
	  }
	  
	});
// 	cur_frm.fields_dict.my_field.$input.on("click", function(evt){

// 	})

}
// 	function get_barcode(frm) {
// 		console.log("1")
// 		frappe.call({
// 		  "method": "barcode_updation.api.get_barcode",
// 		  "args": {
// 			"item": frm.doc.item_code,
// 		   },
// 		   callback(r) {
// 			if (r.message){
// 			   console.log(r.message)
// 			   // cur_frm.set_value("purchase_receipt", r.message);
		 
// 			}
// 			frappe.db.set_value("Website Item",cur_frm.doc.name,"barcode", r.message);
// 		 }
// 	  })  


// }
frappe.ui.form.on('Item Tag Print', {
refresh: function(frm) {
frm.add_custom_button(__("Print Tag"), function() {
            var w = window.open("/printview?doctype=Item%20Tag%20Print&name=" + cur_frm.doc.name + "&trigger_print=1&format=" + cur_frm.doc.print_format + "&no_letterhead=1&_lang=es");

            if(!w) {
                frappe.msgprint(__("Please enable pop-ups")); return;
            }
         }).css({'color':'white','font-weight': 'bold', 'background-color': 'blue'});
  
  },



})
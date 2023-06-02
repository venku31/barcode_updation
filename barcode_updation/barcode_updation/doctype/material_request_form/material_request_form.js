// Copyright (c) 2023, venkatesh nayak and contributors
// For license information, please see license.txt

frappe.ui.form.on('Material Request Form', {
	scan_barcode : function(frm, cdt, cdn){
	if (frm.doc.scan_barcode) {
		fetch_item_entry(frm, cdt, cdn);
		}
},
	validate : function(frm, cdt, cdn){
	// cur_frm.set_value("created_by", frappe.session.user);
	total_qty(frm, cdt, cdn);
	}
});
function fetch_item_entry(frm, cdt, cdn) {
	console.log("1")
	frappe.call({
	  "method": "barcode_updation.barcode_updation.doctype.material_request_form.material_request_form.search_item",
	  "args": {
		"item": frm.doc.scan_barcode,
		// "warehouse": frm.doc.set_warehouse,
	   },
	  callback: function (r) {
		console.log(r)
		// cur_frm.clear_table("details");
		r.message.forEach(stock => {
		  var child = cur_frm.add_child("items");
		  cur_frm.set_value("scan_barcode","")
		  frappe.model.set_value(child.doctype, child.name, "item_code", stock.item_code)
		  frappe.model.set_value(child.doctype, child.name, "item_group", stock.item_group)
		  frappe.model.set_value(child.doctype, child.name, "qty", 1)
		  frappe.model.set_value(child.doctype, child.name, "stock_uom", stock.stock_uom)
		  frappe.model.set_value(child.doctype, child.name, "uom", stock.stock_uom)
		  frappe.model.set_value(child.doctype, child.name, "item_name", stock.item_name)
		  frappe.model.set_value(child.doctype, child.name, "description", stock.description)
		  frappe.model.set_value(child.doctype, child.name, "brand", stock.brand)
		  });
	    cur_frm.refresh_fields()
			
	  }
	  
	});
	cur_frm.fields_dict.my_field.$input.on("click", function(evt){

	})
};

frappe.ui.form.on('Material Request Form Item', {
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
	
	////////////////////////////////////////////

	// frappe.provide("erpnext.accounts.dimensions");
	// {% include 'erpnext/public/js/controllers/buying.js' %};
	
	frappe.ui.form.on('Material Request Form', {
		setup: function(frm) {
			frm.custom_make_buttons = {
				'Stock Entry': 'Issue Material',
				'Purchase Order': 'Purchase Order',
				'Purchase Receipt': 'Purchase Receipt'
			};
	
			
		},
	
		set_from_warehouse: function(frm) {
			if (frm.doc.material_request_type == "Material Transfer"
				&& frm.doc.set_from_warehouse) {
				frm.doc.items.forEach(d => {
					frappe.model.set_value(d.doctype, d.name,
						"from_warehouse", frm.doc.set_from_warehouse);
				})
			}
		},
		refresh: function(frm) {
			frm.events.make_custom_buttons(frm);
		},
	
		make_custom_buttons: function(frm) {
				if (frm.doc.material_request_type === "Material Transfer") {
						add_create_pick_list_button();
						frm.add_custom_button(__("Material Transfer"),
							() => frm.events.make_stock_entry(frm), __('Create'));
	
						frm.add_custom_button(__("Material Transfer (In Transit)"),
							() => frm.events.make_in_transit_stock_entry(frm), __('Create'));
					}
	
					if (frm.doc.material_request_type === "Material Issue") {
						frm.add_custom_button(__("Issue Material"),
							() => frm.events.make_stock_entry(frm), __('Create'));
					}
	
					if (frm.doc.material_request_type === "Customer Provided") {
						frm.add_custom_button(__("Material Receipt"),
							() => frm.events.make_stock_entry(frm), __('Create'));
					}
	
					if (frm.doc.material_request_type === "Purchase") {
						frm.add_custom_button(__('Purchase Order'),
							() => frm.events.make_purchase_order(frm), __('Create'));
					}
	
					
	
					frm.page.set_inner_btn_group_as_primary(__('Create'));
	
					// stop
					frm.add_custom_button(__('Stop'),
						() => frm.events.update_status(frm, 'Stopped'));
	
				},
				make_purchase_order: function(frm) {
					frappe.prompt(
						{
							label: __('For Default Supplier (Optional)'),
							fieldname:'default_supplier',
							fieldtype: 'Link',
							options: 'Supplier',
							description: __('Select a Supplier from the Default Suppliers of the items below. On selection, a Purchase Order will be made against items belonging to the selected Supplier only.'),
							// get_query: () => {
							// 	return{
							// 		query: "erpnext.stock.doctype.material_request.material_request.get_default_supplier_query",
							// 		filters: {'doc': frm.doc.name}
							// 	}
							// }
						},
						(values) => {
							frappe.model.open_mapped_doc({
								method: "barcode_updation.barcode_updation.doctype.material_request_form.material_request_form.make_purchase_order",
								frm: frm,
								args: { default_supplier: values.default_supplier },
								run_link_triggers: true
							});
						},
						__('Enter Supplier'),
						__('Create')
					)
				},
			})
	
		
	
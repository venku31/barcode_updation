// Copyright (c) 2023, venkatesh nayak and contributors
// For license information, please see license.txt

frappe.ui.form.on('Barcode Updation', {
	setup: (frm) => {
		frm.set_query('item', () => {
			if (!(frm.doc.warehouse && frm.doc.date)) {
				frm.trigger('check_warehouse_and_date');
			}
		});
	},

	make_custom_stock_report_button: (frm) => {
		if (frm.doc.item) {
			frm.add_custom_button(__('Stock Balance Report'), () => {
				frappe.set_route('query-report', 'Stock Balance',
					{ 'item_code': frm.doc.item, 'warehouse': frm.doc.warehouse });
			});
		}
	},

	refresh: (frm) => {
		frm.disable_save();
		frm.trigger('make_custom_stock_report_button');
	},

	check_warehouse_and_date: (frm) => {
		frappe.msgprint(__('Please enter Warehouse and Date'));
		frm.doc.item = '';
		frm.refresh();
	},

	warehouse: (frm) => {
		if (frm.doc.item || frm.doc.item_barcode) {
			frm.trigger('get_stock_and_item_details');
		}
	},

	date: (frm) => {
		if (frm.doc.item || frm.doc.item_barcode) {
			frm.trigger('get_stock_and_item_details');
		}
	},

	item: (frm) => {
		frappe.flags.last_updated_element = 'item';
		frm.trigger('get_stock_and_item_details');
		frm.trigger('make_custom_stock_report_button');
	},

	item_barcode: (frm) => {
		frappe.flags.last_updated_element = 'item_barcode';
		frm.trigger('get_stock_and_item_details');
		frm.trigger('make_custom_stock_report_button');
	},

	get_stock_and_item_details: (frm) => {
		if (!(frm.doc.warehouse && frm.doc.date)) {
			frm.trigger('check_warehouse_and_date');
		}
		else if (frm.doc.item || frm.doc.item_barcode) {
			let filters = {
				warehouse: frm.doc.warehouse,
				date: frm.doc.date,
			};
			if (frappe.flags.last_updated_element === 'item') {
				filters = { ...filters, ...{ item: frm.doc.item }};
			}
			else {
				filters = { ...filters, ...{ barcode: frm.doc.item_barcode }};
			}
			frappe.call({
				method: 'erpnext.stock.doctype.quick_stock_balance.quick_stock_balance.get_stock_item_details',
				args: filters,
				callback: (r) => {
					if (r.message) {
						let fields = ['item', 'qty', 'image'];
						if (!r.message['barcodes'].includes(frm.doc.item_barcode)) {
							frm.doc.item_barcode = '';
							frm.refresh();
						}
						fields.forEach(function (field) {
							frm.set_value(field, r.message[field]);
						});
					}
				}
			});
		}
	},
	update: (frm) => {
		if (frm.doc.update_barcode){
			frappe.call({
				method: 'barcode_updation.barcode_updation.doctype.barcode_updation.barcode_updation.add_item_barcode',
				args: {
				   'item_code' : frm.doc.item,
				   'barcode' : frm.doc.update_barcode,
				   'posa_uom':frm.doc.barcode_uom,
				},
				callback(r) {
				   if (r.message){
					  console.log(r.message)
				
				   }
				}
			 })  
			}
		},
		update_image: (frm) => {
			if (frm.doc.item_image){
				frappe.call({
					method: 'barcode_updation.barcode_updation.doctype.barcode_updation.barcode_updation.add_item_image',
					args: {
					   'item_code' : frm.doc.item,
					   'image' : frm.doc.item_image,
					},
					callback(r) {
					   if (r.message){
						  console.log(r.message)
						  
					   }
					   cur_frm.clear_item_image();
					   cur_frm.refresh_fields();
					}
				 })  
				}
			}	
});
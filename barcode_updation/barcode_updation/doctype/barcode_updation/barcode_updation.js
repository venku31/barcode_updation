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
		onload(frm) {
		 frm.set_value("date", frappe.datetime.nowdate());   
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
			},
			update_price: (frm) => {
				if (frm.doc.price_update>0){
					frappe.call({
						method: 'barcode_updation.barcode_updation.doctype.barcode_updation.barcode_updation.update_price',
						args: {
						   'item' : frm.doc.item,
						   'price_list' : frm.doc.price_list,
						   'uom':frm.doc.barcode_uom,
						   'price_list_rate':frm.doc.price_update,
						   'price':frm.doc.price_list_rate,
						},
						callback(r) {
						   if (r.message){
							  console.log(r.message)
						
						   }
						}
					 })  
					}
				},
			
});

frappe.ui.form.on('Barcode Updation', {
	item(frm) {
	get_barcode(frm);
	get_item_price(frm);
	cur_frm.refresh()
	},
	price_list(frm) {
	get_price(frm) ;
	}
	// barcode_uom(frm) {
	// get_price(frm) ;
	//}
})
function get_barcode(frm) {
	console.log("1")
	frappe.call({
	  "method": "barcode_updation.api.get_barcode",
	  "args": {
		"item": frm.doc.item,
	   },
	   callback(r) {
		if (r.message){
		   console.log(r.message)
		   // cur_frm.set_value("purchase_receipt", r.message);
		var barcode = r.message[0].barcode
		}
		cur_frm.set_value("item_barcode", barcode);
		// frappe.db.set_value("Website Item",cur_frm.doc.name,"barcode", barcode);
		cur_frm.refresh_fields()
	 }
	 
  })  
}
function get_item_price(frm) {
	console.log("1")
	frappe.call({
	  "method": "barcode_updation.barcode_updation.doctype.barcode_updation.barcode_updation.get_item_price",
	  "args": {
		"item": frm.doc.item,
		 },
	   callback(r) {
		if (r.message){
		   console.log(r.message)
		   // cur_frm.set_value("purchase_receipt", r.message);
		var price = r.message[0].price_list_rate
		var price_list = r.message[0].price_list
		cur_frm.set_value("price_list_rate", price);
		cur_frm.set_value("price_list", price_list);
		}
		else {
			cur_frm.set_value("price_list_rate", 0);
		}
		cur_frm.refresh_fields()
	 }
	 
  })  
}

  function get_price(frm) {
	console.log("1")
	frappe.call({
	  "method": "barcode_updation.barcode_updation.doctype.barcode_updation.barcode_updation.get_price",
	  "args": {
		"item": frm.doc.item,
		"uom": frm.doc.barcode_uom,
		"price_list": frm.doc.price_list,
		 },
	   callback(r) {
		cur_frm.set_value("price_list_rate", 0);
		if (r.message){
		   console.log(r.message)
		   // cur_frm.set_value("purchase_receipt", r.message);
		var price = r.message[0].price_list_rate 
		cur_frm.set_value("price_list_rate", price);
		}
		
		else {
			cur_frm.set_value("price_list_rate", 0);
		}
		cur_frm.refresh_fields()
	 }
	 
  })  




}
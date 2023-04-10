frappe.ui.form.on('Website Item', {
    // onload(frm) {
    //     get_barcode(frm);
    //     cur_frm.refresh()
    //     },
	after_save(frm) {
	get_barcode(frm);
	cur_frm.refresh()
	}
})

function get_barcode(frm) {
		console.log("1")
		frappe.call({
		  "method": "barcode_updation.api.get_barcode",
		  "args": {
			"item": frm.doc.item_code,
		   },
		   callback(r) {
			if (r.message){
			   console.log(r.message)
			   // cur_frm.set_value("purchase_receipt", r.message);
		    var barcode = r.message[0].barcode
			}
            cur_frm.set_value("barcode", barcode);
			frappe.db.set_value("Website Item",cur_frm.doc.name,"barcode", barcode);
			cur_frm.refresh_fields()
		 }
		 
	  })  


}
// Copyright (c) 2023, venkatesh nayak and contributors
// For license information, please see license.txt

frappe.ui.form.on('Barcode Label Print', {
	refresh: function(frm) {
// //   frm.disable_save();
// //   cur_frm.page.clear_actions_menu()
//   frm.add_custom_button(__("Print"),function(frm, cdt, cdn) {
//    var me = this;
//    var doc = frm.doc
//    var print_format = "DefaultBarcodeLabel"; // print format name
   
//    var w = window.open(frappe.urllib.get_full_url("/printview?"
//       +"doctype="+encodeURIComponent(cdt)
//       +"&name="+encodeURIComponent(cdn)
//       +"&trigger_print=1"
//       +"&format=" + print_format
//       +"&no_letterhead=0"
//       ));
   
//       // if(!w) {
//       //    msgprint(__("Please enable pop-ups for printing.")); return;
//       // }
	
// 	}).css({'color':'white','font-weight': 'bold', 'background-color': 'blue'});


frm.add_custom_button(__("Print"), function() {
            var w = window.open("/printview?doctype=Barcode%20Label%20Print&name=" + cur_frm.doc.name + "&trigger_print=1&format=DefaultBarcodeLabel&no_letterhead=1&_lang=es");

            if(!w) {
                frappe.msgprint(__("Please enable pop-ups")); return;
            }
                }).css({'color':'white','font-weight': 'bold', 'background-color': 'blue'});
  
  },



})

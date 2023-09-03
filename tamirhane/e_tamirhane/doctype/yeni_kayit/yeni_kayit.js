// // Copyright (c) 2023, Ali Arslan and contributors
// // For license information, please see license.txt

// frappe.ui.form.on('Yeni Kayit', {
//     on_submit: function(frm) {
//         let doc_name = frm.doc.name;

//         frappe.call({
//             method: "tamirhane.e_tamirhane.ocr.create_new_bekleyen_arac",
//             args: {
//                 "doc": doc_name
//             },
//             callback: function(response) {
//                 if(response.message) {
//                     let yeni_form_adi = response.message;
//                     window.location.href = `/desk#Form/Bekleyen Araclar/${yeni_form_adi}`;
//                 }
//             }
//         });
//     },

//     on_change: function(frm) {
//         let doc_name = frm.doc.name;

//         if (frm.doc.ekle) {
//             frappe.call({
//                 method: "tamirhane.e_tamirhane.ocr.handle_image_upload",
//                 args: {
//                     "doc": doc_name
//                 },
//                 callback: function(response) {
//                     if(response.message) {
//                         // Burada dönen cevaba göre yapılacak işlemler varsa eklenebilir.
//                     }
//                 }
//             });
//         }
//     }
// });

// Copyright (c) 2023, Ali Arslan and contributors
// For license information, please see license.txt

frappe.ui.form.on('Tamamlanan araclar', {
    refresh: function(frm) {
        frm.add_custom_button(__('Fatura Yaz'), function() {
            // Prepare items for Sales Invoice based on Muayene Tablosu
            var items = [];
            for (var i in frm.doc.items) {
                var item = frm.doc.items[i];
                items.push({
                    'item_code': item.parca,
                    'item_name': item.p_adı,
                    'qty': 1,
                    'rate': item.fiyat,
                });
            }

            frappe.call({
                method: 'tamirhane.e_tamirhane.ocr.my_method',
                args: {
                    customer: frm.doc.customer,
                    items: items,
                    doc: frm.doc.name
                
                },
                callback: function(response) {
                    var doc = response.message;
                    if (doc) {
                        frappe.set_route('Form', 'Sales Invoice', doc);

                        // Reload the document to refresh all linked fields
                        frappe.model.with_doc('Sales Invoice', doc.name, function() {
                            var si_doc = frappe.model.get_doc('Sales Invoice', doc.name);
                            si_doc.items = [];  // Clear the existing items

                            // Add the new items
                            for (var i in items) {
                                var item = items[i];
                                var child = frappe.model.add_child(si_doc, 'Sales Invoice Item', 'items');
                                child.item_code = item.item_code;
                                child.item_name = item.item_name;
                                child.qty = item.qty;
                                child.rate = item.rate;
                            }

                            // Save and refresh the document
                            frm.save();
                        });
                    }
                }
            });
        });
    }
});

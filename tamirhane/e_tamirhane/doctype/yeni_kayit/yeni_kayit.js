// Copyright (c) 2023, Ali Arslan and contributors
// For license information, please see license.txt

frappe.ui.form.on('Yeni Kayit', {
	after_submit: function(frm) {
		frappe.set_route('Form', 'Bekleyen Araclar', frm.name);
	}
});

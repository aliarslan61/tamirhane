// frappe.ui.form.on('Yeni Kayit', {
//   after_save: function(frm) {
//     frm.reload_doc();
//   }
// });



frappe.ui.form.on('Yeni Kayit', {
  refresh: function(frm) {
      frm.add_custom_button(__('Scrap Data'), function() {
          frappe.call({
              method: 'tamirhane.e_tamirhane.testscrapping.scrap',
              args: {
                  // You can pass any necessary arguments here
              },
              callback: function(response) {
                  // Log the response to the browser console
                  console.log("Response from server:", response.message);
              }
          });
      });
  }
});

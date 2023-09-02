// Copyright (c) 2023, Ali Arslan and contributors
// For license information, please see license.txt

frappe.ui.form.on('Bekleyen Araclar', {
    refresh: function(frm) {
        frm.add_custom_button('Sigorta Şirketleri', function() {
            // creating a dialog
            const dialog = new frappe.ui.Dialog({
                title: 'Hasar Dosyası Sorgula',
                fields: [
                    {'fieldname': 'company', 'fieldtype': 'Select', 'options': ['Anadolu Sigorta', 'Türkiye Sigorta', 'Ankara Sigorta',
                    'Allianz Sigorta', 'Sompo Sigorta', 'Doğa Sigorta', 'HDI Sigorta', 
                    'AK Sigorta', 'Ray Sigorta', 'Unico Sigorta', 'Mapfre Sigorta', 'Zürich Sigorta'], 'label': 'Sigorta Şirketleri', 'reqd': 1}
                ],
                primary_action_label: 'Adrese git',
                primary_action(values) {
                    if(values.company === 'Türkiye Sigorta'){
                        window.open('https://www.anadolusigorta.com.tr/hasar-merkezi?gclid=Cj0KCQjw4s-kBhDqARIsAN-ipH1XCPJFCZrf9qO2XDbT-ubwU2OVeVbSfe1yDV0N5Qb9tdsdxyCt96YaAr6qEALw_wcB', '_blank');
                    } else if (values.company === 'anadolu sigorta') {
                        window.open('https://www.turkiyesigorta.com.tr/online-islemler/musteriler/sorgulama', '_blank');
                    } else if (values.company === 'Ankara Sigorta') {
                        window.open('https://www.ankarasigorta.com.tr/online-islemler/hasar-dosya-sorgulama', '_blank');
                    } else if (values.company === 'Allianz Sigorta') {
                        window.open('https://hasar.allianz.com.tr/disclosureClaimWeb/main-template/login-screen', '_blank');
                    } else if (values.company === 'Sompo Sigorta') {
                        window.open('https://www.somposigorta.com.tr/hasariniz-ne-durumda', '_blank');
                    } else if (values.company === 'Doğa Sigorta') {
                        window.open('https://portal.dogasigorta.com/sube.aspx#HasarArama', '_blank');
                    } else if (values.company === 'HDI Sigorta') {
                        window.open('https://web.hdisigorta.com.tr/hasar-sorgulama-3.php', '_blank');
                    } else if (values.company === 'AK Sigorta') {
                        window.open('https://www.aksigorta.com.tr/hasar-dosya-sorgula-2', '_blank');
                    } else if (values.company === 'Ray Sigorta') {
                        window.open('https://www.raysigorta.com.tr/musteri-islemleri/dosya-sorgulama', '_blank');
                    } else if (values.company === 'Unico Sigorta') {
                        window.open('https://www.unicosigorta.com.tr/online-islemler', '_blank');
                    } else if (values.company === 'Mapfre Sigorta') {
                        window.open('https://hasar.mapfre.com.tr/mcn/#/hosgeldiniz', '_blank');
                    } else if (values.company === 'Zürich Sigorta') {
                        window.open('https://www.zurichsigorta.com.tr/hasar-sorgulama', '_blank');
                    }
                    dialog.hide();
                }
            });

            dialog.show();
        });
    }
});
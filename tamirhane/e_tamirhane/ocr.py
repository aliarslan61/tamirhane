import base64
import requests
import json
import frappe
from frappe import _
from urllib.parse import quote
from frappe.utils.file_manager import get_file
from PIL import Image
import io
import datetime

def convert_image_to_binary(doc_name):
    
    doc = frappe.get_doc('Yeni Kayit', doc_name)
    file_data = get_file(doc.ekle)
    image = Image.open(io.BytesIO(file_data[1])) 
    reduced_quality_buffer = io.BytesIO()
    image.save(reduced_quality_buffer, format="JPEG", quality=40, optimize=False)
    reduced_quality_buffer.seek(0)
    binary_data = reduced_quality_buffer.read()
    base64_encoded_data = base64.b64encode(binary_data).decode()
    
    return base64_encoded_data




def send_binary_data_via_api(api_url, file_name, binary_data):
    headers = {
        'Content-Type': 'application/json',
    }

    payload = {
        "name": file_name,
        "binary": binary_data
    }

    response = requests.post(api_url, headers=headers, data=json.dumps(payload))

    if response.status_code != 200:
        frappe.throw(_('Failed to send data to API.'))

    return response.json()  

def parse_fields_from_response(data, doc_name):
    if not isinstance(data, dict):
        frappe.throw(_("The response data should be a dictionary."))

    # doc = frappe.get_cached_doc("Yeni Kayit", doc_name)
    frappe.db.set_value("Yeni Kayit", doc_name, "sase_no", data.get("vin"))    
    frappe.db.set_value("Yeni Kayit", doc_name, "plaka", data.get("plate"))    
    frappe.db.set_value("Yeni Kayit", doc_name, "motor_no", data.get("ein"))    
    frappe.db.set_value("Yeni Kayit", doc_name, "renk", data.get("color"))    
    frappe.db.set_value("Yeni Kayit", doc_name, "model", data.get("manufacturer"))    
    frappe.db.set_value("Yeni Kayit", doc_name, "bolge", data.get("region"))    
    frappe.db.set_value("Yeni Kayit", doc_name, "fuel", data.get("fuel"))    
    frappe.db.commit()


def create_new_bekleyen_arac(doc, method, force=1):
    if doc.sase_no and doc.plaka and doc.motor_no and doc.docstatus == 1:
            
        new_bekleyen_arac = frappe.get_doc(
                {
                        "doctype": "Bekleyen Araclar",
                        "sase_no":doc.sase_no,
                        "tamirci_adi":frappe.session.user,
                        "plaka": doc.plaka,
                        "motor_no": doc.motor_no,
                        "renk":doc.renk,
                        "model":doc.model,
                        "bolge":doc.bolge,
                        "brand":doc.brand,
                        "fuel":doc.fuel,
                        "ekle":doc.ekle,
                        "cusotmer":doc.customer,
                        "start_date":frappe.utils.now_datetime()
                }
            )
        new_bekleyen_arac.save(ignore_permissions=True)
        frappe.db.commit()
    
        frappe.db.set_value("Yeni Kayit", doc.name, "docstatus", 2)
        frappe.delete_doc("Bekleyen Araclar", doc.name)
        frappe.db.commit()
    else:
        frappe.throw("Lütfen Şase No, Plaka ve Motor No giriniz")
    return 

def create_new_biten_arac(doc, arg):
    if doc.status == "Tamir edildi":
        new_biten_arac_doc = frappe.get_doc(
            {
                "doctype": "Tamamlanan araclar",
                "ticari_adi":doc.ticari_adı,
                "customer": doc.customer,
                "sase_no": doc.sase_no,
                "plaka": doc.plaka,
                "motor_no": doc.motor_no,
                "renk": doc.renk,
                "model": doc.model,
                "brand":doc.brand,
                "km": doc.km,
                "bolge": doc.bolge,
                "fuel": doc.fuel,
                "ekle": doc.ekle,
                "sigorta": doc.sigorta,
                "sigorta_acentesi":doc.sigorta_acentesi,
                "police_no":doc.police_no,
                "dosya_no":doc.dosya_no,
                "eksper":doc.eksper,

                
                "items": [
                    {
                        "parca": child.parca,
                        "p_adı": child.p_adı,
                        "durum": child.durum,
                        "fiyat": child.fiyat,
                        "iscilik":child.iscilik
                    } for child in doc.items
                ],
                
            }
        )
                
        test = 1
        new_biten_arac_doc.save(ignore_permissions=True)
        frappe.db.commit()
        frappe.delete_doc("Bekleyen Araclar", doc.name)
        frappe.db.commit()
  
    return

          
     

def handle_image_upload(doc, method):
    if not doc.sase_no:
        
        binary_data = convert_image_to_binary(doc.name)
        api_url = "https://ocr.syncmaze.com/api/OCR/VLicense"
        file_name = doc.ekle.split('/')[-1]
        response = send_binary_data_via_api(api_url, file_name, binary_data)
        result = parse_fields_from_response(response, doc.name)
        delete_doc=create_new_bekleyen_arac(doc,method)



import json

@frappe.whitelist()
def my_method(doc, customer, items):
    items = json.loads(items)
    cur_doc = frappe.get_doc("Tamamlanan araclar", doc)

    new_invoice_items = []
    for item in items:
        new_invoice_items.append({
            "item_code": item['item_code'],
            "item_name": item['item_name'],
            "qty": item['qty'],
            "rate": item['rate'],
            "iscilik":item['iscilik']
        })

    new_invoice = frappe.get_doc({
        'doctype': 'Sales Invoice',
        'customer': customer,
        "items": new_invoice_items
    })

    new_invoice.insert()
    return new_invoice.name  




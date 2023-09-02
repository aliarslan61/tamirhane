import requests
import json
import frappe

@frappe.whitelist()
def pipedrive_integration(doc, arg=None):
    api_token = "f9bc0dc47b894787ecd280b8e5378e348494878d"
    headers = {
        "Content-Type": "application/json", 
        "Accept": "application/json"
        }
    
    


    # Organization
    org_data = {
    'name': doc.company_name,
    'visible_to': 7
    }
    response = requests.post('https://api.pipedrive.com/v1/organizations?api_token=' + api_token, headers=headers, data=json.dumps(org_data))
    if response.json()['success'] == False:
          frappe.get_doc({
            "doctype": "PipeDrive Error Log",
            "webhook": "webhook",
            "reference_document": doc.name,
            "url": f"https://api.pipedrive.com/v1/organizations?api_token={api_token}",
            "header": frappe.as_json(headers) if headers else None,
            "response": response,
            "request":doc.name,
            "error": frappe.get_traceback() if response and not response.ok else None,
        }).insert(ignore_permissions=True)
          return
    org_id = response.json()['data']['id']
    # frappe.db.set_value('Lead', doc.name, 'pipedrive_org_id', org_id)

    #  Person
    person_data = {
        'name': doc.lead_name,
        'org_id': org_id,
        'email': doc.email_id,
        'phone': doc.mobile_no,
        'postal_address': doc.adress
    }
    response = requests.post('https://api.pipedrive.com/v1/persons?api_token=' + api_token, headers=headers, data=json.dumps(person_data))
    if response.json()['success'] == False:
          frappe.get_doc({
            "doctype": "PipeDrive Error Log",
            "webhook": "webhook",
            "reference_document": doc.name,
            "url": f"https://api.pipedrive.com/v1/organizations?api_token={api_token}",
            "header": frappe.as_json(headers) if headers else None,
            "response": response,
            "error": frappe.get_traceback() if response and not response.ok else None,
        }).insert(ignore_permissions=True)
          return
    person_id = response.json()['data']['id']

    checked_boxes = []
    if doc.inverter_request == 1:
        checked_boxes.append("32")
    if doc.solarpanel_request == 1:
        checked_boxes.append("33")
    if doc.offer_request == 1:
        checked_boxes.append("34")
    # if doc.callback_request == 1:
    #     checked_boxes.append("35")
    if doc.complete_set_request == 1:
        checked_boxes.append("36")
    if doc.dealer_request == 1:
        checked_boxes.append("37")
    if doc.heat_pump_request == 1:
        checked_boxes.append("745")
    if doc.lithium_battery_request == 1:
        checked_boxes.append("747")

    b0c0941380fc5ee8501d6c4a8681a4dcf9942224_value = ",".join(checked_boxes)
    
    country = 0
    if doc.state == "Österreich":
        country = 658
    if doc.state == "Deutschland":
        country = 557
    if doc.state == "Schweiz":
        country = 679

    lead_data = {
        'title': doc.lead_name + ' Lead',
        'person_id': person_id,
        "8d98a94c0fdc402aed7a9adbd0ac448d2c03bb18": 746,
        "b0c0941380fc5ee8501d6c4a8681a4dcf9942224": b0c0941380fc5ee8501d6c4a8681a4dcf9942224_value,
        "e30181b8b620ee27cd51aa01cda8a4b98af6f12c": 54,
        "0f203d306141131d11d0f24a145a59273a608212": country,
        "organization_id": org_id,
    }


    response = requests.post('https://api.pipedrive.com/v1/leads?api_token=' + api_token, headers=headers, data=json.dumps(lead_data))
    if response.json()['success'] == False:
          frappe.get_doc({
            "doctype": "PipeDrive Error Log",
            "webhook": "webhook",
            "reference_document": doc.name,
            "url": f"https://api.pipedrive.com/v1/organizations?api_token={api_token}",
            "header": frappe.as_json(headers) if headers else None,
            "request": frappe.as_json(lead_data),                
            "response": response,
            "error": frappe.get_traceback() if response and not response.ok else None,
        }).insert(ignore_permissions=True)
          return
    lead_id = response.json()['data']['id']
    
    
    note_data ={
        "content": doc.interview_notes,
        "lead_id": lead_id,
        "person_id": person_id,
        "org_id": org_id,
        "user_id": 14507478,
        "title":"message"
        }
    response = requests.post('https://api.pipedrive.com/v1/notes?api_token=' + api_token, headers=headers, data=json.dumps(note_data))

    note2_data ={
        "lead_id": lead_id,
        "person_id": person_id,
        "org_id": org_id,
        "user_id": 14507478,
        "content":"Orginal beleg ist unter https://tommatech.frappe.cloud/app/lead in ERPNext zu finden. Bitte Überprüfe ob unter Activities ein Email vom Kunden eingegangen ist."
        }
    response = requests.post('https://api.pipedrive.com/v1/notes?api_token=' + api_token, headers=headers, data=json.dumps(note2_data))
    # frappe.db.set_value('Lead', doc.name, 'pipedrive_lead_id', lead_id)
    
    

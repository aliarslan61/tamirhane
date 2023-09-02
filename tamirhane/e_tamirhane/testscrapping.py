import PyPDF2
import frappe
import requests
from io import BytesIO
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import time

@frappe.whitelist()
def scrap():
    pdf_url = 'http://10.0.0.32:8003/files/cv.pdf'

    # Download the PDF from the URL
    response = requests.get(pdf_url)
    pdf_file = BytesIO(response.content)

    # Read the PDF content
    reader = PyPDF2.PdfFileReader(pdf_file)
    text = ''
    for page_num in range(reader.numPages):
        text += reader.getPage(page_num).extractText()
    
    print(text)
    return text  # Optionally return the text


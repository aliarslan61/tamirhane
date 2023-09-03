from . import __version__ as app_version

app_name = "tamirhane"
app_title = "E-Tamirhane"
app_publisher = "Ali Arslan"
app_description = "Tamirhane Yönetim Merkezi"
app_email = "arslan.ahmet93@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/tamirhane/css/tamirhane.css"
# app_include_js = "/assets/tamirhane/js/tamirhane.js"

# include js, css files in header of web template
# web_include_css = "/assets/tamirhane/css/tamirhane.css"
# web_include_js = "/assets/tamirhane/js/tamirhane.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "tamirhane/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"UOM" : "public/js/cusotm.js"}

# include js in doctype views
doctype_js = {"Yeni Kayit" : "public/js/custom.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "tamirhane.utils.jinja_methods",
#	"filters": "tamirhane.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "tamirhane.install.before_install"
# after_install = "tamirhane.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "tamirhane.uninstall.before_uninstall"
# after_uninstall = "tamirhane.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "tamirhane.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	# "Yeni Kayit": {
	# 	"on_change": "tamirhane.e_tamirhane.ocr.handle_image_upload",
    #     "on_submit": "tamirhane.e_tamirhane.ocr.create_new_bekleyen_arac"
	# },
 	#"Bekleyen Araclar": {
	#	"on_update": "tamirhane.e_tamirhane.ocr.create_new_biten_arac"
	#},
    # "Lead": {
    #     "on_change": "tamirhane.e_tamirhane.pipedrive.pipedrive_integration",
    # }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"tamirhane.tasks.all"
#	],
#	"daily": [
#		"tamirhane.tasks.daily"
#	],
#	"hourly": [
#		"tamirhane.tasks.hourly"
#	],
#	"weekly": [
#		"tamirhane.tasks.weekly"
#	],
#	"monthly": [
#		"tamirhane.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "tamirhane.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "tamirhane.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "tamirhane.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["tamirhane.utils.before_request"]
# after_request = ["tamirhane.utils.after_request"]

# Job Events
# ----------
# before_job = ["tamirhane.utils.before_job"]
# after_job = ["tamirhane.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"tamirhane.auth.validate"
# ]

import frappe


def execute():
	# Custom Field validation doesn't allow Data -> Autocomplete, but both are varchar(140) columns, so
	# switch the existing fields in place; after_migrate's create_custom_fields then finds them converted.
	for doctype in ("Quotation", "Sales Order", "Sales Invoice"):
		custom_field = frappe.db.get_value(
			"Custom Field", {"dt": doctype, "fieldname": "cc_attention_to", "fieldtype": "Data"}
		)
		if custom_field:
			frappe.db.set_value("Custom Field", custom_field, "fieldtype", "Autocomplete")
			frappe.clear_cache(doctype=doctype)

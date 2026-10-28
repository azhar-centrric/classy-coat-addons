def get_sales_order_fields():
	return {
		"Sales Order": [
			{
				"fieldname": "cc_attention_to",
				"label": "Attention To",
				"fieldtype": "Autocomplete",
				# Suggests Mr./Ms. on click (see public/js/attention_to_salutation.js for
				# ignore_validation), but the field still accepts any typed name after that.
				"options": "Mr.\nMs.",
				# Same fieldname as Quotation's cc_attention_to: Frappe's get_mapped_doc (used by
				# "Make Sales Order") copies any field present on both source and target with a
				# matching fieldname, so this carries the value across automatically - no mapping
				# code needed.
				"insert_after": "cen_payment_terms",
			},
		]
	}

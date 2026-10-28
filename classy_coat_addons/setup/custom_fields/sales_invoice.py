def get_sales_invoice_fields():
	return {
		"Sales Invoice": [
			{
				"fieldname": "cc_attention_to",
				"label": "Attention To",
				"fieldtype": "Autocomplete",
				# Suggests Mr./Ms. on click (see public/js/attention_to_salutation.js for
				# ignore_validation), but the field still accepts any typed name after that.
				"options": "Mr.\nMs.",
				# Same fieldname as Quotation/Sales Order's cc_attention_to, so it carries across
				# "Make Sales Order" and "Make Sales Invoice" automatically (see sales_order.py).
				"insert_after": "cen_payment_terms",
			},
		]
	}

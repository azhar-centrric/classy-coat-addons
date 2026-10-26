import frappe


def execute():
	# "Amount In Words" was printing the currency as "AED", the client wants "UAE Dirham". That
	# word comes from frappe.utils.money_in_words(), which runs it through _(main_currency,
	# context="Currency") - so a Translation override is the fix, not a print format change.
	if not frappe.db.exists(
		"Translation", {"language": "en", "source_text": "AED", "context": "Currency"}
	):
		frappe.get_doc(
			{
				"doctype": "Translation",
				"language": "en",
				"source_text": "AED",
				"context": "Currency",
				"translated_text": "UAE Dirham",
			}
		).insert(ignore_permissions=True)

	# in_words/base_in_words are computed and stored at save time, so existing documents keep
	# showing "AED ..." until re-saved - update their stored text directly instead.
	for doctype in ("Quotation", "Sales Order", "Sales Invoice"):
		for field in ("in_words", "base_in_words"):
			frappe.db.sql(
				f"""update `tab{doctype}`
				set {field} = concat('UAE Dirham', substring({field}, 4))
				where {field} like 'AED%%'"""
			)

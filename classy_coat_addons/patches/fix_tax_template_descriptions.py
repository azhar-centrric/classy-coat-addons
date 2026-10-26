import re

import frappe


def execute():
	# The tax templates were set up with the rate written twice, e.g. "VAT 5% @ 5.0" instead of
	# just "VAT 5%" - fixes the templates themselves (so new documents come out right) and every
	# existing document's own copy of that text (tax rows are copied at the time the tax is
	# applied, so fixing the template alone doesn't touch documents that already have it).
	rows = frappe.db.sql(
		"""select name, description from `tabSales Taxes and Charges`
		where description like '%% @ %%'""",
		as_dict=True,
	)
	for row in rows:
		new_description = re.sub(r"\s*@\s*[\d.]+\s*$", "", row.description)
		if new_description != row.description:
			frappe.db.set_value(
				"Sales Taxes and Charges", row.name, "description", new_description, update_modified=False
			)

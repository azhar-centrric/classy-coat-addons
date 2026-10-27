import re
from typing import Literal

import frappe
from frappe.model.document import Document
from frappe.utils.print_format import download_pdf as original_download_pdf

# Doctypes whose downloaded PDF filename should include the customer name, not just the
# document's own ID. Both have a customer_name field already fetched onto the document.
DOCTYPES_WITH_CUSTOMER_IN_FILENAME = ("Quotation", "Sales Invoice")


def sanitize_for_filename(value: str) -> str:
	# Same characters the original download_pdf strips from the document name, plus the other
	# ones Windows/most filesystems disallow in a filename.
	return re.sub(r'[\\/:*?"<>|]', "-", value).strip()


@frappe.whitelist()
def download_pdf(
	doctype: str,
	name: str,
	format: str | None = None,
	doc: Document | None = None,
	no_letterhead: bool | int = 0,
	language: str | None = None,
	letterhead: str | None = None,
	pdf_generator: Literal["wkhtmltopdf", "chrome"] | None = None,
):
	original_download_pdf(
		doctype,
		name,
		format=format,
		doc=doc,
		no_letterhead=no_letterhead,
		language=language,
		letterhead=letterhead,
		pdf_generator=pdf_generator,
	)

	if doctype not in DOCTYPES_WITH_CUSTOMER_IN_FILENAME:
		return

	customer_name = doc.get("customer_name") if doc else frappe.db.get_value(doctype, name, "customer_name")
	if not customer_name:
		return

	frappe.local.response.filename = "{name} - {customer}.pdf".format(
		name=sanitize_for_filename(name), customer=sanitize_for_filename(customer_name)
	)

// cc_attention_to is an Autocomplete suggesting Mr./Ms. on click, while still accepting a typed
// name after that (ignore_validation skips Autocomplete's default "must match a suggestion" check).
//
// set_df_property writes to frappe.meta's per-docname docfield copy (keyed by frm.docname), not a
// single shared df. "setup" only fires once per form controller, for whichever docname happened to
// be active the first time this doctype's form was built - every document opened afterwards (a new
// quotation, a duplicate) gets its own fresh copy without ignore_validation, so Autocomplete's
// validate() silently blanked out any typed value that wasn't literally "Mr." or "Ms.". Using
// "refresh" instead re-applies it for every document, every time.
["Quotation", "Sales Order", "Sales Invoice"].forEach((doctype) => {
	frappe.ui.form.on(doctype, {
		refresh: function (frm) {
			frm.set_df_property("cc_attention_to", "ignore_validation", 1);
		},
	});
});

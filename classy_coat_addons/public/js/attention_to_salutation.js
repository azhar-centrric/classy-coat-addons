// cc_attention_to is an Autocomplete suggesting Mr./Ms. on click, while still accepting a typed
// name after that (ignore_validation skips Autocomplete's default "must match a suggestion" check).
["Quotation", "Sales Order", "Sales Invoice"].forEach((doctype) => {
	frappe.ui.form.on(doctype, {
		setup: function (frm) {
			frm.set_df_property("cc_attention_to", "ignore_validation", 1);
		},
	});
});

// Frappe's list view always appends the literal "ID" (fieldname "name") column at the very end
// whenever a doctype has a title_field set (Quotation and Sales Invoice both use customer_name),
// and the column-picker UI has no way to override that - reorder_listview_fields() only
// reorders/filters the fields *between* the fixed-first Subject column and that appended ID
// column. This patches ListView.setup_columns to move ID to position 1 (right after Customer
// Name) for just these two doctypes, since the client explicitly asked for that exact order.
(function () {
	if (frappe.views.ListView.prototype.__cc_id_column_patched) return;
	frappe.views.ListView.prototype.__cc_id_column_patched = true;

	const DOCTYPES_WITH_ID_SECOND = ["Quotation", "Sales Invoice"];
	const original_setup_columns = frappe.views.ListView.prototype.setup_columns;

	frappe.views.ListView.prototype.setup_columns = function () {
		original_setup_columns.call(this);

		if (!DOCTYPES_WITH_ID_SECOND.includes(this.doctype)) return;

		const id_index = this.columns.findIndex(
			(col) => col.type === "Field" && col.df && col.df.fieldname === "name"
		);
		if (id_index > 1) {
			const [id_column] = this.columns.splice(id_index, 1);
			this.columns.splice(1, 0, id_column);
		}
	};
})();

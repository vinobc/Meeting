import frappe
from frappe import _

@frappe.whitelist()
def send_meeting_invitation_emails(meeting):
	meeting = frappe.get_doc("Meeting", meeting)
	meeting.check_permission("email")


	if meeting.status == "Planned":
		frappe.sendmail(
			recipients=[d.attendee for d in meeting.meeting_attendees],
			sender=frappe.session.user, 
			subject=meeting.title, 
			message=meeting.message, 
			reference_doctype=meeting.doctype,
			reference_name=meeting.name
		) 

		meeting.status = "Invite Sent"
		meeting.save()

		frappe.msgprint(_("Invite Sent"))

	else:
		frappe.msgprint(_("Meeting Status must be 'Planned'"))

@frappe.whitelist()
def get_meetings(start, end):
	if not frappe.has_permission("Meeting", "read"):
		raise frappe.PermissionError

	return frappe.db.sql("""select 
		timestamp(`date`, from_time) as start,
		timestamp(`date`, to_time) as end,
		name,
		title,
		status,
		0 as all_day
	from `tabMeeting`
	where `date` between %(start)s and %(end)s""", {
		"start": start,
		"end": end
	}, as_dict=True) 

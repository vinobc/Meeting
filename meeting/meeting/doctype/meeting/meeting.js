frappe.ui.form.on("Meeting", {
  send_meeting_invites: function(frm) {
        if (frm.doc.status === "Planned") {
          frappe.call({
            method: "meeting.api.send_meeting_invitation_emails",
            args: {
              meeting: frm.doc.name
            },
            callback: function(r) {

            }
          });
        }
    },
})

frappe.ui.form.on("Meeting Attendees", {
  attendee: function(frm, cdt, cdn) {
          var attendee = frappe.model.get_doc(cdt, cdn);
          if (attendee.attendee) {
             frappe.call({
                method: "meeting.meeting.doctype.meeting.meeting.get_attendee_name",
                args: {
                     attendee: attendee.attendee
                },
                callback: function(r) {
                        frappe.model.set_value(cdt, cdn, "full_name", r.message);
                } 
              });
          } else {
              frappe.model.set_value(cdt, cdn, "full_name", null);
        }
    },
  });

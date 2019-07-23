# -*- coding: utf-8 -*-
# Copyright (c) 2018, R Vinob Chander and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class Meeting(Document):
    def validate(self):
        """Set missing names"""
        found_attendee = []
        found_chair = []
        found_coordinator = []
        found_owner = []
        for attendee in self.meeting_attendees:
		    if not attendee.full_name:
	        	attendee.full_name = get_attendee_name(attendee.attendee)

	    	if attendee.attendee in found_attendee:
	        	frappe.throw(_("Duplicate attendee {0} found").format(attendee.attendee))
            	found_attendee.append(attendee.attendee)

	#for chair in self.meeting_chair:
           # if not chair.chair_name:
               # chair.chair_name = get_chair_name(chair.user)

	    #if chair.user in found_chair:
             #   frappe.throw(_("Duplicate chair {0} found").format(chair.user))

            #found_chair.append(chair.user)

	
	#for coordinator in self.meeting_coordinator:
         #   if not coordinator.coordinator_name:
          #      coordinator.coordinator_name = get_coordinator_name(coordinator.user)

	   # if coordinator.user in found_coordinator:
            #    frappe.throw(_("Duplicate coordinator {0} found").format(coordinator.user))

            #found_coordinator.append(coordinator.user)


        for owner in self.meeting_minutes:
            if not owner.owner_name:
                owner.owner_name = get_owner_name(owner.owner_assigned_to)

	    if owner.owner_assigned_to in found_owner:
                frappe.throw(_("Duplicate task owner {0} found").format(owner.owner_assigned_to))

            found_owner.append(owner.owner_assigned_to)


@frappe.whitelist()
def get_attendee_name(attendee):
    user = frappe.get_doc("User", attendee)
    return " ".join(filter(None,[user.first_name,user.middle_name,user.last_name]))

#@frappe.whitelist()
#def get_chair_name(chair):
 #   user = frappe.get_doc("User", chair)
  #  return " ".join(filter(None,[user.first_name,user.middle_name,user.last_name]))

#@frappe.whitelist()
#def get_coordinator_name(coordinator):
 #   user = frappe.get_doc("User", coordinator)
  #  return " ".join(filter(None, [user.first_name,user.middle_name,user.last_name]))

@frappe.whitelist()
def get_owner_name(owner):
    user = frappe.get_doc("User", owner)
    return " ".join(filter(None,[user.first_name,user.middle_name,user.last_name]))

from django.db import models


class AttendeeEvent(models.Model):

    attendee = models.ForeignKey("Attendee", on_delete=models.CASCADE)
    event = models.ForeignKey("Event", on_delete=models.CASCADE)
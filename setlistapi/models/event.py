from django.db import models

class Event(models.Model):

    headliner = models.ForeignKey("Artist", on_delete=models.CASCADE, related_name="headliner")
    opener = models.ForeignKey("Artist", on_delete=models.CASCADE, related_name="opener")
    city = models.ForeignKey("City", on_delete=models.CASCADE)
    state = models.ForeignKey("State", on_delete=models.CASCADE)
    date = models.DateField(auto_now = False, auto_now_add = False)
    venue = models.ForeignKey("Venue", on_delete=models.CASCADE)
    attendees = models.ManyToManyField("Attendee", through="AttendeeEvent", related_name="attending")

    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value
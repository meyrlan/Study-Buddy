from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import User
from place.models import Place


class Appointment(models.Model):
    topic = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    date = models.DateTimeField()
    time = models.TimeField()
    offline_mode = models.BooleanField(default=True)
    meeting_link = models.CharField(max_length=255, blank=True)
    place = models.ForeignKey(
        Place,
        verbose_name=_("Place"),
        on_delete=models.PROTECT,
        related_name="place_appointments",
    )
    users = models.ManyToManyField(
        User,
        verbose_name=_("User"),
        related_name="appointments",
        db_table="users_appointments",
    )
    host = models.ForeignKey(
        User,
        verbose_name=_("Host"),
        on_delete=models.PROTECT,
        related_name="host_appointments",
    )

    def __str__(self):
        return f"{self.topic}"
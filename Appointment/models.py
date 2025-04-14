from django.db import models
from django.contrib.auth.models import User


class Therapist(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # کاربری که نوبت را ثبت کرده است
    therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)  # درمانگر مربوطه
    date = models.DateTimeField()  # تاریخ و زمان نوبت
    notes = models.TextField(blank=True, null=True)  # یادداشت‌های اختیاری

    def __str__(self):
        return f"{self.user.username} - {self.therapist.name} - {self.date}"

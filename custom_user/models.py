from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# model for custom user (or rather user profile)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    random_number = models.IntegerField(null=True, blank=False)

    def __str__(self):
        return f'{self.user}'

    def get_absolute_url(self):  # returns to profile detail view
        return reverse('custom_user:details', kwargs={"pk": self.user.pk})

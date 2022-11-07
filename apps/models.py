from django.db.models import Model, CharField, EmailField, DateField
from django.utils.timezone import now


class Employee(Model):
    name = CharField(max_length=255)
    email = EmailField(max_length=255)
    address = CharField(max_length=255)
    phone = CharField(max_length=50)
    year = DateField()

    @property
    def get_age(self):
        return now().year - self.year.year

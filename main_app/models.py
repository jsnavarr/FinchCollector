from django.db import models
from django.urls import reverse
from datetime import date

ROLES = (
    ('FoodGiver', 'FoodGiver'),
    ('FoodTaker', 'FoodTaker'),
    ('Admin', 'Admin')
)

class Meal(models.Model):
    description = models.CharField(max_length=200)
    available_on = models.DateField('availability date')
    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('meals_detail', kwargs={'pk': self.id})

class User(models.Model):
    role = models.CharField(
        max_length = 12,
        choices = ROLES,
        default = ROLES[0][1]
    )
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    logo = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    meals = models.ManyToManyField(Meal)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'user_id': self.id})

class Phone(models.Model):
    number = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.number
        # return f"{self.get_number_display()} on {self.number}"

    # change the default sort
    # class Meta:
    #     ordering = ['-date']
    
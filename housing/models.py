from django.db import models
from django.db.models.fields import IntegerField
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


class HousingOption(models.Model):
    """
    Example Inputs - Need to be put on Heroku
    """
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=1000)
    numberOfBedrooms = models.IntegerField(default=0)
    numberOfBathrooms = models.IntegerField(default=0)
    pricePerUnit = models.IntegerField(default=0)
    website = models.CharField(max_length=3000, blank=False)
    furnished = models.BooleanField(default=False)
    description = models.TextField(default="")
    pic = models.URLField(
        default='https://cdn-icons-png.flaticon.com/128/2101/2101126.png')

    def __str__(self):
        return self.name + "\t" + self.address


class Review(models.Model):
    housing = models.ForeignKey(
        HousingOption, on_delete=models.CASCADE, related_name='reviews')
    user = models.CharField(max_length=300, default="")
    body = models.TextField()
    created_on = models.DateTimeField(default=now, editable=False)
    rating = IntegerField(default=5, validators=[
                          MaxValueValidator(10), MinValueValidator(0)])

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Review {} by {}'.format(self.body, self.name)

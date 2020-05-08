from django.db import models


class Requests(models.Model):
    delivery_date = models.DateTimeField()
    address = models.CharField(max_length=50)
    description = models.TextField()
    author = models.CharField(max_length=50)
#     offers = models.Model('Offers')
#
#
# class Offers(models.Model):
#     name_of_provider = models.CharField(max_length=50)
#     date = models.DateTimeField()
#     price = models.CharField(max_length=50)

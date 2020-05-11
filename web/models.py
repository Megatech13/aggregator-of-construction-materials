from django.db import models


class MaterialRequests(models.Model):
    author = models.CharField(max_length=50)
    delivery_date = models.DateTimeField()
    address = models.TextField()
    description = models.TextField()


class Offers(models.Model):
    # wantlist_item = models.ForeignKey(MaterialRequests, on_delete=models.CASCADE)
    name_of_provider = models.CharField(max_length=50)
    date = models.DateTimeField()
    price = models.CharField(max_length=50)

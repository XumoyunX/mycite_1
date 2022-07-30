from django.db import models





class Categoriya(models.Model):
    name = models.CharField(max_length=250)


class Product(models.Model):
    categoriya = models.ForeignKey(Categoriya, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    price = models.PositiveSmallIntegerField()
    img = models.ImageField(upload_to='images/')
    text = models.TextField()


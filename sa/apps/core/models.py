from django.db import models


class Car(models.Model):
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    body_type = models.CharField(max_length=255)
    transmission = models.CharField(max_length=255)
    engine = models.DecimalField(max_digits=5, decimal_places=2)
    drive = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __unicode__(self):
        return "%s %s" % (self.make, self.model)

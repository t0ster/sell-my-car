# -*- coding: utf-8 -*-
from django.db import models


class Car(models.Model):
    SEDAN_BODY_TYPE = u'Седан'
    HATCHBACK_BODY_TYPE = u'Хетчбэк'
    WAGON_BODY_TYPE = u'Универсал'
    BODY_TYPE_CHOICES = (
        (SEDAN_BODY_TYPE, u'Седан'),
        (HATCHBACK_BODY_TYPE, u'Хетчбэк'),
        (WAGON_BODY_TYPE, u'Универсал'),
    )

    MANUAL_TRANSMISSION = u'Механическая'
    AUTOMATIC_TRANSMISSION = u'Автомат'
    TRANSMISSION_CHOICES = (
        (MANUAL_TRANSMISSION, u'Механическая'),
        (AUTOMATIC_TRANSMISSION, u'Автомат'),
    )

    FRONT_DRIVE = u'Передняя'
    REAR_DRIVE = u'Задняя'
    ALL_DRIVE = u'4x4'
    DRIVE_CHOICES = (
        (FRONT_DRIVE, u'Передняя'),
        (REAR_DRIVE, u'Задняя'),
        (ALL_DRIVE, u'4x4'),
    )
    make = models.CharField(max_length=255, verbose_name=u"Марка")
    model = models.CharField(max_length=255, verbose_name=u"Модель")
    body_type = models.CharField(max_length=255, choices=BODY_TYPE_CHOICES, verbose_name=u"Тип Кузова")
    transmission = models.CharField(max_length=255, choices=TRANSMISSION_CHOICES, verbose_name=u"КПП")
    drive = models.CharField(max_length=255, choices=DRIVE_CHOICES, verbose_name=u"Подвеска")
    engine = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=u"Обьем двигателя")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=u"Цена")

    @models.permalink
    def get_absolute_url(self):
        return ('car', [str(self.pk)])

    def __unicode__(self):
        return "%s %s" % (self.make, self.model)

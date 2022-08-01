from django.utils.translation import gettext_lazy as _
from django.db import models
from django_countries.fields import CountryField

from apps.common.models import TimeStampedUUIDModel


class VpnCountry(TimeStampedUUIDModel):
    place = CountryField(verbose_name=_("Country"), blank_label="(select country)", unique=True, null=False)
    discount_percentage = models.PositiveIntegerField(verbose_name=_("Country discount percentage"), default=0)

    class Meta:
        verbose_name = "Vpn country"
        verbose_name_plural = "Vpn Countries"

    @property
    def country(self) -> str:
        return self.place.name

    def __str__(self):
        return f'Country {self.place} with discount {self.discount_percentage}'
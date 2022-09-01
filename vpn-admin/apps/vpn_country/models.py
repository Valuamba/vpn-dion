from django.utils.translation import gettext_lazy as _
from django.db import models
from django_countries.fields import CountryField

from apps.common.models import TimeStampedUUIDModel


class VpnCountry(TimeStampedUUIDModel):
    place = CountryField(verbose_name=_("Country"), blank_label="(select country)", unique=True, null=False)
    discount_percentage = models.PositiveIntegerField(verbose_name=_("Country discount percentage"), default=0)
    is_default = models.BooleanField(verbose_name=_("Is default"), default=False)

    class Meta:
        verbose_name = "Vpn country"
        verbose_name_plural = "Vpn Countries"
        db_table = "vpn_countries"

    @classmethod
    def get_defaults(cls):
        results = VpnCountry.objects.raw('''
SELECT c.pkid, place, discount_percentage, is_default FROM public.vpn_countries as c 
INNER JOIN public.vpn_instances as i on country_id = c.pkid
WHERE i.is_online=True and c.is_default=True
GROUP BY c.pkid, place, discount_percentage
''')
        return results

    @property
    def country(self) -> str:
        return self.place.name

    def __str__(self):
        return f'Country {self.place} with discount {self.discount_percentage}'
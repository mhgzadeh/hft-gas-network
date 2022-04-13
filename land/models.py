from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _


class LandParcel(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name=_('id'))
    geometry = models.PolygonField(srid=25832, verbose_name=_('geometry'))
    area = models.FloatField(verbose_name=_('area'))


class Owners(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name=_('id'))
    name = models.CharField(verbose_name=_('name'))


class Own(models.Model):
    land_parcel = models.ForeignKey(LandParcel, from_fields='id', on_delete=models.PROTECT, related_name='owns',
                                    verbose_name=_('land_parcels')
                                    )
    owner = models.ForeignKey(Owners, from_fields='id', on_delete=models.PROTECT, related_name='owns',
                              verbose_name=_('owners'))

# -*- coding: utf-8 -*-
import re
import os
import datetime

from django.db import models
from django.db.models import permalink
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from hvad.models import TranslatableModel, TranslatedFields

from stnb.membres.models import Membre
from stnb.utils.text_processing import text_sense_accents

def nom_fitxer(ruta, nom):
    fitxer_nom = text_sense_accents(nom)
    return os.path.join(ruta, fitxer_nom)

def presentacio_nom_fitxer(esdeveniment, nom):
    ruta = 'esdeveniments/presentacions'
    fitxer_nom = nom_fitxer(ruta, nom)
    return fitxer_nom

def article_nom_fitxer(esdeveniment, nom):
    ruta = 'esdeveniments/articles'
    fitxer_nom = nom_fitxer(ruta, nom)
    return fitxer_nom

class Serie(TranslatableModel):
    slug = models.SlugField(_('slug'), max_length=50)
    organitzadors = models.ManyToManyField(Membre, verbose_name=_('organisers'),
                                           related_name='series',
                                           blank=True)
    altres_organitzadors = models.CharField(_('other organisers'),
                                            max_length=250, blank=True,
                                            null=True)

    translations = TranslatedFields(
        nom = models.CharField(_('name'), max_length=50),
        descripcio = models.TextField(_('description'), blank=True, null=True),
    )

    class Meta:
        verbose_name = _('series')
        verbose_name_plural = _('series')

    def __unicode__(self):
        return self.nom

class Esdeveniment(TranslatableModel):
    slug = models.SlugField(_('slug'), max_length=100)
    serie = models.ForeignKey(Serie, verbose_name=_('serie'), blank=True,
                              null=True, related_name='esdeveniments')
    data = models.DateField(_('date'))

    amfitrions = models.ManyToManyField(Membre, verbose_name=_('hosts'),
                                        related_name='esdeveniments_organizats',
                                        blank=True)
    altres_amfitrions = models.CharField(_('other hosts'), max_length=250,
                                         blank=True, null=True)
    presentadors = models.ManyToManyField(Membre, verbose_name=_('presenters'),
                                          related_name=
                                              'esdeveniments_presentats',
                                          blank=True)
    altres_presentadors = models.CharField(_('other presenters'),
                                           max_length=250, blank=True,
                                           null=True)

    presentacio = models.FileField(_('presentation'),
                                   upload_to=presentacio_nom_fitxer,
                                   blank=True, null=True)
    article = models.FileField(_('article'), upload_to=article_nom_fitxer,
                               blank=True, null=True)

    translations = TranslatedFields(
        titol = models.CharField(_('title'), max_length=255),
        abstracte = models.TextField(_('abstract'), blank=True, null=True),
        lloc = models.TextField(_('location')),
    )

    class Meta:
        verbose_name = _('event')
        verbose_name_plural = _('events')
        ordering = ['-data']

    def __unicode__(self):
        return self.titol

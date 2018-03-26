# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from base.us_states import STATE_CHOICES, USPS_CHOICES
from base.managers import ActiveManager


# Create your models here.


class USStateField(models.CharField):

    description = _("U.S. state (two uppercase letters)")

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = STATE_CHOICES
        kwargs['max_length'] = 2
        super(USStateField, self).__init__(*args, **kwargs)


class USPostalCodeField(models.CharField):

    description = _("U.S. postal code (two uppercase letters)")

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = USPS_CHOICES
        kwargs['max_length'] = 2
        super(USPostalCodeField, self).__init__(*args, **kwargs)


class PhoneNumberField(models.CharField):

    description = _("Phone number")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 20
        super(PhoneNumberField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        from .forms import USPhoneNumberField
        defaults = {'form_class': USPhoneNumberField}
        defaults.update(kwargs)
        return super(PhoneNumberField, self).formfield(**defaults)


class BaseAddress(models.Model):
    address_1 = models.CharField(_("address"), max_length=128)
    address_2 = models.CharField(_("address cont'd"), max_length=128, blank=True)

    city = models.CharField(_("city"), max_length=64, default="Sacramento")
    state = USStateField(_("state"), default="CA")
    zip_code = models.CharField(_("zip code"), max_length=5, default="95827")

    class Meta:
        abstract = True


class BaseProfile(models.Model):
    GENDER_CHOICES = (
        ('F', 'Female',),
        ('M', 'Male',),
        ('U', 'Undisclose',),
    )
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
    )
    dob = models.DateField(null=True, blank=True)

    class Meta:
        abstract = True


class BaseUser(BaseProfile):
    user = models.OneToOneField(User)
    
    # temporary account freeze field indicator
    acc_freeze_in = models.BooleanField(default=False)

    # invoke managers
    active_members = ActiveManager()

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.user.username


class BaseChildProfile(BaseProfile):
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return u'%s, %s' % (self.last_name, self.first_name) 

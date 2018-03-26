from django.db import models

from base.us_states import STATE_CHOICES, USPS_CHOICES
from base.forms import USPhoneNumberField


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
        defaults = {'form_class': USPhoneNumberField}
        defaults.update(kwargs)
        return super(PhoneNumberField, self).formfield(**defaults)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create managers here.


class ActiveManager(models.Manager):
    def get_query_set(self):
        return super(ActiveManager, self).get_query_set().filter(acc_freeze_in=False)

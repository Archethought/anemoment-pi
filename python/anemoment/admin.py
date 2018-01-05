from django.contrib import admin

from .models import WindData, RawInputError

admin.site.register(WindData)
admin.site.register(RawInputError)

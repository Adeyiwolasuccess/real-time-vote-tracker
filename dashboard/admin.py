from django.contrib import admin
from .models import Party, PollingUnit, Submission

admin.site.register(Party)
admin.site.register(PollingUnit)
admin.site.register(Submission)
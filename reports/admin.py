from django.contrib import admin
from .models import Report
from leaflet.admin import LeafletGeoAdmin



admin.site.register(Report, LeafletGeoAdmin)
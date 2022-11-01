from django.contrib import admin

# Applications:
#  ○ operationsMetrics (home)
#  ○ packagesPerHour
#  ○ DEX
#  ○ volumeAvailabilityStatus

# Register your models here.
from .models import packagesPerHour, Exceptions, DEX, volumeAvailabilityStatus

admin.site.register(packagesPerHour)
admin.site.register(Exceptions)
admin.site.register(DEX)
admin.site.register(volumeAvailabilityStatus)
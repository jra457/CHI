from django.contrib import admin
from .models import packagesPerHour, Exceptions, DEX, volumeAvailabilityStatus, Region, Facility

# ~~~~~ Applications ~~~~~
#  ○ operationsMetrics (home)
#  ○ packagesPerHour
#  ○ DEX
#  ○ volumeAvailabilityStatus
# ~~~~~

# ~~~~~ Models ~~~~~
admin.site.register(packagesPerHour)
admin.site.register(Exceptions)
admin.site.register(DEX)
admin.site.register(volumeAvailabilityStatus)
admin.site.register(Region)
admin.site.register(Facility)
# ~~~~~
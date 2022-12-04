from django.contrib import admin
from .models import Division, Region, District, Location, packagesPerHour, Employee

# ~~~~~ Applications ~~~~~
#  ○ operationsMetrics (home)
#  ○ packagesPerHour
#  ○ DEX
#  ○ volumeAvailabilityStatus
# ~~~~~

# ~~~~~ Models ~~~~~
admin.site.register(packagesPerHour)
admin.site.register(Division)
admin.site.register(Region)
admin.site.register(District)
admin.site.register(Location)
# ~~~~~
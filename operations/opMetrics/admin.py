from django.contrib import admin
from .models import Division, Region, District, Location, packagesPerHour, Employee, Package, Company

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
admin.site.register(Package)
admin.site.register(Company)
# ~~~~~
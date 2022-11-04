from django.shortcuts import render
from django.views import generic
from .models import packagesPerHour, Exceptions, DEX, volumeAvailabilityStatus, Region, Facility

# ~~~~~ Documentation ~~~~~
# https://docs.djangoproject.com/en/4.0/topics/class-based-views/generic-display/
# ~~~~~

# ~~~~~ Operation Metrics Home Page ~~~~~
def operationsMetrics(request):
    """View function for home page of site."""

    # Generate counts of the main objects
    numPackagesPerHour = packagesPerHour.objects.all().count()
    numExceptions = Exceptions.objects.all().count()
    numDEX = DEX.objects.all().count()
    numVolAvailStats = volumeAvailabilityStatus.objects.all().count()

    context = {
        'numPackagesPerHour': numPackagesPerHour,
        'numExceptions': numExceptions,
        'numDEX': numDEX,
        'numVolAvailStats': numVolAvailStats,
    }

    # Render the HTML template metrics.html with the data in the context variable
    return render(request, 'operationsMetrics.html', context=context)
# ~~~~~



# ~~~~~ Region Classes ~~~~~
class RegionListView(generic.ListView):
    """Generic class-based list view for a region."""
    model = Region

class RegionDetailView(generic.DetailView):
    """Generic class-based detail view for a region."""
    model = Region
# ~~~~~



# ~~~~~ Facility Classes ~~~~~
class FacilityListView(generic.ListView):
    """Generic class-based list view for a facility."""
    model = Facility

class FacilityDetailView(generic.DetailView):
    """Generic class-based detail view for a facility."""
    model = Facility
# ~~~~~



# ~~~~~ Packages Per Hour Classes ~~~~~
class packagesPerHourListView(generic.ListView):
    """Generic class-based list view for a region."""
    model = packagesPerHour

class packagesPerHourDetailView(generic.DetailView):
    """Generic class-based detail view for a region."""
    model = packagesPerHour
# ~~~~~
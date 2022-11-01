from django.shortcuts import render
from django.views import generic
# Create your views here.
from .models import packagesPerHour, Exceptions, DEX, volumeAvailabilityStatus
# https://docs.djangoproject.com/en/4.0/topics/class-based-views/generic-display/
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

class packagesPerHourView(generic.ListView):
    model = packagesPerHour
from django.db import models
from django.urls import reverse
from datetime import date

# ~~~~~ Applications ~~~~~
#  ○ operationsMetrics (home)
#  ○ packagesPerHour
#  ○ DEX
#  ○ volumeAvailabilityStatus
# ~~~~~

# book -> packagesPerHour
# ~~~~~ packagesPerHour Model ~~~~~
class packagesPerHour(models.Model):
    """Model representing Packages Per Hour."""
    pph = models.IntegerField('packagesPerHour', default=0, help_text='Enter the Number of Packages per Hour', null=True, blank=True)
    facility = models.ForeignKey('Facility', on_delete=models.SET_NULL, null=True, blank=True, default="test")
    date = models.DateField('date', default=date.today, null=True, blank=True)

    class Meta:
        ordering = ['pph']

    def get_absolute_url(self):
        """Returns the url to access a particular pph instance."""
        return reverse('packagesPerHour-detail', args=[str(self.id)])

    def __int__(self):
        """String for representing the Model object."""
        return self.pph
# ~~~~~



# author -> facility
# ~~~~~ Facility Model ~~~~~
class Facility(models.Model):
    name = models.CharField(max_length=100, help_text="Enter a Facility Name.")
    location = models.CharField('Location', max_length=20,
                        unique=True,
                        help_text="Enter a Facility Location.",
                        default="noAddress")

    def get_absolute_url(self):
        """Returns the url to access a particular region instance."""
        return reverse('facility-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name
# ~~~~~



# ~~~~~ Region Model ~~~~~
class Region(models.Model):
    """Model representing Regions."""
    name = models.CharField(max_length=200)

    facility = models.ManyToManyField(Facility, help_text="Select a Facility to add to the Region.")
    
    class Meta:
        ordering = ['name']

    def display_facility(self):
        """Creates a string for the Facility. This is required to display facility in Admin."""
        return ', '.join([facility.name for facility in self.facility.all()[:3]])

    display_facility.short_description = 'Facility'

    def get_absolute_url(self):
        """Returns the url to access a particular region instance."""
        return reverse('region-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.name
# ~~~~~



# ~~~~~ Exceptions Model ~~~~~
class Exceptions(models.Model):
    """Model representing Exceptions."""
    name = models.CharField(max_length=200, help_text='Enter an Exception Type.')

    def __str__(self):
        """String for representing the Model object."""
        return self.name
# ~~~~~



# ~~~~~ DEX Model ~~~~~
class DEX(models.Model):
    """Model representing Delivery Exceptions (by exception type)."""
    name = models.CharField(max_length=200, help_text='DEX')

    exception = models.ManyToManyField(Exceptions, help_text='Select an Exception.')

    def __str__(self):
        """String for representing the Model object."""
        return self.exception

    def __str__(self):
        """String for representing the Model object."""
        return self.name
# ~~~~~



# ~~~~~ volumeAvailabilityStatus Model ~~~~~
class volumeAvailabilityStatus(models.Model):
    """Model representing Volume Availability Status."""
    name = models.CharField(max_length=200, help_text='Volume Availability Status')

    def __str__(self):
        """String for representing the Model object."""
        return self.name
# ~~~~~
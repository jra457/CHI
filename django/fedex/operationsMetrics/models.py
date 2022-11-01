from django.db import models

# Applications:
#  ○ operationsMetrics (home)
#  ○ packagesPerHour
#  ○ DEX
#  ○ volumeAvailabilityStatus

# Create your models here.
# ~~~~~ packagesPerHour ~~~~~
class packagesPerHour(models.Model):
    """Model representing Packages Per Hour."""
    name = models.CharField(max_length=200, help_text='Packages Per Hour')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

# ~~~~~ Exceptions ~~~~~
class Exceptions(models.Model):
    """Model representing Exceptions."""
    name = models.CharField(max_length=200, help_text='Enter an Exception Type.')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

# ~~~~~ DEX ~~~~~
class DEX(models.Model):
    """Model representing Delivery Exceptions (by exception type)."""
    name = models.CharField(max_length=200, help_text='DEX')

    exception = models.ManyToManyField(Exceptions, help_text='Select an Exception.')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

# ~~~~~ volumeAvailabilityStatus ~~~~~
class volumeAvailabilityStatus(models.Model):
    """Model representing Volume Availability Status."""
    name = models.CharField(max_length=200, help_text='Volume Availability Status')

    def __str__(self):
        """String for representing the Model object."""
        return self.name
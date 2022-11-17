from django.db import models
from django.urls import reverse
from datetime import date

# ~~~~~ (1) Division Model ~~~~~
class Division(models.Model):
    """Model representing the Division."""
    division = models.CharField(max_length=10, help_text='Division Name')

    def __str__(self):
        """String for representing the Model object."""
        return self.division
# ~~~~~



# ~~~~~ (2) Region Model ~~~~~
class Region(models.Model):
    """Model representing the Region."""
    division = models.ForeignKey(Division, on_delete=models.CASCADE, null=True)

    region = models.CharField(max_length=15, help_text='Region Name', default='')

    def __str__(self):
        """String for representing the Model object."""
        return self.region
# ~~~~~



# ~~~~~ (3) District Model ~~~~~
class District(models.Model):
    """Model representing the District."""
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, default='')

    district = models.CharField(max_length=15, help_text='Enter District Name.')

    def __str__(self):
        """String for representing the Model object."""
        return self.district
# ~~~~~



# ~~~~~ (4) Location Model ~~~~~
class Location(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)

    location = models.CharField(max_length=5, help_text='Enter the Location Name.')

    senior_Manager = models.CharField(max_length=25, help_text='Enter the Location Type.')

    # ~~~~~ Location Type
    Hub, Ramp, Station = 'Hub', 'Ramp', 'Station'

    typeChoices = [
        (Hub, 'Hub'), (Ramp, 'Ramp'), (Station, 'Station')
    ]

    type = models.CharField(
        max_length=10,
        choices=typeChoices,
        default=Hub,
    )
    # ~~~~~

    # ~~~~~ Location State
    Alabama       , Alaska        , Arizona        = 'AL', 'AK', 'AZ'
    Arkansas      , California    , Colorado       = 'AR', 'CA', 'CO'
    Connecticut   , Delaware      , Florida        = 'CT', 'DE', 'FL'
    Georgia       , Hawaii        , Idaho          = 'GA', 'HI', 'ID'
    Illinois      , Indiana       , Iowa           = 'IL', 'IN', 'IA'
    Kansas        , Kentucky      , Louisiana      = 'KS', 'KY', 'LA'
    Maine         , Maryland      , Massachusetts  = 'ME', 'MD', 'MA'
    Michigan      , Minnesota     , Mississippi    = 'MI', 'MN', 'MS'
    Missouri      , Montana       , Nebraska       = 'MO', 'MT', 'NE'
    Nevada        , New_Hampshire , New_Jersey     = 'NV', 'NH', 'NJ'
    New_Mexico    , New_York      , North_Carolina = 'NM', 'NY', 'NC'
    North_Dakota  , Ohio          , Oklahoma       = 'OR', 'PA', 'RI'
    Oregon        , Pennsylvania  , Rhode_Island   = 'OR', 'PA', 'RI'
    South_Carolina, South_Dakota  , Tennessee      = 'SC', 'SD', 'TN'
    Texas         , Utah          , Vermont        = 'TX', 'UT', 'VT'
    Virginia      , Washington    , West_Virginia  = 'VA', 'WA', 'WV'
    Wisconsin     , Wyoming                        = 'WI', 'WY'

    stateChoices = [
        (Alabama       , 'Alabama'       ), (Alaska       , 'Alaska'       ), (Arizona       , 'Arizona       '),
        (Arkansas      , 'Arkansas'      ), (California   , 'California'   ), (Colorado      , 'Colorado      '),
        (Connecticut   , 'Connecticut'   ), (Delaware     , 'Delaware'     ), (Florida       , 'Florida       '),
        (Georgia       , 'Georgia'       ), (Hawaii       , 'Hawaii'       ), (Idaho         , 'Idaho         '),
        (Illinois      , 'Illinois'      ), (Indiana      , 'Indiana'      ), (Iowa          , 'Iowa          '),
        (Kansas        , 'Kansas'        ), (Kentucky     , 'Kentucky'     ), (Louisiana     , 'Louisiana     '),
        (Maine         , 'Maine'         ), (Maryland     , 'Maryland'     ), (Massachusetts , 'Massachusetts '),
        (Michigan      , 'Michigan'      ), (Minnesota    , 'Minnesota'    ), (Mississippi   , 'Mississippi   '),
        (Missouri      , 'Missouri'      ), (Montana      , 'Montana'      ), (Nebraska      , 'Nebraska      '),
        (Nevada        , 'Nevada'        ), (New_Hampshire, 'New Hampshire'), (New_Jersey    , 'New Jersey    '),
        (New_Mexico    , 'New Mexico'    ), (New_York     , 'New York'     ), (North_Carolina, 'North Carolina'),
        (North_Dakota  , 'North Dakota'  ), (Ohio         , 'Ohio'         ), (Oklahoma      , 'Oklahoma      '),
        (Oregon        , 'Oregon'        ), (Pennsylvania , 'Pennsylvania' ), (Rhode_Island  , 'Rhode Island  '),
        (South_Carolina, 'South Carolina'), (South_Dakota , 'South Dakota' ), (Tennessee     , 'Tennessee     '),
        (Texas         , 'Texas'         ), (Utah         , 'Utah'         ), (Vermont       , 'Vermont       '),
        (Virginia      , 'Virginia'      ), (Washington   , 'Washington'   ), (West_Virginia , 'West Virginia '),
        (Wisconsin     , 'Wisconsin'     ), (Wyoming      , 'Wyoming'      )
    ]

    state = models.CharField(
        max_length=2,
        choices=stateChoices,
        default=Alabama
    )
    # ~~~~~

    def get_absolute_url(self):
        """Returns the url to access a particular location instance."""
        return reverse('location-detail', args=[str(self.id)])

    def __str__(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        str = 'Location: ' + self.location + ", " + self.senior_Manager + ", " + self.type + ", " + self.state
        return str
# ~~~~~



# ~~~~~ packagesPerHour Model ~~~~~
class packagesPerHour(models.Model):
    objects = models.Manager()
    """Model representing Packages Per Hour."""
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    pph = models.IntegerField('packagesPerHour', default=0, help_text='Enter the Number of Packages per Hour', null=True, blank=True)
    date = models.DateField('date', default=date.today, null=True, blank=True)
    
    class Meta:
        ordering = ['date']

    def get_absolute_url(self):
        """Returns the url to access a particular pph instance."""
        return reverse('packagesPerHour-detail', args=[str(self.id)])

    def __str__(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        #str = self.location.location + f"{date}" + self.pph
        
        return f"{self.location.location}, {self.date}, {self.pph}"
# ~~~~~



# ~~~~~ Employee Model ~~~~~
class Employee(models.Model):
    firstName = models.CharField(max_length=30)

    lastName = models.CharField(max_length=30)
    
    class Meta:
        ordering = ['lastName']

    def __str__(self):
        return f"{self.lastname}, {self.firstName}"
# ~~~~~
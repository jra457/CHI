from django.db import models
from django.urls import reverse
from datetime import date

# ~~~~~ (1) Division Model ~~~~~
class Division(models.Model):
    """Model representing the Division."""
    name = models.CharField(max_length=10, help_text='Division Name')

    def __str__(self):
        """String for representing the Model object."""
        return self.division
# ~~~~~



# ~~~~~ (2) Region Model ~~~~~
class Region(models.Model):
    """Model representing the Region."""
    division = models.ForeignKey(Division, on_delete=models.CASCADE, null=True)

    name = models.CharField(max_length=15, help_text='Region Name', default='')

    def __str__(self):
        """String for representing the Model object."""
        return self.region
# ~~~~~



# ~~~~~ (3) District Model ~~~~~
class District(models.Model):
    """Model representing the District."""
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, default='')

    name = models.CharField(max_length=15, help_text='Enter District Name.')

    def __str__(self):
        """String for representing the Model object."""
        return self.district
# ~~~~~



# ~~~~~ (4) Location Model ~~~~~
class Location(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)

    name = models.CharField(max_length=5, help_text='Enter the Location Name.')

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

    def get_pph(self):
        return packagesPerHour.get_location_pph(self.id)

    def get_absolute_url(self):
        """Returns the url to access a particular location instance."""
        return reverse('location-detail', args=[str(self.id)])

    def __str__(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        str = 'Location: ' + self.name + ", " + self.senior_Manager + ", " + self.type + ", " + self.state
        return str
# ~~~~~



from django.db.models import Sum, Avg
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

    def get_location_pph(locationID):
        today = date.today()
        todayRange = packagesPerHour.objects.filter(location_id=locationID, date__range=[today, today])
        todaySum = todayRange.aggregate(Sum('pph'))['pph__sum']
        todayAvg = todayRange.aggregate(Avg('pph'))['pph__avg']

        if todaySum == None:
            todaySum = 0
            todayAvg = 0

        return {'sum': todaySum, 'avg': todayAvg, 'date': today.strftime("%m/%d/%y")}

    def get(self, input1):
        print(input1)
        pass

    def __str__(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        #str = self.location.location + f"{date}" + self.pph

        return f"{self.location.name}, {self.date}, {self.pph}"
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

def getLevel2Dict(levelInput):
    if levelInput == "company":
        returnDict = {}

    else:
        levelDict = {
            "division": Division.objects.all(),
            "region":   Region.objects.all(),
            "district": District.objects.all(),
            "location": Location.objects.all(),
        }
        levelList = levelDict.get(levelInput)

        returnDict = {}
        for level in levelList:
            returnDict[level.name] = level.id

    return returnDict

from itertools import chain
def getOutputData(levelType, id, startDate, endDate):
    # If Division:
        # If (US Ops) output:
            # Regions (Eastern)
            # Districts (Founders, High Rise)
            # Locations (OWDA, CEFA, NYCA, JRBA)
        # If (AGFS) output:
            # Regions (Western AGFS)
            # Districts (Paradise, Lake)
            # Locations (ANCIP, ANCRT, HNLRT, COSR, SEART)

    # If Region:
        # If (Eastern) output:
            # Districts (Founders, High Rise)
            # Locations (OWDA, CEFA, NYCA, JRBA)
        # If (Western AGFS) output:
            # Districts (Paradise, Lake)
            # Locations (ANCIP, ANCRT, HNLRT, COSR, SEART)

    # If District:
        # If (Founders) output:
            # Locations (OWDA, CEFA)
        # If (High Rise) output:
            # Locations (NYCA, JRBA) 
        # If (Paradise) output:
            # Locations (ANCIP, ANCRT)  
        # If (Lake) output:
            # Locations (HNLRT, COSR, SEART)

    if levelType == "company" or id == None:
        divisionList = Division.objects.all()

        idList = []
        for division in divisionList:
            idList.append(division.id)

        data = []
        for id in idList:
            data = chain(data, packagesPerHour.objects.filter(location__district__region__division__id=id, date__range=[startDate, endDate]))
            
    else:
        dataDict = {
            "division": packagesPerHour.objects.filter(location__district__region__division__id=id, date__range=[startDate, endDate]),
            "region":   packagesPerHour.objects.filter(location__district__region__id=id, date__range=[startDate, endDate]),
            "district": packagesPerHour.objects.filter(location__district__id=id, date__range=[startDate, endDate]),
            "location": packagesPerHour.objects.filter(location__id=id, date__range=[startDate, endDate]),
        }
        data = dataDict.get(levelType)

    return data

from datetime import datetime
def getDate():
    now = datetime.now()
    return f"{now.year}-{now.month}-{now.day}"
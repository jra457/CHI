from django.shortcuts import render
from datetime import datetime
import calendar
from calendar import HTMLCalendar
from .forms import PackagesForm
from django.views import generic
from .models import Division, Region, District, Location, \
    packagesPerHour, getLevel2Dict, getToday, getOutputData

# ~~~~~ Add Packages ~~~~~
def addpackages(request):
    # ~~~~~ Initialize 
    form = PackagesForm
    # ~~~~~


    # ~~~~~ Return Generated Values ~~~~~
    context = {
        'form': form,
    }
    return render(request, 'opMetrics/addpackages.html', context=context)
    # ~~~~~
# ~~~~~


# ~~~~~ Delivery Exceptions ~~~~~
def DEX(request):


    
    # ~~~~~ Return Generated Values ~~~~~
    today = getToday()
    context = {
        'today': today,
    }
    return render(request, 'opMetrics/dex.html', context=context)
    # ~~~~~
# ~~~~~



# ~~~~~ Volume Availability Status ~~~~~
def VAS(request):



    # ~~~~~ Return Generated Values ~~~~~
    today = getToday()
    context = {
        'today': today,
    }
    return render(request, 'opMetrics/vas.html', context=context)
    # ~~~~~
# ~~~~~



# ~~~~~ Home ~~~~~
def home(request):


    
    # ~~~~~ Return Generated Values ~~~~~
    today = getToday()
    context = {
        'today': today,
    }
    return render(request, 'opMetrics/home.html', context=context)
    # ~~~~~
# ~~~~~



# ~~~~~ Search ~~~~~
from django.db.models import Q
def Search(request):
    query = request.GET.get("q")
    object_list = Location.objects.filter(
        Q(location=query) | Q(state=query) | Q(senior_Manager=query)
    )

    if not object_list:
        results = False
        region = ''
        division = ''
    else:
        results = True
        region = object_list[0].district.region
        division = region.division

    # ~~~~~ Return Generated Values ~~~~~
    today = getToday()
    context = {
        'today': today,
        
        'object_list': object_list,
        'query': query,
        'results': results,
    }
    return render(request, 'opMetrics/search.html', context=context)
    # ~~~~~
# ~~~~~



# ~~~~~ Company ~~~~~
def Company(request):



    # ~~~~~ Return Generated Values ~~~~~
    today = getToday()
    context = {
        'today': today,
    }
    return render(request, 'opMetrics/company.html', context=context)
    # ~~~~~
# ~~~~~


from django.core.paginator import Paginator
def packagesperhour(request, level1='company', level2='all', sDatePPH=getToday(), eDatePPH=getToday()):
    if request.method == 'POST':
        sDate = request.POST.get("sDatePPH")
        eDate = request.POST.get("eDatePPH")
        sDatePPH = sDate
        eDatePPH = eDate
        level2Dict = getLevel2Dict(level1)
        level2List = list(level2Dict.keys())
        id = level2Dict.get(level2)

        dataRange = getOutputData(level1, id, sDatePPH, eDatePPH)
    
    else:
        sDatePPH = sDatePPH
        eDatePPH = eDatePPH

        level2Dict = getLevel2Dict(level1)
        level2List = list(level2Dict.keys())
        id = level2Dict.get(level2)
        dataRange = getOutputData(level1, id, sDatePPH, eDatePPH)
    testNum = request.POST.get("test")

    paginator = Paginator(dataRange, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    def getRowNumber():
        try:
            rowNumber
        except:
            rowNumber = 0
        rowNumber = rowNumber + 1
        return rowNumber
        
    # ~~~~~ Return Generated Values ~~~~~
    context = {
        'dataRange': dataRange,
        'sDatePPH': sDatePPH,
        'eDatePPH': eDatePPH,

        'level1': level1,
        'level2': level2,
        'level2List': level2List,

        'page_obj': page_obj,
        'rowNumber': getRowNumber(),
    }
    return render(request, 'opMetrics/packagesPerHour.html', context=context)
    # ~~~~~
# ~~~~~



from django.shortcuts import get_object_or_404
class DivisionDetailView(generic.DetailView):
    model = Division

    def division_detail_view(request, primary_key):
        division = get_object_or_404(Division, pk=primary_key)
        today = getToday()
        context = {
        'division': division,
        'today': today,
        }
        return render(request, 'opMetrics/division_detail.html', context=context)

class RegionDetailView(generic.DetailView):
    model = Region

    def region_detail_view(request, primary_key):
        region = get_object_or_404(Region, pk=primary_key)
        today = getToday()
        context = {
        'region': region,
        'today': today,
        }
        return render(request, 'opMetrics/region_detail.html', context=context)

class DistrictDetailView(generic.DetailView):
    model = District

    def district_detail_view(request, primary_key):
        district = get_object_or_404(District, pk=primary_key)
        today = getToday()
        context = {
        'district': district,
        'today': today,
        }
        return render(request, 'opMetrics/district_detail.html', context=context)

class LocationDetailView(generic.DetailView):
    model = Location
    getToday()

    def location_detail_view(request, primary_key):
        location = get_object_or_404(Location, pk=primary_key)
        context = {
        'location': location,
        'today': location.today,
        }
        return render(request, 'opMetrics/location_detail.html', context=context)


# ~~~~~ Login ~~~~~
def Login(request):


    
    # ~~~~~ Return Generated Values ~~~~~
    today = getToday()
    context = {
        'today': today,
    }
    return render(request, 'opMetrics/login.html', context=context)
    # ~~~~~
# ~~~~~
    
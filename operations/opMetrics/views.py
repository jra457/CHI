from django.shortcuts import render
from django.views import generic
from datetime import datetime
from datetime import date
from datetime import timedelta
import calendar
from calendar import HTMLCalendar
from .forms import PackagesForm
from .models import Location, packagesPerHour, getLevel2Dict, getDate, getOutputData

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




# # ~~~~~ Packages Per Hour ~~~~~
# class packagesPerHourListView(generic.ListView):
#     """Generic class-based list view for a region."""
#     model = packagesPerHour
#     def get(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
#         # ~~~~~ Initialize Calendar
#         month = month.title()
#         month_number = list(calendar.month_name).index(month)
#         month_number = int(month_number)


#         cal = HTMLCalendar().formatmonth(year, month_number)
#         now = datetime.now()
#         current_year = now.year

#         time = now.strftime('%I:%M:%S %p')
#         # ~~~~~


#         # ~~~~~ Return Generated Values ~~~~~
#         context = {
#             'year': year,
#             'month': month,
#             'month_number': month_number,
#             'cal': cal,
#             'current_year': current_year,
#             'time': time,
#         }
#         return render(request, 'opMetrics/packagesperhour.html', context=context)
#         # ~~~~~
# # ~~~~~

# # ~~~~~ Packages Per Hour Classes ~~~~~
# class packagesPerHourListView(generic.ListView):
#     """Generic class-based list view for a region."""
#     model = packagesPerHour

# class packagesPerHourDetailView(generic.DetailView):
#     """Generic class-based detail view for a region."""
#     model = packagesPerHour
# # ~~~~~


# ~~~~~ Delivery Exceptions ~~~~~
def DEX(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    # ~~~~~ Initialize Calendar
    month = month.title()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)


    cal = HTMLCalendar().formatmonth(year, month_number)
    now = datetime.now()
    current_year = now.year

    time = now.strftime('%I:%M:%S %p')
    # ~~~~~


    # ~~~~~ Return Generated Values ~~~~~
    context = {
        'year': year,
        'month': month,
        'month_number': month_number,
        'cal': cal,
        'current_year': current_year,
        'time': time,
    }
    return render(request, 'opMetrics/dex.html', context=context)
    # ~~~~~
# ~~~~~



# ~~~~~ Volume Availability Status ~~~~~
def VAS(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    # ~~~~~ Initialize Calendar
    month = month.title()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)


    cal = HTMLCalendar().formatmonth(year, month_number)
    now = datetime.now()
    current_year = now.year

    time = now.strftime('%I:%M:%S %p')
    # ~~~~~


    # ~~~~~ Return Generated Values ~~~~~
    context = {
        'year': year,
        'month': month,
        'month_number': month_number,
        'cal': cal,
        'current_year': current_year,
        'time': time,
    }
    return render(request, 'opMetrics/vas.html', context=context)
    # ~~~~~
# ~~~~~



# ~~~~~ Home ~~~~~
def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    # ~~~~~ Initialize Calendar
    month = month.title()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    day_number = datetime.now().strftime('%d')

    today = f"{year}-{month_number}-{day_number}"
    # ~~~~~
    
    # ~~~~~ Return Generated Values ~~~~~
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
    print("OBJECT LISTs:", object_list)
    print("Q:", query)
    if not object_list:
        print("FALSE")
        results = False
        region = ''
        division = ''
    else:
        print("TRUE")
        results = True
        region = object_list[0].district.region
        division = region.division


    print("Object List:", object_list)

    # ~~~~~ Return Generated Values ~~~~~
    context = {
        'object_list': object_list,
        'query': query,
        'results': results,
    }
    return render(request, 'opMetrics/search.html', context=context)
    # ~~~~~
# ~~~~~



# ~~~~~ Company ~~~~~
def Company(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    # ~~~~~ Initialize Calendar
    month = month.title()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)


    cal = HTMLCalendar().formatmonth(year, month_number)
    now = datetime.now()
    current_year = now.year

    time = now.strftime('%I:%M:%S %p')
    today = f"{now.year}-{now.month}-{now.day}"
    # ~~~~~day


    # ~~~~~ Return Generated Values ~~~~~
    context = {
        'year': year,
        'month': month,
        'month_number': month_number,
        'cal': cal,
        'current_year': current_year,
        'time': time,
        'today': today,
    }
    return render(request, 'opMetrics/company.html', context=context)
    # ~~~~~
# ~~~~~



def packagesperhour(request, level1='company', level2='all', sDatePPH=getDate(), eDatePPH=getDate()):
    if request.method == 'POST':
        sDate = request.POST.get("sDatePPH")
        eDate = request.POST.get("eDatePPH")
        sDatePPH = sDate
        eDatePPH = eDate
    
    else:
        sDatePPH = sDatePPH
        eDatePPH = eDatePPH

    level2Dict = getLevel2Dict(level1)
    level2List = list(level2Dict.keys())
    id = level2Dict.get(level2)

    dataRange = getOutputData(level1, id, sDatePPH, eDatePPH)
    print("OUTPUT:", dataRange)
    
    # ~~~~~ Calculate Sums & Averages ~~~~~
    # dataRange = packagesPerHour.objects.filter(location__district__region__id=2, date__range=[sDatePPH, eDatePPH])

    # ~~~~~ Return Generated Values ~~~~~
    context = {
        'dataRange': dataRange,
        'sDatePPH': sDatePPH,
        'eDatePPH': eDatePPH,

        'level1': level1,
        'level2': level2,
        'level2List': level2List,
    }
    return render(request, 'opMetrics/packagesPerHour.html', context=context)
    # ~~~~~
# ~~~~~
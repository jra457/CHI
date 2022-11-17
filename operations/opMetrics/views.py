from django.shortcuts import render
from datetime import datetime
from datetime import date
from datetime import timedelta
import calendar
from calendar import HTMLCalendar
from .forms import PackagesForm
from .models import Location

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




# ~~~~~ Packages Per Hour ~~~~~
def packagesPerHour(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
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
    return render(request, 'opMetrics/packagesperhour.html', context=context)
    # ~~~~~
# ~~~~~



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

    region = object_list[0].district.region
    division = region.division

    print("division:", division)

    # ~~~~~ Return Generated Values ~~~~~
    context = {
        'object_list': object_list,
        'region': region,
        'division': division,
    }
    return render(request, 'opMetrics/search.html', context=context)
    # ~~~~~
# ~~~~~
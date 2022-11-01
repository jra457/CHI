from django.urls import path
from . import views

# URLs:
#  ○ operationsMetrics/ (Home Page)
#  ○ operationsMetrics/packagesPerHour/
#  ○ operationsMetrics/DEX/
#  ○ operationsMetrics/volAvailStats/

# operationsMetrics
urlpatterns = [
    path('', views.operationsMetrics, name='operationsMetrics'),
    path('packagesPerHour', views.packagesPerHourView.as_view(),
    name='packagesperhour'),
]
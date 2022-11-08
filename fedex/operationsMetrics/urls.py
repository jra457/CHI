from django.urls import path
from . import views

# ~~~~~ URL List ~~~~~
#  ○ operationsMetrics/ (Home Page)
#  ○ operationsMetrics/packagesPerHour/
#  ○ operationsMetrics/DEX/
#  ○ operationsMetrics/volAvailStats/
# ~~~~~

# ~~~~~ URLs ~~~~~
urlpatterns = [
    path('', views.operationsMetrics, name='operationsMetrics'),
    
    path('packagesPerHour/', views.packagesPerHourListView.as_view(), name='packagesPerHour'),
    path('packagesPerHour/<int:pk>', views.packagesPerHourDetailView.as_view(), name='packagesPerHour-detail'),

    path('volumeAvailabilityStatus/', views.volumeAvailabilityStatusListView.as_view(), name='volumeAvailabilityStatus'),
    path('volumeAvailabilityStatus/<int:pk>', views.volumeAvailabilityStatusDetailView.as_view(), name='volumeAvailabilityStatus-detail'),

    path('dex/', views.DEXListView.as_view(), name='DEX'),
    path('dex/<int:pk>', views.DEXDetailView.as_view(), name='DEX-detail'),

    path('regions/', views.RegionListView.as_view(), name='regions'),
    path('regions/<int:pk>', views.RegionDetailView.as_view(), name='region-detail'),
    path('facility/', views.FacilityListView.as_view(), name='facility'),
    path('facility/<int:pk>', views.FacilityDetailView.as_view(), name='facility-detail'),
]
# ~~~~~
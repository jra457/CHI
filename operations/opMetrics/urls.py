from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:year>/<str:month>/', views.home, name='home'),
    path('packagesPerHour/', views.packagesperhour, name='packagesPerHour'),
    path('packagesPerHour/<str:level1>/<slug:sDatePPH>/<slug:eDatePPH>/', views.packagesperhour, name='packagesPerHour'),
    path('packagesPerHour/<str:level1>/<str:level2>/<slug:sDatePPH>/<slug:eDatePPH>/', views.packagesperhour, name='packagesPerHour'),
    path('dex/', views.DEX, name='dex'),
    path('vas/', views.VAS, name='vas'),
    path('company/', views.Company, name='company'),
    # path('addpackages/', views.addpackages, name='addpackages'),
    path('search/', views.Search, name='search'),

    path('division/<int:pk>', views.DivisionDetailView.as_view(), name='division-detail'),
    path('region/<int:pk>', views.RegionDetailView.as_view(), name='region-detail'),
    path('district/<int:pk>', views.DistrictDetailView.as_view(), name='district-detail'),
    path('location/<int:pk>', views.LocationDetailView.as_view(), name='location-detail'),

    path('login/', views.Login, name='login'),
]
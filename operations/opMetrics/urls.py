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
]
from django.urls import path,include
from .import views
from nyc import views
from .views import mutual_aid,borough
from rest_framework.urlpatterns import format_suffix_patterns
#URL CONFIGURATION
urlpatterns=[
    path('boroughs/', views.borough),
    path('boroughs/borough',views.borough_detail),
    path('mutualaids/boroughs/', views.mutual_aid),
    path('boroughs/mutualaids/', views.aid_detail),
    # path('mutualaids/<int:id>/boroughs',views.aid_detail)


]
urlpatterns=format_suffix_patterns(urlpatterns)
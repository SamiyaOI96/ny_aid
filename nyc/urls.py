from django.urls import path,include
from .import views
from nyc import views
from .views import mutual_aid,borough
from rest_framework.urlpatterns import format_suffix_patterns
#URL CONFIGURATION
urlpatterns=[
    path('boroughs/', views.borough),
    path('mutualaids/boroughs/', views.mutual_aid),

]
urlpatterns=format_suffix_patterns(urlpatterns)
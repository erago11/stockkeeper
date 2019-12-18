from django.urls import path,include
from . import views

app_name='stockkeepapp'

urlpatterns = [
    path('search',views.search,name='search'),
    path('searchresult',views.searchResult,name='searchresult'),
]

from django.urls import path,include
from . import views

app_name='stockkeepapp'

urlpatterns = [
    path('search',views.search,name='search'),
    path('mystocklist',views.my_stock_list,name='mystocklist'),
]

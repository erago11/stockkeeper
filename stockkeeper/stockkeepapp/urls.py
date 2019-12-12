from django.urls import path,include
from . import views

app_name='stockkeepapp'

urlpatterns = [
    path('',views.index,name='index'),
]

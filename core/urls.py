from django.urls import path
from .views import home,update,delete




urlpatterns=[
    path('',home),
    path('update/',update,name="update"),
    path('delete/',delete,name="delete"),

]
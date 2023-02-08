from django.urls import path, include
from .views import *

urlpatterns = [
    path('lift_details/', ElevatorNumber.as_view()),
    path('floor_details/', Floor.as_view()),
    path('req_to_each_lift/', ReqOfElevator.as_view()),
    path('lift_travel_history/', LiftHistory.as_view()),
]

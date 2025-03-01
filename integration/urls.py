from django.urls import path
from .views import PushSalesToAPI, PullLeadsFromAPI

urlpatterns = [
    path('push-sales/', PushSalesToAPI.as_view(), name='push-sales'),
    path('pull-leads/', PullLeadsFromAPI.as_view(), name='pull-leads'),
]

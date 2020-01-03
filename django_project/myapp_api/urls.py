from django.urls import path,include
from . import views
from rest_framework import routers
routers=routers.DefaultRouter()
routers.register('languages',views.languageview)

urlpatterns = [
    path('',include(routers.urls))

]

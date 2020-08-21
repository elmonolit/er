from testapp import views
from django.urls import path

urlpatterns = [
    path('', views.testapp, name='testapp')
]
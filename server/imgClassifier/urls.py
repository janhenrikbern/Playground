from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('classify', views.classifier, name='Classifier')
]

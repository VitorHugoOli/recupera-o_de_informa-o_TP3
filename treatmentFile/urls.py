from django.urls import path
from .views import *

urlpatterns = [
    path('', LerPDF.as_view(), name='lerPDF'),

]
from django.urls import path
from .views import *

urlpatterns = [
    path('uploadFile', insertText.as_view(), name='uploadFile'),
    path('search',search.as_view(),name='search'),
    path('texto',texto.as_view(),name='getTexto')

]
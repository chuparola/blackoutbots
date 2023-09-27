from django.urls import path
from core.views import index, sobre, contato

urlpatterns = [
    path('', index, name='index'),
    path('sobre-nós/', sobre, name='sobre'),
    path('contato/', contato, name='contato'),
]

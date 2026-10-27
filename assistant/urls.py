from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('api/generate/', views.generate_ai_response, name='generate_ai_response'),
]

from django.urls import path, include
from .views import PostAPI

urlpatterns = [
    path("<int:id>/", PostAPI)
]
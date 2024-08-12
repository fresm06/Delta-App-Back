from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FileUploadAPIView, PostAPI
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

# router = DefaultRouter()
# router.register(r'articles', ArticleViewSet)


urlpatterns = [
    path("<int:id>/", PostAPI), 
    path('upload-file/', FileUploadAPIView.as_view(), name='upload-file')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
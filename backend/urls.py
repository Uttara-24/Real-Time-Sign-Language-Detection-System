from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # Import the settings module
from django.conf.urls.static import static  
from detection.views import index
from detection import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('detection/', include('detection.urls')),
    path('detection/recognize_gesture_button/', views.recognize_gesture_button, name='recognize_gesture_button'),  
    path('',include('frontends.urls')),
    path('', index, name='index'),
]

if settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

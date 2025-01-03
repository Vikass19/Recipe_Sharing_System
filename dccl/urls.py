
from django.contrib import admin
from django.urls import include, path
from polls import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("", include("polls.urls")),
   
   
    path('',views.signup, name = "signup"),
    path("admin/", admin.site.urls),
    
    path("accounts/", include("django.contrib.auth.urls")),
    path('api-auth/', include('rest_framework.urls')),
]
  


# Add static files serving in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   
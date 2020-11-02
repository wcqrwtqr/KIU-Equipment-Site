from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(), name='home'),
    path('about/', views.AboutUs.as_view(), name='about'),
    path('thanks/', views.ThanksPage.as_view(), name='thanks'),
    path('FAR/', include('FAR.urls')),
    path('Jobs/', include('Jobs.urls')),
    path('Maintenance/', include('Maintenance.urls')),
    path('Employee/', include('Employee.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]


if settings.DEBUG:
    urlpatterns +=  static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

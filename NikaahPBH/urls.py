"""
URL configuration for NikaahPBH project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from PBH.views import create_profile, profile_created,get_profiles,update_profile,get_profile,index,contact_us

from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url

# from django.views.generic import TemplateView
print("hello urls")
print("hello")
urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('create-profile/', create_profile, name='create_profile'),
    path('profile-created/', profile_created, name='profile_created'),
    path('update-profile/',update_profile, name='update_profile'),
    path('profiles/', get_profiles, name='get_profiles'),
    path('profiles/<int:profile_id>/', get_profile, name='get_profile'),
    path('contact_us/', contact_us, name='contact us'),
    url(r'^media/(?p<path>.*)$',serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^media/(?p<path>.*)$',serve,{'document_root': settings.STATIC_ROOT}),
    # path('', TemplateView.as_view(template_name='NikaahPBH/index.html'), name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


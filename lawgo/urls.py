"""lawgo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^admin/', admin.site.urls),
    url(r'^podcast/', include('podcast.urls')),
    url(r'^podcast/(?P<show_id>[0-9]+)/episode/list', episode_list, name="episode_list"),
    #url(r'^dl', dl, name='dl')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns() + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# if getattr(settings, 'DEBUG', False):
#     urlpatterns += staticfiles_urlpatterns() + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

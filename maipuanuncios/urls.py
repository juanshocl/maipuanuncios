"""maipuanuncios URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from apps.home.views import HomeList
from apps.post.views import PostView
from apps.admins.views import Admins, Forms, AllList
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url



urlpatterns = [
    path('admin/', admin.site.urls),
    path('admins/', Admins.as_view(), name = 'admins'),
    path('admins/forms/', Forms.as_view(), name = 'forms'),
    path('admins/all/', AllList.as_view(), name = 'all'),
    path('', HomeList.as_view(), name='index'), #Vista estatica del index Vista Operativa
    path('post/', PostView.as_view(), name='post')
    #path('', IndexList.as_view(), name='index'), #Vista estatica del index Vista Operativa
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

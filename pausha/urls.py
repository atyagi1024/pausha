"""pausha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
import pausha.views
import callmgr.views


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # User Auth urls
    url(r'accounts/login/$', pausha.views.login),
    url(r'accounts/auth/$', pausha.views.auth_view),
    url(r'accounts/logout/$', pausha.views.logout),
    url(r'accounts/loggedin/$', pausha.views.loggedin),
    url(r'accounts/invalid/$', pausha.views.invalid),

    # Call Manager urls
    # We need to move these urls to specific apps using include() urlconf
    #url(r'^callmgr', include('callmgr.urls')),
    url(r'^callmgr/$', callmgr.views.home),
]

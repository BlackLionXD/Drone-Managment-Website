"""ohio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from . import views as pki_views
from django.urls import path

urlpatterns = [
    
    path('credentials/', pki_views.CredentialsList.as_view(), name='pki-credentials-list'),
    path('credentials/<uuid:pk>', pki_views.CredentialsDetail.as_view(), name='pki-credentials-detail'),
    path('auth_server_fullchain', pki_views.AuthServerFullChain.as_view(), name='auth-server-full-chain'),
    
]

"""
URL configuration for PruebaCorreos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from Correos import views
from Team import views as TeamViews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name = 'home'),
    path("undercontract/", views.undercontract, name='under contract'),
    path("undercontract/dates/", views.dates, name = 'tc dates'),
    path("undercontract/transactions", views.transactions, name = 'transacciones'),
    path("undercontract/transactions/<int:property_id>/", views.details, name = "detalles"),
    path("undercontract/transactions/<int:property_id>/closed",views.closed, name = "cerrado"),
    path("undercontract/congratulations/", views.congratulations, name = "congratulations"),
    path("undercontract/transactions/<int:property_id>/mails", views.emails, name = "7 correos"),
    path("undercontract/transactions/<int:property_id>/mails/send", views.emailsend, name = 'enviado'),
    path("agents/new/", TeamViews.AddAgent, name = "agregar"),
    path("agents/", TeamViews.Agents, name = "agentes")
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)

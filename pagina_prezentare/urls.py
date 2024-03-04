from django.contrib import admin
from django.urls import path, include
from pagina_prezentare import views
from . import views

urlpatterns = [

    path('pagina_prezentare/', include('pagina_prezentare.urls')),
    path('admin/', admin.site.urls)

]
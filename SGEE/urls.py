"""
URL configuration for SGEE project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from .views import estra_view, contact_view,eventos_view,estrategias_view,reportes_view,usuarios_view,informacion_profesoral_view,encuestas_view
from .views import sobrenos_view,testimonials_view
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('models/', include('data_models.urls')),
    path('', estra_view, name='pagina_principal'),
    path('contactenos/',contact_view,name='contactar'),
    path('estrategias/', estrategias_view, name='estrategias'),
    path('eventos/', eventos_view, name='eventos'),
    path('reportes/', reportes_view, name='reportes'),
    path('usuarios/', usuarios_view, name='usuarios'),
    path('informacion_profesoral/', informacion_profesoral_view, name='informacion_profesoral'),
    path('encuestas/', encuestas_view, name='encuestas'),
    path('sobrenos/',sobrenos_view, name='sobrenos'),
    path('testimonials/',testimonials_view, name='testimonials'),
    path('formularios_encuestas/', views.formularios_encuestas_view, name='formularios_encuestas'),
    path('formulario_estrategia/', views.formulario_estrategia_view, name='formulario_estrategia'),
    path('formulario_eventos/', views.formulario_eventos_view, name='formulario_eventos'),
    path('formulario_usuarios/', views.formulario_usuarios_view, name='formulario_usuarios'),
    path('formulario_reporte/', views.formulario_reporte_view, name='formulario_reporte'),
    path('formulario_informacion_pro/', views.formulario_informacion_pro_view, name='formulario_informacion_pro'),
    path('eliminar_estrategia/<int:estra_id>/', views.eliminarEstrategia, name='eliminar_estrategia'),
]
"""probando24"""
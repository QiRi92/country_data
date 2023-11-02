"""directory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from App import views 

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('format', views.format, name="format"),
    path('line/<str:directory_id>/graph', views.graph, name="graph"),
    path('line/<str:directory_id>/', views.line, name="line"),
    # Path to ADD directory
    path('add_directory', views.add_directory, name="add_directory"),
    # Path to View directory data individually
    path('directory/<str:directory_id>', views.directory, name="directory"),
    # Path to Edit employee
    path('edit_directory', views.edit_directory, name="edit_directory"),
    # Path to Delete employee
    path('delete_directory/<str:directory_id>', views.delete_directory, name="delete_directory")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

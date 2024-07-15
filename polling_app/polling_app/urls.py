"""
URL configuration for polling_app project.

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
from django.urls import include, path #include is used to include other URLconfs from another folder 

urlpatterns = [

    # Initial URL address is polls/ then under the polls folder, we will include the urls.py file
    path('polls/', include('polls.urls')), # This is the URL configuration for the polls app    

    # This is built-in from django. We do not need to think of the admin panel anymore
    # since Django has already created how we can manage our users and groups
    # we can still customize it using admin and modelsAdmin classes
    path('admin/', admin.site.urls),
]

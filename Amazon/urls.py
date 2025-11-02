"""
URL configuration for Amazon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path
# from booking import views
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('home/',views.home,name='home'),
#     path('register/',views.register,name='reg'),
#     path('about/',views.about,name='about'),
#     path('contact/',views.contact,name='contact'),
#     path('login/',views.login,name='login'),
#     path('welcome/',views.welcome,name='welcome'),
#     path('display/',views.display,name='display'),
#     path('logout/',views.logout,name='logout'),
#     path('update/',views.update,name='update'),
#     path('delete/',views.delete,name='delete'),
#     path('search/',views.search,name='search'),
# ]

#update code here---
"""
URL configuration for Amazon project.

The `urlpatterns` list routes URLs to views. 
For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from booking import views   # import your app's views

urlpatterns = [
    # Redirect base URL (example.com/) → /home
    path('', lambda request: redirect('home')),

    # Admin panel
    path('admin/', admin.site.urls),

    # Your app routes
    path('home/', views.home, name='home'),
    path('register/', views.register, name='reg'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('welcome/', views.welcome, name='welcome'),
    path('display/', views.display, name='display'),
    path('logout/', views.logout, name='logout'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
    path('search/', views.search, name='search'),
]

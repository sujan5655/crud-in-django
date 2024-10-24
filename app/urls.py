from django.contrib import admin
from django.urls import path
from app.views import profile,createProfile,updateProfile,deleteProfile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/',profile),
    path('createProfile/',createProfile),
    path('updateProfile/<int:id>/',updateProfile),
    path('deleteProfile/<int:id>/',deleteProfile),
]
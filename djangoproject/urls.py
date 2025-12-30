from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('onlinecourse.urls')),
]

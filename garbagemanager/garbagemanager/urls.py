
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),    
    path('', include('users.urls'), name= 'users'), # include your app urls.py here
    path('report/', include('reports.urls'), name = 'reports'), # include your app urls.py here
    # path('/collectors', include('collectors.urls'), name = 'collectors')
]
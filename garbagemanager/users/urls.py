from django.urls import path
from .views import RegisterUserView, RegisterCollectorView, CustomAuthToken
from .views import Home

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('register-collector/', RegisterCollectorView.as_view(), name='register-collector'),
    path('login/', CustomAuthToken.as_view(), name='login'),

    path('', Home.as_view()),
]
    
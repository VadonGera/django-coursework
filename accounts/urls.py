from django.urls import path

from .apps import AccountsConfig
from .views import RegisterView
# from rest_framework_simplejwt.views import TokenRefreshView

app_name = AccountsConfig.name

urlpatterns = [
    # path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('register/', RegisterView.as_view(), name='register'),
]
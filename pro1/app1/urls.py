from .views import *
from django.urls import path

urlpatterns = [
    path('', Home),
    path('Register-Page', Register),
    path('Login-Page', Login),
    path('Logout', Logout),
    path('DashBoard', DashBoard),
    path('DashTable', DataTable),
    path('Edit/<int:id>', Edit),
    path('Delete/<int:user_id>', Delete),
    path('Forget/<int:id>', Forget),
    path('Otp/<int:id>', Otp)
]
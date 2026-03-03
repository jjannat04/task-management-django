from django.urls import path
from tasks.views import manager_dashboard, user_dashboard, test
urlpatterns = [

    path('test/', test),
    path('manager-dashboard/', manager_dashboard),
    path('user-dashboard/', user_dashboard)
]
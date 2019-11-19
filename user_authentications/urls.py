from django.urls import path
from . import views

urlpatterns = [
   path('login/',views.user_login,name='login'),
   path('register/',views.register_user,name='register'),
   path('ajax/validate_username/', views.validate_username, name='validate_username'),
   path('logout/', views.logout_view,name='logout'),
   path('dashboard/',views.user_dashboard,name='dashboard'),
   path('dashboard/my-adds',views.my_add,name='my_add'),
]

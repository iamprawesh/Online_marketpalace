from django.urls import path
from . import views

urlpatterns = [
   path('login/',views.user_login,name='login'),
   path('register/',views.register_user,name='register'),
   path('ajax/validate_username/', views.validate_username, name='validate_username'),
   path('logout/', views.logout_view,name='logout'),
   path('dashboard/',views.user_dashboard,name='dashboard'),
   path('dashboard/my-adds',views.my_add,name='my_add'),
   path('dashboard/order-requests',views.order_request,name='order_request'),
   path('dashboard/feature_add',views.feature_add,name='feature_your_add'),
   path('delete/<pk>', views.ContactDeleteView.as_view(), name='delete_contact'),


]

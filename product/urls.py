from django.urls import path
from . import views

urlpatterns = [
    path('',views.productlist,name='home'),
    path('search',views.search,name='search'),

    path('add/', views.ProductCreateView.as_view(), name='product_add'),
    path('update/<pk>', views.ProductUpdateView.as_view(), name='product_update'),
    path('delete/<pk>', views.ProductDeleteView.as_view(), name='product_delete'),

    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
    # path('all-products/', views.all_products, name='all_products'),
    path('all-products/', views.all_items, name='all_products'),

    path('<int:p_id><str:slug>/',views.product_detail,name='pro_details'),
    path('category/<str:slug>/',views.category_detail,name='category_detail'),
]

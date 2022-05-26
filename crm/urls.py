from django.urls import include, path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    #product url
    path('products/',views.products,name='product'),
    path('add_products/',views.add_product,name='add_product'),
    path('edit_products/<str:pk>',views.edit_product,name='edit_product'),
    path('delete_products/<str:pk>',views.delete_product,name='delete_product'),
    
    #order url
    path('create_order/',views.create_order,name='create_order'),
    path('order_list/',views.order_list,name='order_list'),
    path('update_order/<str:pk>',views.update_order,name='update_order'),
    path('delete_order/<str:pk>',views.delete_order,name='delete_order'),
    #customer url
    path('customers-list',views.customers_list,name='customers_list'),
    path('customer_dashboard/<str:pk>',views.customers,name='customer'),
]

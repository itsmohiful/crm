from django.urls import include, path

from . import views

urlpatterns = [
    path('',views.home,name='home'),

    path('products/',views.products,name='product'),
    path('add_products/',views.add_product,name='add_product'),
    path('edit_products/<str:pk>',views.edit_product,name='edit_product'),
    path('delete_products/<str:pk>',views.delete_product,name='delete_product'),

    path('customers/<str:pk_test>',views.customers,name='customer'),

    path('create_order_inline/<str:pk>',views.createorderinlineset,
    name='create_order_inline'),

    path('create_order/',views.createorder,name='create_order'),

    path('order_list/',views.order_list,name='order_list'),

    path('update_order/<str:pk>',views.updateorder,name='update_order'),

    path('delete_order/<str:pk>',views.deleteorder,name='delete_order'),

    path('customers-list',views.customers_list,name='customers-list'),
]

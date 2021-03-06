from distutils.log import log

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms import inlineformset_factory
from django.shortcuts import redirect, render
from users.decorators import user_permission

from .filters import *
from .forms import OrderForm, ProductForm

# def home(request):
#     return render(request,'crm/home.html')


#home view 
@login_required(login_url='login')
@user_permission
def home(request):
    customers = User.objects.all()
    orders = Order.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    out_for_delivery = orders.filter(status='Out For Delivery').count()

    context = {
        'customers' : customers,
        'orders' : orders,
        'total_customers' : total_customers,
        'total_orders' : total_orders,
        'delivered' : delivered,
        'pending' : pending,
        'out_for_delivery' : out_for_delivery,
    }
    return render(request,'crm/home.html',context)



#show all customers
def customers_list(request):
    customers = User.objects.all()
    context = {
        'customers' : customers,
    }

    return render(request,'crm/all_customers.html',context)


#customer dashboard
def customer(request,pk):
    customer = User.objects.get(id=pk)
    orders = customer.order_set.all()
    order_count = orders.count()

    #filtering_order
    order_filter = OrderFilter(request.GET, queryset=orders)
    orders = order_filter.qs

    context = {
        'customer' : customer,
        'orders' : orders,
        'order_count' : order_count,
        'order_filter' : order_filter,
    }

    return render(request,'crm/customer.html',context)


#every customer dashboard
def customer_page(request):
    customer_id = request.user.id
    customer = User.objects.filter(id=customer_id).first()
    orders = customer.order_set.all()
    order_count = orders.count()

    #filtering_order
    order_filter = OrderFilter(request.GET, queryset = orders)
    orders = order_filter.qs

    context = {
        'customer' : customer,
        'orders' : orders,
        'order_count' : order_count,
        'order_filter' : order_filter,
    }

    return render(request,'crm/customer_page.html',context)



#product view
def products(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request,'crm/products.html',context)


#add products
@login_required(login_url='login')
def add_product(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Successfully Product Added')
            return redirect('product')

    context = {
        'form' : form
    }

    return render(request,'crm/add_product.html',context)


#edit products
def edit_product(request,pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance = product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request,f'Product Updated')
            return redirect('product')

    context = {
        'form' : form
    }

    return render(request,'crm/edit_product.html',context)


#delete product 
def delete_product(request,pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request,f'Product Deleted')
        return redirect('product')
    context = {
        'item' : product,
    }
    return render(request,'crm/delete_product.html',context)


#order list
def order_list(request):
    all_orders = Order.objects.order_by("-date_created")
    order_count = all_orders.count()

    #filtering_order
    order_Filter = OrderFilter(request.GET,queryset=all_orders)
    all_orders = order_Filter.qs

    context = {
        'all_orders' : all_orders,
        'order_count' : order_count,
        'order_filter' : order_Filter,
    }

    return render(request,'crm/order_list.html',context)


@login_required(login_url='login')
#create order view
def create_order(request):
    #customer = Customer.objects.get(id=pk)
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user
            order.save()
            messages.success(request,f'Successfully Order Created')
            return redirect('customer_page')
    context = {
        'form' : form,
    }
    return render(request,'crm/order_form.html',context)



#update order
def update_order(request,pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance = order)

    if request.method == 'POST':
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            messages.success(request,f'Successfully Order Updated')
            return redirect('order_list')

    context = {
        'form' : form,
    }

    return render(request, 'crm/update_order.html',context)


#delete order view
def delete_order(request,pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        messages.success(request,f'Successfully Order Deleted')
        return redirect('order_list')
    context = {
        'item' : order,
    }
    return render(request,'crm/delete_order.html',context)

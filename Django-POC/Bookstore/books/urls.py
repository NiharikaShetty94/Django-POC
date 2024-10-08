from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    book_list,
    book_detail,
    book_create,
    book_update,
    book_delete,
    add_book,
    register,
    user_logout,
    add_to_cart,
    view_cart,
    remove_from_cart,
    set_language,
    user_profile,
    delete_book,
    admin_dashboard,
    place_order,
    order_success,
    view_orders,
)

urlpatterns = [
    path('', book_list, name='book_list'),
    path('book/<int:pk>/', book_detail, name='book_detail'),
    path('book/create/', book_create, name='book_create'),
    path('book/delete/<int:pk>/', book_delete, name='book_delete'),
    path('add-book/', add_book, name='add_book'),
    path('register/', register, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='books/login.html'), name='login'),
    path('logout/', user_logout, name='logout'),
    path('add-to-cart/<int:book_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='view_cart'),
    path('remove-from-cart/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),
    path('set-language/', set_language, name='set_language'),
    path('books/<int:pk>/edit/', book_update, name='book_update'),
    path('accounts/profile/', user_profile, name='user_profile'),
    path('admin/dashboard/', admin_dashboard, name='admin_dashboard'),
    path('delete-book/<int:book_id>/', delete_book, name='delete_book'),
    path('order/', place_order, name='place_order'),
    path('order/success/', order_success, name='order_success'),
    path('admin/orders/', view_orders, name='view_orders'),

]

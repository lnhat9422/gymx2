# services/urls.py (Bị lỗi)
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.service_view, name='services'),
    path('dich-vu/admin/', views.admin_login, name='admin_login'),  # <-- Đăng nhập tùy chỉnh

    # 2. Trang Đăng xuất
    path('dich-vu/admin/logout/', auth_views.LogoutView.as_view(next_page='admin_login'), name='admin_logout'),
    # Đăng xuất và chuyển hướng về trang login

    # 3. Các chức năng CRUD
    path('dich-vu/admin/services/', views.service_list, name='admin_service_list'),
    path('dich-vu/admin/services/add/', views.add_service, name='admin_add_service'),
    path('dich-vu/admin/services/edit/<int:pk>/', views.edit_service, name='admin_edit_service'),
    path('dich-vu/admin/services/delete/<int:pk>/', views.delete_service, name='admin_delete_service'),
]
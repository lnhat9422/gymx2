# Ví dụ: trong my_app/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout # Import các hàm Auth
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Service
from .forms import ServiceForm
from django.contrib.auth.forms import AuthenticationForm # Dùng form đăng nhập mặc định
def service_view(request):
    """Render trang giới thiệu các dịch vụ (Gym, Yoga, Dance)."""
    # Bạn có thể thêm context data nếu cần thiết
    context = {
        'page_title': 'Dịch Vụ Của GymX'
    }
    return render(request, 'services\service_type_detail.html', context)


# --- Hàm Quản lý Danh sách Dịch vụ (Read & Search) ---
@login_required
def service_list(request):
    services = Service.objects.all()
    query = request.GET.get('q')

    if query:
        # Tìm kiếm theo Tên DV hoặc Mô tả
        services = services.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        ).distinct()

    context = {
        'services': services,
        'query': query
    }
    return render(request, 'admin/service_list.html', context)


# --- Hàm Thêm Dịch vụ (Create) ---
@login_required
def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save()
            # Trả về trang danh sách sau khi lưu
            return redirect('admin_service_list')
    else:
        form = ServiceForm()

    context = {
        'form': form,
        'action': 'Thêm mới'
    }
    return render(request, 'admin/service_form.html', context)


# --- Hàm Sửa Dịch vụ (Update) ---
@login_required
def edit_service(request, pk):
    service = get_object_or_404(Service, pk=pk)

    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            # Trả về trang danh sách sau khi lưu
            return redirect('admin_service_list')
    else:
        form = ServiceForm(instance=service)

    context = {
        'form': form,
        'service': service,
        'action': 'Cập nhật'
    }
    return render(request, 'admin/service_form.html', context)


# --- Hàm Xóa Dịch vụ (Delete) ---
@login_required
def delete_service(request, pk):
    service = get_object_or_404(Service, pk=pk)

    # Yêu cầu xóa chỉ xử lý qua POST (bấm nút)
    if request.method == 'POST':
        service.delete()
        return redirect('admin_service_list')

    # Trường hợp không phải POST, hiển thị trang xác nhận (tùy chọn)
    return redirect('admin_service_list')


# --- View Đăng nhập Tùy chỉnh ---
def admin_login(request):
    if request.user.is_authenticated:
        # Nếu đã đăng nhập, chuyển hướng đến trang quản lý dịch vụ
        return redirect('admin_service_list')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                # CHUYỂN HƯỚNG VỀ DANH SÁCH DỊCH VỤ
                return redirect('admin_service_list')
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
        'page_title': 'Đăng nhập Quản trị'
    }
    return render(request, 'admin/admin_login.html', context)
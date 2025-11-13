from django.shortcuts import render
def home_view(request):
    """Render trang chủ sử dụng home.html."""
    return render(request, 'home.html')
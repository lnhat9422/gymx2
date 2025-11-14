
from django.db import models
from django.urls import reverse

class ServiceType(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='services/types/', blank=True)

    class Meta:
        verbose_name = "Loại dịch vụ"
        verbose_name_plural = "Các loại dịch vụ"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('services:type_detail', args=[self.slug])

class Service(models.Model):
    # MaDV tự động tạo (Primary Key)
    service_id = models.AutoField(
        primary_key=True,
        verbose_name="Mã DV"
    )

    name = models.CharField(
        max_length=100,
        verbose_name="Tên Dịch vụ",
        unique=True
    )

    description = models.TextField(
        verbose_name="Mô tả chi tiết"
    )

    # Thêm trường này nếu bạn muốn hiển thị ảnh đại diện cho dịch vụ trong quản lý
    image = models.ImageField(
        upload_to='service/',
        verbose_name="Ảnh đại diện",
        null=True,
        blank=True
    )
    STATUS_CHOICES = (
        ('draft', 'Bản nháp (Ẩn)'),
        ('published', 'Công khai (Hiện)'),
        ('archived', 'Lưu trữ'),
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft',  # Mặc định là Bản nháp
        verbose_name='Trạng thái hiển thị'
    )
    # Thêm trường order để sắp xếp (Tùy chọn)
    display_order = models.IntegerField(default=0, verbose_name='Thứ tự hiển thị')

    class Meta:
        verbose_name = "Dịch vụ"
        verbose_name_plural = "Dịch vụ"
        ordering = ['service_id']

    def __str__(self):
        return self.name


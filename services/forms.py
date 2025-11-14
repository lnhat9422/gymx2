from django import forms
from django import forms
from .models import Service


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        # service_id là AutoField nên loại bỏ
        fields = ['name', 'description', 'image','status', 'display_order']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'status': forms.Select(choices=Service.STATUS_CHOICES),
        }
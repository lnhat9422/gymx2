from .models import ServiceType

def service_types(request):
    return {'service_types': ServiceType.objects.all()}

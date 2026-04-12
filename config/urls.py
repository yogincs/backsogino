from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path


def root_view(request):
    return JsonResponse({
        'message': 'Welcome to sogino-backend. Use /api/email/ or /api/suggestion/',
        'routes': ['admin/', 'api/email/', 'api/suggestion/'],
    })

urlpatterns = [
    path('', root_view, name='root'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]

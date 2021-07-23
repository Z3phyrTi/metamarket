from django.urls import path,include
urlpatterns = [
    path('categoria/', include('api.apicategoria.urls')),
    path('cuentas/', include('api.apicuentas.urls')),
    path('producto/', include('api.apiproducto.urls'))
]
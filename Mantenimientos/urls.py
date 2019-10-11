from django.urls import path
from Mantenimientos.views import *

urlpatterns = [	path('auten/', autentificar, name="autentificar"),
				path('inicio/', Inicio_view),
				path('AgregarHeart_ajax/', AgregarHeart_ajax_view),
				path('Bienvenida/', Bienvenida_view),
]

from django.urls import path, include
from .views import IndexView 

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    
    # path('Cadastro/', include('cadastro.urls'),name='cadastro'),
    
]

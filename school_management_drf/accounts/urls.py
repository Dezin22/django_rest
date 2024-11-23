from django.urls import path
from .views import CustomUserViewSet, CustomLoginView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Criando o roteador para o ModelViewSet do CustomUser
router = DefaultRouter()
router.register('users', CustomUserViewSet)

urlpatterns = [
    # Definindo a URL do login (obter tokens)
    path('login/', CustomLoginView.as_view(), name='login'),  # Essa view vai gerar o access e refresh token
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Para refrescar o token de acesso
]

# Adicionando as URLs do roteador para o CustomUser
urlpatterns += router.urls

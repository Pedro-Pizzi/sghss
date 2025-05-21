from django.urls import include, path
from rest_framework import routers
from hospital import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register(r'pacientes', views.PacienteViewSet, basename='pacientes')
router.register(r'consultas', views.ConsultaViewSet, basename='consultas')
router.register(r'profissionais', views.ProfissionalViewSet, basename='profissionais')
router.register(r'leitos', views.LeitoViewSet, basename='leitos')
router.register(r'receitas', views.ReceitaViewSet, basename='receitas')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]
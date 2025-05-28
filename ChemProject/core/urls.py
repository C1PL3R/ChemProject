from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.conf.urls import handler400, handler403, handler404, handler500
from rest_framework import routers
from .views import MoluculeAPIView
from .views_classes.auth_view import AuthView, AuthPostView
from .views_classes.send_molecule_data_views import SendFormulaView, SendNameView


handler404 = 'your_project.views.custom_page_not_found'
handler500 = 'your_project.views.custom_error_view'

router = routers.DefaultRouter()
router.register(r'molecule-history', MoluculeAPIView, basename='molecule-history')

urlpatterns = [
    path('', views.index, name='index'),
    path('google45b8458dd0908687.html', views.copyright_for_google),
    path('auth/', views.auth, name='auth'),
    path('my-ip/', views.my_ip_view),
    path('about/', views.about, name='about'),
    path('what_are_smiles/', views.what_are_smiles, name="what_are_smiles"),
    path('logout/', views.logout, name='logout'),
    path('auth/', AuthView.as_view(), name='auth'),
    path('auth-post/', AuthPostView.as_view()),
    path('send-name/', SendNameView.as_view(), name="send-name"),
    path('send-formula/', SendFormulaView.as_view(), name='send-formula'),
    # Chem Apps
    path('visualizer/', include('ChemVisualizer.urls')),
    path('chat/', include('ChemChat.urls')),
    path('document/', include('ChemDocument.urls')),
    path('api/', include(router.urls)),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
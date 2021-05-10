from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from rest_framework.routers import DefaultRouter
from .api import MessageModelViewSet, UserModelViewSet
from .views import signup, logout_, home, login_
from django.contrib.auth import views as auth_views

router = DefaultRouter()
router.register(r'message', MessageModelViewSet, basename='message-api')
router.register(r'user', UserModelViewSet, basename='user-api')

urlpatterns = [
    path(r'api/v1/', include(router.urls)),
    # path('', login_required(
    #     TemplateView.as_view(template_name='core/chat.html')), name='home'),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    path('home/', home, name='home'),
    path('signup/', signup, name='signup'),
    path('logout/', logout_, name='logout'),
    path('', login_, name='login'),
]




from django.urls import path
from rest_framework import routers

from .apiviews.public import ListsAPIView

from .viewsets.person import PersonViewSet
from .viewsets.user import UserViewSet
from .viewsets.role import RoleViewSet
from .viewsets.module import ModuleViewSet
from .viewsets.view import ViewViewSet
from .viewsets.user_role import UserRoleViewSet
from .viewsets.module_role import ModuleRoleViewSet
from .viewsets.module_view import ModuleViewViewSet

from .apiviews.login import LoginAPIView
from .apiviews.access_views import LoginViewsAPIView
from .apiviews.views_system import ViewsInfoAPIView
from .apiviews.audit import AuditAPIView
from .apiviews.practices import PracticesAPIView
from .apiviews.user_role import UserRoleInactiveAPIView

router = routers.SimpleRouter()
router.register(r'person', PersonViewSet, basename='person')
router.register(r'user', UserViewSet, basename='user')
router.register(r'role', RoleViewSet, basename='role')
router.register(r'module', ModuleViewSet, basename='module')
router.register(r'view', ViewViewSet, basename='view')
router.register(r'user-role', UserRoleViewSet, basename='user-role')
router.register(r'module-role', ModuleRoleViewSet, basename='module-role')
router.register(r'module-view', ModuleViewViewSet, basename='module-view')
urlpatterns = router.urls + [
    path("lists/", ListsAPIView.as_view(), name="public-lists"),
]

urlpatterns = urlpatterns + [
    path("login/", LoginAPIView.as_view(), name="login"),
    path("login-views/", LoginViewsAPIView.as_view(), name="login-views"),
    path("views-system/<str:state>/", ViewsInfoAPIView.as_view(), name="views-system"),
    path("audit/<str:user>/", AuditAPIView.as_view(), name="audit"),
    path("practices/", PracticesAPIView.as_view(), name="practices"),
    path("users-with-inactive-roles/", UserRoleInactiveAPIView.as_view(), name="users-with-inactive-roles"),
]

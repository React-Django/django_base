from rest_framework.routers import DefaultRouter

from rest_framework.routers import DefaultRouter
from test_app.views import TestModelViewSet

router = DefaultRouter()
router.register('testmodel', TestModelViewSet)

urlpatterns = [] + router.urls

from dynamic_rest import routers

from app.viewsets import PersonViewSet

router = routers.DynamicRouter()

router.register(r'persons', PersonViewSet)
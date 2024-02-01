from app.viewsets import PersonViewSet
from dynamic_rest import routers

router = routers.DynamicRouter()

router.register(r'persons', PersonViewSet)

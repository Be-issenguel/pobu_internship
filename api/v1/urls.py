from rest_framework.routers import SimpleRouter
from .subscription.responsible import ResponsibleViewSet

router = SimpleRouter()

router.register(r'responsible', ResponsibleViewSet)

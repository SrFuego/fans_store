# Python imports


# Django imports


# Third party apps imports


# Local imports
from .viewsets import OrderViewSet


# Create your routers here.
orders = (
    (r"orders", OrderViewSet),
)

# Python imports


# Django imports


# Third party apps imports


# Local imports
from .viewsets import KindViewSet, ProductViewSet


# Create your routers here.
products = (
    (r"kinds", KindViewSet),
    (r"products", ProductViewSet),
)

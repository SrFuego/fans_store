# Python imports


# Django imports


# Third party apps imports


# Local imports
from .viewsets import KindViewSet


# Create your routers here.
products = (
    (r"kinds", KindViewSet),
)

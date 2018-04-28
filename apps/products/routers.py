# Python imports


# Django imports


# Third party apps imports


# Local imports
from .viewsets import (
    KindViewSet, MostViewedViewSet, NewersViewSet, ProductViewSet)


# Create your routers here.
products = (
    (r"kinds", KindViewSet),
    (r"most_viewed", MostViewedViewSet),
    (r"newers", NewersViewSet),
    (r"products", ProductViewSet),
)

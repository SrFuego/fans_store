# Python imports


# Django imports


# Third party apps imports


# Local imports
from .viewsets import (
    CollectionViewSet, ColorViewSet, KindViewSet, MostViewedViewSet,
    NewersViewSet, ProductViewSet, SizeViewSet,)


# Create your routers here.
products = (
    (r"collections", CollectionViewSet),
    (r"colors", ColorViewSet),
    (r"kinds", KindViewSet),
    (r"most_viewed", MostViewedViewSet),
    (r"newers", NewersViewSet),
    (r"products", ProductViewSet),
    (r"sizes", SizeViewSet),
)

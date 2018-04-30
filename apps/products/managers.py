# Python imports


# Django imports
from django.db import models


# Third party apps imports


# Local imports


# Create your managers here.
class ProductManager(models.QuerySet):

    def most_viewed(self):
        return self.all().order_by("-views")[:6]

    def newers(self):
        return self.all().order_by("-created")[:6]

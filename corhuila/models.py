from django.db import models
from safedelete.models import SafeDeleteModel, SOFT_DELETE_CASCADE

# Create your models here.
class BaseModel(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True
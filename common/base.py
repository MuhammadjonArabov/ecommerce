import uuid
from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    guid = models.CharField(max_length=225, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

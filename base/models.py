from django.db import models
import uuid
# Create your models here.
class BaseModel(models.Model):
    uid=models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    created_at=models.DateTimeField(auto_now_add=True)# time is created when created

    update_at=models.DateTimeField(auto_now=True)# time is updated at evry save

    class Meta:
        abstract=True


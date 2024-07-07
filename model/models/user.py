from model.models.base import BaseModel
from django.db import models

class User(BaseModel):
    name = models.CharField(max_length=255)
    email = models.CharField(db_index=True, unique=True, max_length=255)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    class Meta:
        db_table = 'users'

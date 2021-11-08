from ninja import ModelSchema, Schema
from .models import Task


class TaskSchema(ModelSchema):
    class Config:
        model = Task
        model_fields = ['status', 'description']
from typing import List
from ninja import NinjaAPI
from ninja.security import django_auth
from .schema import TaskSchema
from .models import Task



api = NinjaAPI()

@api.get('/to-do/{task_id}', response={200: TaskSchema})
def individual_tas(request, task_id: int):
    todo = Task.objects.get(pk=task_id)
    return 200, todo


@api.get('/to-do', response=List[TaskSchema])
def all_task(request):
    todo = Task.objects.all()
    return 200, todo


@api.post('/to-do', response={201: TaskSchema})
def create_task(request, task: TaskSchema):
    task = Task.objects.create(**task.dict())
    return task

@api.put('/to-do/{task_id}', response={200: TaskSchema})
def change_task(request, task_id: int, data: TaskSchema):
    task = Task.objects.get(pk=task_id)
    for attribute, value in data.dict().items():
        setattr(task, attribute, value)
    task.save()
    return 200, task
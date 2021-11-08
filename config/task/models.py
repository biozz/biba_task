from django.db import models


class Task(models.Model):
    TODO = 'todo'
    DONE = 'done'

    STATUS_CHOISES = (
        (TODO, 'Todo'),
        (DONE, 'Done')
    )

    description = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS_CHOISES, default=TODO)

    def __str__(self):
        return self.description
    
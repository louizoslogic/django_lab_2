from django.db import models


class Groceries(models.Model):

    description = models.CharField(max_length=200)
    createdate = models.DateTimeField(null=True, blank=True)
    completedate = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False, editable=True)

    def __str__(self):
        return self.description

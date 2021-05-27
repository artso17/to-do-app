from django.db import models

# Create your models here.


class ListToDo(models.Model):
    judul = models.CharField(max_length=200)
    published = models.DateTimeField(
        auto_now_add=True, blank=True, null=True, editable=False)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.judul

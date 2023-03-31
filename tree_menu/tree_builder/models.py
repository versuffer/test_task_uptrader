from django.db import models
from django.utils.text import slugify


class Node(models.Model):
    menu_name = models.CharField(max_length=255, default='first')
    option = models.CharField(max_length=255)
    parent = models.ForeignKey(
        'self', related_name='children', on_delete=models.CASCADE, null=True, blank=True
    )
    url_name = models.CharField(
        max_length=255, null=True, blank=True, unique=True
    )

    def __str__(self):
        return f'node_id: {self.id}'

    def save(self):
        if not self.url_name:
            self.url_name = hash(f'{self.id}_{self.menu_name}_{self.option}')
        else:
            self.url_name = slugify(self.url_name)
        super().save()

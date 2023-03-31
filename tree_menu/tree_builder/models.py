from django.db import models


class Node(models.Model):
    menu_name = models.CharField(max_length=255, default='first')
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, null=True, blank=True)
    option = models.CharField(max_length=255)

    def __str__(self):
        return f'node_id: {self.id}'

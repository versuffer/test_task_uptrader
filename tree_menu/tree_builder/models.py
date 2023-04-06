from django.db import models
from django.utils.text import slugify


class Node(models.Model):
    menu_name = models.CharField(max_length=255, default="first_menu")
    option = models.CharField(max_length=255, default="DEFAULT_OPTION", unique=True)
    parent = models.ForeignKey(
        "self", related_name="children", on_delete=models.CASCADE, null=True, blank=True
    )
    slug = models.SlugField()

    def __str__(self):
        return f"node_id: {self.id}; option: {self.option}; menu_name: {self.menu_name}"

    def save(self, *args, **kwargs):
        if not self.parent:
            self.slug = f"{self.menu_name}-root-node"
            self.option = self.menu_name
        else:
            self.menu_name = self.parent.menu_name
            self.slug = self.option
        self.slug = slugify(self.slug)
        super().save(*args, **kwargs)

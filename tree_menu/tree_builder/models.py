from django.db import models
from django.utils.text import slugify


class Node(models.Model):
    menu_name = models.CharField(max_length=255, default="first")
    option = models.CharField(max_length=255, default="DEFAULT_OPTION", unique=False)
    parent = models.ForeignKey(
        "self", related_name="children", on_delete=models.CASCADE, null=True, blank=True
    )
    url_name = models.CharField(max_length=200, null=True, blank=True, unique=True)

    def __str__(self):
        return f"node_id: {self.id}; option: {self.option}; menu_name: {self.menu_name}"

    def save(self):
        if not self.parent:
            self.url_name = f"{self.menu_name}-root-node"
        else:
            self.menu_name = self.parent.menu_name

        if not self.url_name:
            self.url_name = hash(f"{self.id}_{self.menu_name}_{self.option}")

        self.url_name = slugify(self.url_name)
        super().save()

# Generated by Django 4.1.7 on 2023-03-30 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree_builder', '0006_node_menu_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='node',
            name='menu_id',
        ),
        migrations.AddField(
            model_name='node',
            name='menu_name',
            field=models.CharField(default='first', max_length=255),
        ),
    ]

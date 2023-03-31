# Generated by Django 4.1.7 on 2023-03-31 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tree_builder', '0007_remove_node_menu_id_node_menu_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='tree_builder.node'),
        ),
    ]

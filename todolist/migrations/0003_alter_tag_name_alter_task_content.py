# Generated by Django 5.1.1 on 2024-09-25 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todolist", "0002_remove_task_tags_task_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tag",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="task",
            name="content",
            field=models.TextField(unique=True),
        ),
    ]
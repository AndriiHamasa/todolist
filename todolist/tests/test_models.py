from django.db import IntegrityError
from django.utils import timezone

from django.test import TestCase

from todolist.models import Task, Tag


class ModelsTestCase(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="test tag")
        self.task = Task.objects.create(
            content="test task",
            deadline=timezone.now() + timezone.timedelta(days=7),
            is_completed=False,
        )
        self.task.tags.add(self.tag)
        self.task.save()

    def test_task_str_method(self):
        return self.assertEqual(str(self.task), self.task.content)

    def test_tag_str_method(self):
        return self.assertEqual(str(self.tag), self.tag.name)

    def test_task_content_unique(self):
        with self.assertRaises(IntegrityError):
            task = Task.objects.create(
                content="test task",
                deadline=timezone.now() + timezone.timedelta(days=7),
                is_completed=False,
            )
            task.tags.add(self.tag)
            task.save()

    def test_tag_name_unique(self):
        with self.assertRaises(IntegrityError):
            Tag.objects.create(name="test tag")

    def test_many_to_many_relationship(self):
        tag = Tag.objects.create(name="test tag second")
        self.task.tags.add(tag)
        self.assertEqual(self.task.tags.count(), 2)

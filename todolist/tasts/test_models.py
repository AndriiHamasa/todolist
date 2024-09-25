from django.utils import timezone

from django.test import TestCase

from todolist.models import Task, Tag


class ModelsTestCase(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name='test tag')
        self.task = Task.objects.create(
            content="test task",
            deadline=timezone.now() + timezone.timedelta(days=7),
            is_completed=False
        )
        self.task.tags.add(self.tag)
        self.task.save()

    def test_task_str_method(self):
        return self.assertEqual(str(self.task), self.task.content)

    def test_tag_str_method(self):
        return self.assertEqual(str(self.tag), self.tag.name)
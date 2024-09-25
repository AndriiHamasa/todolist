from django.test import TestCase
from django.urls import reverse

from todolist.models import Tag, Task

TASK_LIST_URL = reverse("todolist:task-list")
TAG_LIST_URL = reverse("todolist:tag-list")


class TaskTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="test tag")

        self.task = Task.objects.create(
            content="test content", deadline="2024-09-25 13:04:06"
        )
        self.task.tags.add(self.tag)
        self.task.save()

    def test_retrieve_task_list(self):
        res = self.client.get(TASK_LIST_URL)
        task_list = Task.objects.all()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(list(res.context["task_list"]), list(task_list))
        self.assertTemplateUsed(res, "todolist/task_list.html")

    def test_task_create(self):
        form_data = {
            "content": "test content second",
            "deadline": "2024-09-26 13:04:06",
            "tags": (self.tag.id,),
        }

        response = self.client.post(reverse("todolist:task-create"), form_data)
        new_task = Task.objects.get(content=form_data["content"])

        self.assertEqual(new_task.content, form_data["content"])
        self.assertRedirects(response, reverse("todolist:task-list"))

    def test_task_delete(self):
        new_task = Task.objects.create(
            content="test content_new", deadline="2024-09-25 13:04:06"
        )
        new_task.tags.add(self.tag)
        new_task.save()

        response = self.client.post(
            reverse("todolist:task-delete", kwargs={"pk": new_task.id})
        )

        self.assertTrue(len(Task.objects.filter(content="test content_new")) == 0)
        self.assertRedirects(response, reverse("todolist:task-list"))


class TagTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="test tag")

    def test_retrieve_tag_list(self):
        res = self.client.get(TAG_LIST_URL)
        tag_list = Tag.objects.all()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(list(res.context["tag_list"]), list(tag_list))
        self.assertTemplateUsed(res, "todolist/tag_list.html")

    def test_tag_create(self):
        form_data = {
            "name": "test tag second",
        }

        response = self.client.post(reverse("todolist:tag-create"), form_data)
        new_tag = Tag.objects.get(name=form_data["name"])

        self.assertEqual(new_tag.name, form_data["name"])
        self.assertRedirects(response, reverse("todolist:tag-list"))

    def test_tag_delete(self):
        new_tag = Tag.objects.create(name="test tag new")

        response = self.client.post(
            reverse("todolist:tag-delete", kwargs={"pk": new_tag.id})
        )

        self.assertTrue(len(Tag.objects.filter(name="test tag new")) == 0)
        self.assertRedirects(response, reverse("todolist:tag-list"))

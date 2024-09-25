from django import forms
from django.test import TestCase

from todolist.forms import TaskForm
from todolist.models import Tag


class FormTests(TestCase):
    def test_task_creation_form_is_valid(self):
        tag = Tag.objects.create(name="test_tag")
        form_data = {
            "content": "test content",
            "deadline": "2024-09-25 13:04:06",
            "tags": (tag.id,),
        }

        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["content"], "test content")

    def test_task_form_field_widget(self):
        form = TaskForm()
        self.assertIsInstance(form.fields["content"].widget, forms.Textarea)
        self.assertIsInstance(form.fields["tags"].widget, forms.CheckboxSelectMultiple)
        self.assertIsInstance(form.fields["deadline"].widget, forms.DateTimeInput)

from django import forms

from todolist.models import Task, Tag


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                "type": "datetime-local",
            }
        )
    )

    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "style": "form-control; resize: none;",
                "rows": 3,
            }
        )
    )

    class Meta:
        model = Task
        fields = ("content", "deadline", "tags")

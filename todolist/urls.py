from django.urls import path

from todolist.views import (
    TaskListView,
    TagListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskToggleCompleteView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("update/<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
    path("delete/<int:pk>/", TaskDeleteView.as_view(), name="task-delete"),
    path(
        "toggle-complete/<int:pk>/",
        TaskToggleCompleteView.as_view(),
        name="task-toggle-complete",
    ),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "todolist"

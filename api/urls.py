from django.urls import path
from . import views

urlpatterns = [
    # todo
    path("todos/completed", views.TodoCompletedList.as_view()),
    path("todos", views.TodoListCreated.as_view()),
    path("todos/<int:pk>", views.TodoRetrieveUpdateDestroy.as_view()),
    path("todos/<int:pk>/complete", views.TodoComplete.as_view()),
    # auth
    path("signup", views.signup),
    path("login", views.login),
]

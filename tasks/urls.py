from django.urls import path
from tasks.views import home, add_task, show_tasks, edit_task, delete_task, completed_task, complete_tasks

urlpatterns = [
    path('', home, name='home'),
    path('add_new_task/', add_task, name='add_task'),
    path('show_task/', show_tasks, name='show_tasks'),
    path('edit_task/<int:id>', edit_task, name='edit_task'),
    path('delete_task/<int:id>', delete_task, name='delete_task'),
    path('completed_task/<int:id>', completed_task, name='completed_task'),
    path('complete_tasks/', complete_tasks, name='complete_tasks'),
]
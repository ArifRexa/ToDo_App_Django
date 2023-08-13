from django import forms
from tasks.models import TaskStoreModel

class TaskStoreForm(forms.ModelForm):
    class Meta:
        model = TaskStoreModel
        fields = ['id','taskTitle','taskDescription']

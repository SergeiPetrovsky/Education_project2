from  django.forms import ModelForm, TextInput, Textarea
from  .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "body", "fio", "job"]
        widgets = {
            "title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название'}),
            "body": Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание'}),
            "fio": TextInput(attrs={'class': 'form-control', 'placeholder': 'ФИО исполнителя'}),
            "job": TextInput(attrs={'class': 'form-control', 'placeholder': 'Должность'})
        }


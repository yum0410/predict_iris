from django import forms
from .models import Iris


class IrisForm(forms.ModelForm):
    class Meta:
        model = Iris
        fields = ('sepal_length', 'sepal_width', 'petal_length', 'petal_width')
        labels = {
            'sepal_length': 'sepal length',
            'sepal_width': 'sepal width',
            'petal_length': 'petal length',
            'petal_width': 'petal width'
        }

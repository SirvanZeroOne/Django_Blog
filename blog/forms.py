from django import forms
from . import models


class comment_forms(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ('name', 'email', 'comment')

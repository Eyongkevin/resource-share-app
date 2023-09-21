from django import forms
from .models import Tag

# TODO: Add fields for category(Radio) and tags(Select)

# Testing this
tags = [tag.name for tag in Tag.objects.all()]


class PostResourceForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "title-input",
                "placeholder": "Enter a title",
            }
        )
    )  # type='text'
    link = forms.URLField()  # type='url'
    description = forms.CharField(widget=forms.Textarea)  # type='textarea'

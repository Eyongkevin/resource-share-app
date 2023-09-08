from django import forms


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

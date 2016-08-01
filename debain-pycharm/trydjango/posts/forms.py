from django import forms

from .models import Post

class Postfrom(forms.ModelForm):
    class Meta:
        model = Post
        fields=[
            "title",
            "content"
        ]
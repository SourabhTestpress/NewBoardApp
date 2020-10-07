from django import forms
from django.shortcuts import get_object_or_404
from django.utils.text import slugify
from django.contrib.auth.models import User

from boards.models import Board, Topic, Post


class CreateTopicForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(), max_length=2000)
    board = forms.ModelChoiceField(
        queryset=Board.objects.all(), widget=forms.HiddenInput
    )
    user = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput)

    class Meta:
        model = Topic
        fields = ["board", "user", "subject", "message"]

    def save(self, *args, **kwargs):
        self.instance.slug = slugify(self.cleaned_data.get("subject"))
        self.instance.save()

        post_obj = Post.objects.create(
            message=self.cleaned_data.get("message"),
            topic=self.instance,
            created_by=kwargs.get("current_user"),
        )
        return self.instance

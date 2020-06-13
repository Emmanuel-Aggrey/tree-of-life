from django import forms

from ckeditor.widgets import CKEditorWidget

from .models import Article, Event


class ArticleForm(forms.ModelForm):
    story = forms.CharField(widget=CKEditorWidget())
    # story = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows':3,'cols':30}))

    class Meta:
        model = Article
        fields = ['title','image_url','image', 'story', 'active', 'tags', 'source']


class EventForm(forms.ModelForm):
    name = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 3, 'cols': 40}))

    class Meta:
        model = Event
        fields = ['event_type', 'name', 'date', 'time', 'active', ]

        widgets = {
            'date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date', }),
            'time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'time'}),

        }

from django import forms

from ckeditor.widgets import CKEditorWidget

from .models import Article, Event


class ArticleForm(forms.ModelForm):
    story = forms.CharField(widget=CKEditorWidget())
    # story = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows':3,'cols':30}))
   
    def clean(self):
        cleaned_data = super(ArticleForm, self).clean()
        image = cleaned_data.get('image')
        image_url = cleaned_data.get('image_url')
        age = cleaned_data.get('age')
        if image and image_url:
    
    # Record errors that will be displayed later.   
            msg = 'select just one filed either image or an image url not both.'
            self.add_error('image_url', msg)
            self.add_error('image', msg)
        
        if not  image and not image_url:
            msg = 'select just one filed either image or an image url both can not be blank.'
            self.add_error('image_url', msg)
            self.add_error('image', msg)
    # Always return the full collection of cleaned data.
        return cleaned_data

    
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

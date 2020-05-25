from django import  forms
from ckeditor.widgets import CKEditorWidget
from .models import  Article

class ArticleForm(forms.ModelForm):
    story = forms.CharField(widget=CKEditorWidget())
    # story = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows':3,'cols':30}))
    
    class Meta:
        model = Article
        fields = ['title','image','story','active','tags','source']

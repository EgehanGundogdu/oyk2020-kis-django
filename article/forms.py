from django import forms
from article.models import Post


class ArticleForm(forms.Form):
    header = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
    liked = forms.IntegerField(required=True)
    draft = forms.BooleanField(required=True)


class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Post
    # bütün fieldlar icin
        #fields = '__all__'
        # fields = ['content','header',....]
        exclude = ['owner', 'image']

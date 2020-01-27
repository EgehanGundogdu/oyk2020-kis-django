from django import forms
from article.models import Post, Comment


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

    def clean_header(self):
        header = self.cleaned_data.get('header')
        if Post.objects.filter(header=header).exists():
            raise forms.ValidationError('bu baslıkta bir makale bulunmakta!')
        return header

    # def clean_header(self):
    #     header = self.cleaned_data.get('header')
    #     try:
    #         post = Post.objects.get(header=header)
    #     except Post.DoesNotExist:
    #         post = None
    #     if post is not None:
    #         raise forms.ValidationError('asdadsads')
    #     return header

    def clean_content(self):
        if len(self.cleaned_data.get('content')) < 50:
            raise forms.ValidationError('İcerik 50 karakterden kisa olamaz')
        return self.cleaned_data.get('content')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']
        

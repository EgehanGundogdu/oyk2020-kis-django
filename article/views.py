from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import ListView
from article.forms import ArticleModelForm
from article.forms import ArticleForm, CommentForm
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse, Http404
from datetime import datetime
from article.models import Post, Comment
from django.contrib import messages
# Create your views here.


def post_detail(request, post_id):
    pk = post_id
    # try:
    #     post = Post.objects.get(id=pk)
    # except Post.DoesNotExist:
    #     raise Http404('bulunamadı')

    post = get_object_or_404(Post, id=pk, draft=False)
    comments = post.comments.all()
    form = CommentForm(request.POST or None)
    context = {
        'post': post,
        'comments': comments,
        'form': form
    }

    if request.method == 'POST':
        if form.is_valid():
            form.instance.post = post
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Basari ile kayit edildi')

            return redirect('post_detail', post_id=post.id)

    # if request.method == 'POST':
    #     if form.is_valid():
    #         form.instance.post = post
    #         form.save()
    #         messages.add_message(request, messages.SUCCESS,
    #                              'Basarıyla olusturuldu')

    #

    return render(request, 'article/post_detail.html', context)


def post_list(request):
    queryset = Post.objects.all()
    context = {
        'postlar': queryset
    }

    return render(request, 'article/post_list.html', context=context)


def anasayfa(request):

    context = {
        'django': True,
        'flask': True,
        'pehape': False,
        'now': datetime.now()
    }

    return render(request, template_name='article/index.html', context=context)


def create_post(request):
    form = ArticleForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            # header = form.cleaned_data.get()
            header = form.cleaned_data['header']
            content = form.cleaned_data['content']
            liked = form.cleaned_data['liked']
            draft = form.cleaned_data['draft']
            post = Post.objects.create(
                header=header, content=content, liked=liked,
                draft=draft, owner=request.user
            )
            post.save()
            return HttpResponse('nesne yaratıldı')
    else:
        print(request.user)
        return render(request, 'article/post_create.html', {'form': form})

# MODEL FORM KULLANILDI


def createPostMF(request):
    form = ArticleModelForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.owner = request.user
            form.save()
            return render(request, 'article/index.html')
    return render(request, 'article/post_create.html', {'form': form})


"""
CLASS BASED VIEW REFACTORING


"""


class ArticleListView(ListView):
    model = Post
    template_name = 'article/post_list.html'
    queryset = Post.objects.all()
    context_object_name = 'posts'


class ArticleCreateView(CreateView):
    model = Post
    #fields = '__all__'
    form_class = ArticleModelForm
    success_url = reverse_lazy('anasayfa')
    template_name = 'article/post_create.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article/post_detail.html'
    pk_url_kwarg = 'post_id'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        return context

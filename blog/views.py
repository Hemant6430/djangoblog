from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView

from .models import Post, Category
from .forms import PostForm, RegisterForm


# Home page - Read
def home(request):
    posts_list = Post.objects.all().order_by('-id')
    categories = Category.objects.all()

    paginator = Paginator(posts_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'title': 'Hello Djangoblog',
        'page_obj': page_obj,
        'categories': categories,
    }

    return render(request, 'blog/post_list.html', context)


# About page
def about(request):
    return render(
        request,
        "blog/about.html",
        {"title": "This is the DjangoBlog Team"}
    )


# Base page
def base(request):
    return render(
        request,
        "blog/base.html",
        {"title": "This is the DjangoBlog Team"}
    )


# Contact page
def contact(request):
    return render(
        request,
        "blog/contact.html",
        {"title": "This is the DjangoBlog Team"}
    )


# Post detail - Read
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    return render(
        request,
        'blog/post_detail.html',
        {'post': post}
    )


# Create Post
@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()

    return render(
        request,
        'blog/post_form.html',
        {'form': form}
    )


# Register
class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "blog/register.html"
    success_url = "/"

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
# Edit Post
@login_required
def post_edit(request, pk):
    post = get_object_or_404(
        Post,
        pk=pk,
        author=request.user
    )

    if request.method == 'POST':
        form = PostForm(
            request.POST,
            request.FILES,
            instance=post
        )

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm(instance=post)

    return render(
        request,
        'blog/post_form.html',
        {'form': form, 'post': post}
    )


# Delete Post
@login_required
def post_delete(request, pk):
    post = get_object_or_404(
        Post,
        pk=pk,
        author=request.user
    )

    if request.method == 'POST':
        post.delete()
        return redirect('home')

    return render(
        request,
        'blog/post_confirm_delete.html',
        {'post': post}
    )
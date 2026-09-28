from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Post, Category


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
def post_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        slug = request.POST['slug']
        content = request.POST['content']

        Post.objects.create(
            title=title,
            slug=slug,
            content=content
        )

        return redirect('home')

    return render(request, 'blog/post_form.html')
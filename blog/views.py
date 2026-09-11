from django.shortcuts import render


def home(request):
    return render(
        request,
        'blog/home.html',
        {'title': 'This is the DjangoBlog HomePage.'}
    )


def about(request):
    return render(
        request,
        'blog/about.html',
        {'content': 'This is the DjangoBlog Team.'}
    )


def contact(request):
    return render(
        request,
        'blog/contact.html',
        {'contant': 'This is the DjangoBlog HomePage.'}
    )
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'May 28, 2025'
    },
    {
        'author': 'JaneDoe',
        'title': 'Exploring Flask for Beginners',
        'content': 'In this post, we dive into setting up your first Flask app and explain the core concepts.',
        'date_posted': 'May 29, 2025'
    },
    {
        'author': 'MikeDev',
        'title': 'Understanding Python Decorators',
        'content': 'Decorators can be tricky. Here’s a breakdown of how they work with practical examples.',
        'date_posted': 'May 30, 2025'
    },
    {
        'author': 'TechieTom',
        'title': 'Async in Python Made Simple',
        'content': 'This article simplifies async/await in Python and shows where it’s most useful.',
        'date_posted': 'May 31, 2025'
    },
    {
        'author': 'SaraCoder',
        'title': 'Debugging Tips for Flask Apps',
        'content': 'Here are some tips and tools to help you debug your Flask applications efficiently.',
        'date_posted': 'June 1, 2025'
    },
    {
        'author': 'DevWithDan',
        'title': 'Top 5 Python Libraries for Web Development',
        'content': 'Discover some of the most powerful Python libraries for building modern web applications.',
        'date_posted': 'June 2, 2025'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

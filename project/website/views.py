from django.shortcuts import render

posts = [
    {
        'author': 'Michael',
        'title': "Michael's First Blog Post",
        'content': 'First post content',
        'date_posted': 'April 13, 2023'
    },
    {
        'author': 'Thomas',
        'title': "Thomas' First Blog Post",
        'content': 'First post content',
        'date_posted': 'January 12, 2023'
    },
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'website/home.html', context)

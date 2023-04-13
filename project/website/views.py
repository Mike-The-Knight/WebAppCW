from django.shortcuts import render

posts = [
    {
        'author': 'Michael',
        'title': "Michael's First Blog Post",
        'content': 'I am a student at the University of Surrey and I am studying Computer Science.',
        'date_posted': 'April 13, 2023'
    },
    {
        'author': 'Nishanth',
        'title': "Nishanth's First Blog Post",
        'content': 'I am a teacher at the University of Surrey and I am teaching Computer Science.',
        'date_posted': 'January 12, 2023'
    },
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'website/home.html', context)

def about(request):
    return render(request, 'website/about.html', {'title': 'About'})

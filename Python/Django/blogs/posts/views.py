from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post
# Create your views here.

def welcome(request):
    return HttpResponse("Welcome to my blog")

def say_hello(request, id):
    return HttpResponse(f"<h2 style='color:red;text-align:center'>Hello {id} From Django Course</h2>")

# posts = [
#     {
#         'id':1,
#         'title': 'First Post',
#         'description': 'This is the first post',
#         'image': 'p1.avif'
#     },
#     {
#         'id':2,
#         'title': 'Second Post',
#         'description': 'This is the second post',
#         'image': 'p2.avif'
#     },
#     {
#         'id':3,
#         'title': 'Third Post',
#         'description': 'This is the third post',
#         'image': 'p3.avif'
#     },
# ]
def index(request):
    posts = Post.objects.all()
    print('----------->',posts)
    return render(request, 'posts/index.html',context={'posts':posts})

def details(request,id):
    post = Post.objects.get(id=id)
    print('----------->',post)
    return render(request, 'posts/details.html',context={'post':post})

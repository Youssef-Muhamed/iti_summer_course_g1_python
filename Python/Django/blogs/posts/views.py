from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from posts.models import Post
from category.models import Category
# Create your views here.
# from posts.forms import PostForm
from posts.forms import PostModelForm
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
    return render(request, 'posts/index.html',context={'posts':posts})

def details(request,id):
    post = Post.objects.get(id=id)
    return render(request, 'posts/details.html',context={'post':post})

def delete_post(request,id):
    post = get_object_or_404(Post,id=id)
    post.delete()
    return redirect('posts.index')

def create_post(request):
    if request.method == 'GET':
        # categories = Category.objects.all()
        form = PostModelForm()
        return render(request, 'posts/createForm.html',context={'form':form})
    elif request.method == 'POST':
        # print('------------>',request.POST)
        # title = request.POST.get('title')
        # description = request.POST.get('description')
        # author = request.POST.get('author')
        # image = request.FILES.get('image')
        # version = request.POST.get('version')
        # category_id = request.POST.get('category')
        # category = Category.objects.get(id=category_id)
        # Post.objects.create(title=title,description=description,author=author,image=image,version=version,category=category)
        form = PostModelForm(request.POST,request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('posts.index')

        return redirect('posts.index')

def update_post(request,id):
    post = get_object_or_404(Post,id=id)
    # post = Post.objects.get(id=id)
    if request.method == 'GET':
        form = PostModelForm(instance=post)
        return render(request, 'posts/editForm.html',context={'form':form})
    elif request.method == 'POST':
        form = PostModelForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('posts.index')

        return redirect('posts.index')

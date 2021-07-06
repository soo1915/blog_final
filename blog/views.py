from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
# paginator = 게시판과 같은 목록이 주어져있을 때, 페이지 당 몇 개의 글을 보여줄지 지정해줄 수 있도록 도와주는 모듈
from django.core.paginator import Paginator
from .models import Blog
from .forms import BlogPost
# Create your views here.

def home(request):
    blogs = Blog.objects
    # 블로그 모든 글들을 대상으로
    blog_list = Blog.objects.all()
    # 블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(blog_list, 3)
    # request된 페이지가 뭔지를 알아냄 (request 페이지를 변수에 담아냄)
    page = request.GET.get('page')
    # request된 페이지를 얻어온 뒤 return 해줌
    posts = paginator.get_page(page)

    return render(request, 'blog/home.html', {'blogs':blogs, 'posts' : posts})
    
def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'blog/detail.html', {'blog': blog_detail})

def new(request) :
    return render(request, 'blog/new.html') 

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))

def blogpost(request) :
    if request.method == 'POST' :
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    else :
        form = BlogPost()
        return render(request, 'blog/new.html', {'form' : form})

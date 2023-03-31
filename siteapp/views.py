from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import Post,ERRORCASE
from .forms import PostForm,ErrorForm
from django.shortcuts import redirect,render
# Create your views here.



def error_list(request):
    posts=ERRORCASE.objects.order_by('published_date').reverse()
    return render(request,'siteapp/error_list.html',{'posts':posts})

def post_detail(request,pk):
    post=get_object_or_404(Post, pk=pk)
    return render(request,'siteapp/post_detail.html',{'post':post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'siteapp/post_edit.html',{'form':form})


    
def multiselect_form(request):
    if request.method == "POST":
        form = ErrorForm(request.POST)
        print("ログ１：%s"%(request.POST))
        if form.is_valid():
            print("データ保存")
            post = form.save(commit=False)
            post.selecter=request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('multiselect_form')
    else:
        form = ErrorForm()
    return render(request, 'siteapp/multiselect_form.html',{'form':form})
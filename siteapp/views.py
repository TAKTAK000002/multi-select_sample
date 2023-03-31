from django.shortcuts import render
from django.utils import timezone
from .models import ERRORCASE
from .forms import ErrorForm
from django.shortcuts import redirect,render
# Create your views here.



def error_list(request):
    posts=ERRORCASE.objects.order_by('published_date').reverse()
    return render(request,'siteapp/error_list.html',{'posts':posts})


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
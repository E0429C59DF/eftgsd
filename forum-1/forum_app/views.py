from django.shortcuts import render, redirect
from forum_app import forms
from .models  import beitrag, comment
from django.views.generic.detail import DetailView
from .forms import acomment

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    post = forms.PostBeitrag()
    all_beitrag = beitrag.objects.all()
    all_comment = comment.objects.all()
    welcome = request.user.username

    if request.method == 'POST':
        post = forms.PostBeitrag(request.POST)

        if post.is_valid():
            post.save(commit=True)
            post = forms.PostBeitrag()
            return HttpResponseRedirect(reverse('index'))
        
    return render(request, 'forum_app/index.html',{'beitrag_form':post, 'username':welcome, 'beitrag':all_beitrag, 'beitrag.comment.all':all_comment,})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))



def register(request):

    registered = False

    if request.method == 'POST':
        register = forms.register_form(request.POST)

        if register.is_valid():
            user = register.save()
            user.set_password(user.password)
            user.save()

            registered=True

    else:
        register = forms.register_form()

    return render(request, 'forum_app/register.html', {'register_form': register, 'registered':registered})

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            
            else:
                HttpResponse('Account not active')
        else:
            HttpResponse('Falsche Anmeldedaten')
    else:
        return render(request,'forum_app/login.html')
    
    return render(request,'forum_app/login.html')




class BeitragDetail(DetailView):
    model = beitrag
    template_name = 'forum_app/beitrag_details.html'
    

    def GET(self, request, pk):
        form = self.post(pk, initial=self.inital)
        return HttpResponse(request, self.template_name,{"beitrag_form":form})

#    def GET(self,request, pk):
#        post = comment.objects.get (pk)
#        context = {'post':post}
#        return render (request, 'forum_app/beitrag_details.html', context)
    
    def POST(self, request, pk):
        form = self.post(request.POST, pk)
        if acomment.is_valid():
            form.save(commit=True)
            forms = forms.acomment()
        return render(request, self.template_name, {"form":forms})

#    def POST(self, request, pk):
#        comments = comment.objects.get(pk)
#        comments.body = request.POST.get('body')
#        comments.save()
#        return redirect('comments')

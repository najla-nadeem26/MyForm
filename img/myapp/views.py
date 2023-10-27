from django.shortcuts import render
from .forms import MyForm
# Create your views here.


def form_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
             name = form.cleaned_data['name']
             email=form.cleaned_data['email']
             coursename=form.cleaned_data['coursename']
             joiningdate =form.cleaned_data['joiningdate']
             return render(request,'success.html',{'name':name,'email':email,'coursename':coursename,'joiningdate':joiningdate})
    else:
        form = MyForm()
        return render(request,'form.html',{'form':form})


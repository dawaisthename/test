from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Test
from .forms import TestForm

# Create your views here.

def test_all(request,*args,**kwargs):
    tests = Test.objects.all()
    context= {
         'tests':tests
    }
    return render(request,'index.html',context)
    # return HttpResponse('these is all page')
def test_insert(request,*args,**kwargs):
    form = TestForm()
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('all')
    else:
        form= TestForm()
    context = {
        'form':form
    }
    return render(request,'insert.html',context)
def test_remove(request,id=None,*args,**kwargs):
    Test.objects.get(id =id).delete()
    return redirect('all')
def test_update(request,id=None,*args,**kwargs):
    test= Test.objects.get(id=id)
    form = TestForm(instance = test)
    if request.method == 'POST':
        form = TestForm(request.POST,instance = test)
        if form.is_valid():
            form.save()
            return redirect('all')
        else:
            form = TestForm(instance=test)
    context = {'form': form
    }

    return render(request,'update.html',context)
    

    
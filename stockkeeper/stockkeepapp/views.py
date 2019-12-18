from django.shortcuts import render
from django.http import HttpResponse
from .forms import StockCreateForm
from .self_made_module import get_stockprice as gs


# Create your views here.
def search(request):
    if request.method == 'GET':
        form = StockCreateForm(request.GET)

    if form.is_valid():
        code=form.cleaned_data['code']
        context = gs.getstockprice(code)
        return render(request,'stockkeepapp/search_result.html',context)
    else:
        context = {
                   'form':StockCreateForm()
        }
        return render(request,'stockkeepapp/search_form.html',context)

def searchResult(request):
    context = gs.getstockprice(3626)
    return render(request,'stockkeepapp/search_result.html',context)

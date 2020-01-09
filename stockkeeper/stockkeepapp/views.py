from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .forms import StockSearchForm,StockResultForm
from .models import Stock
from .self_made_module import get_stockprice as gs

def search(request):
    #データをDBに登録する。
    if request.method == 'POST':
        form = StockResultForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('stockkeepapp:mystocklist')

    #コードから、社名・現在株価を取得し、フォームに入力して表示する。
    elif request.method == 'GET':
        form = StockSearchForm(request.GET or None)
        if form.is_valid():
            code=form.cleaned_data['code']
            companyInfo = gs.getstockprice(code)
            form =StockResultForm(initial={
                                           'code':companyInfo['stock_code'],
                                           'name':companyInfo['company_name'],
                                           'price':companyInfo['stock_price'],
                                           'remarks':companyInfo['remarks']
                                           })
            context={
                     'form':form
                     }
            return render(request,'stockkeepapp/search_result.html',context)

    #コード入力欄のみを持ったページを表示する。
        context = {
                   'form':StockSearchForm()
                   }
        return render(request,'stockkeepapp/search_form.html',context)

def my_stock_list(request):
    context = {
               'stock_list':Stock.objects.all()
    }
    context = gs.get_now_stockprice(context)
    return render(request,'stockkeepapp/stock_list.html',context)

def update(request,pk):
    stock = get_object_or_404(Stock,pk=pk)
    form =StockResultForm(request.POST or None,instance=stock)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('stockkeepapp:mystocklist')

    context = {
               'form':form
    }
    return render(request,'stockkeepapp/search_result.html',context)

def delete(request,pk):
    stock = get_object_or_404(Stock,pk=pk)

    if request.method == 'POST':
        stock.delete()
        return redirect('stockkeepapp:mystocklist')

    context = {
               'stock':stock
    }
    return render(request,'stockkeepapp/stock_confirm_delete.html',context)

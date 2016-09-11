from django.shortcuts import render
from django.shortcuts import HttpResponse
from display.forms import *
from .models import Assets
# from .forms import DetailForm
# from django.template.context_processors import csrf


# Create your views here.
def search(request):
    if request.method == 'POST':
        form = Asset(request.POST)
        if form.is_valid():
            date = form.cleaned_data
            fgdzc = date['gdzc']
            asset = Assets.objects.get(fgdzc=fgdzc)
            return render(request, 'detail.html', {'asset': asset})     # todo:补充资产编号没有怎样处理

    form = Asset()
    return render(request, 'base.html', {'asset': form})


# def detail(request, fgdzc):
#     # fgdzc = request.POST
#     if fgdzc in request.POST:
#         asset = request.POST(fgdzc)
#     else:
#         asset = '错误的资产编号'
#
#     return render(request, 'detail.html', {'asset': asset})

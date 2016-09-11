# #  _*_ coding: utf-8 _*_
# from display.forms import *
# from display.models import *
#
#
# def search_gdzc(request):
#     gdzc = Asset['gdzc']
#     fgdzcs = Assets.objects.all()
#     if gdzc in fgdzcs:
#         asset = Assets.objects.get(fgdzc=Asset['gdzc'])
#         return {'asset': asset}
#     else:
#         form = Asset()
#         return {'asset': form}

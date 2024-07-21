from datetime import datetime

from django.shortcuts import render

def index(request, tvno=0):
    tv_list = [{'name': 'CCTV中文国际', 'tvcode': '/cctv4/?spm=C28340.PALq7Iyxwdh3.ExidtyEJcS5K.4'},
               {'name': 'CCTV少儿频道', 'tvcode': 'cctvchild/?spm=C28340.PUdOXeMUrKth.ExidtyEJcS5K.26'}]
    now = datetime.now()
    tv = tv_list[tvno]
    return render(request, 'index.html', locals())

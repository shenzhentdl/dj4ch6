from datetime import datetime

from django.shortcuts import render

def index(request, tvno=0):
    tv_list = [{'name': 'CCTV中文国际', 'tvcode': '9sE12tg3CmA?si=oLlwPhqmOr4BS7ni'},
               {'name': '凤凰卫视资讯台', 'tvcode': 'bYBjjtgKUnM?si=SgGUL_PHTk8Pe0BA'}]
    now = datetime.now()
    tv = tv_list[tvno]
    return render(request, 'index.html', locals())

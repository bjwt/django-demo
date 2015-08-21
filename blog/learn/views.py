#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
from books.models import Book
import datetime

text = u"8月13日，记者从爆炸地点附近的高层拍摄天津爆炸事故现场。记者从事故处理现场了解到，8月12日晚，天津港国际物流中心区域内瑞海公司所属危险品仓库发生爆炸，截至发稿时已造成17人死亡，32名危重伤员，283人入院观察治疗。" 
def index(request):
    return HttpResponse(text)

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s. path = %s \n host = %s \n user Agent = %s\
addr = %s</body></html>" % (now,
request.path, request.get_host(), request.META['HTTP_USER_AGENT'],
request.META['REMOTE_ADDR'])
    return HttpResponse(html)

def hours_ahead(request, offset):
#    try:
#        offset = int(offset)
#    except ValueError:
#        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset,
dt)
    return HttpResponse(html)

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))


def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render_to_response('search_results.html',
            {'books': books, 'query': q})
    else:
        return render_to_response('search_form.html', {'error': True})

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

import jingo
from waffle import flag_is_active


def flag_in_view(request):
    if flag_is_active(request, 'myflag'):
        return HttpResponse('on')
    return HttpResponse('off')


def flag_in_jingo(request):
    return jingo.render(request, 'jingo.html')


def flag_in_django(request):
    c = RequestContext(request, {})
    return render_to_response('django.html', context_instance=c)

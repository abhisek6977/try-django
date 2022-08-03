'''
To render html web pages
'''
from django.http import HttpResponse

HTML_STRING = """
<h1> hello world</h1>
"""


def home_view(request):

    return HttpResponse(HTML_STRING)
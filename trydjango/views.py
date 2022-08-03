'''
To render html web pages
'''
import random
from django.http import HttpResponse



def home_view(request):

    name = "abhisek"
    number = random.randint(10, 1233123)
    H1_STRING = f"""
        <h1> hello {name} - {number}!</h1>
        """
    P_STRING = f"""
        <p> hi {name} - {number}!</p>
        """
    HTML_STRING = H1_STRING + P_STRING
    return HttpResponse(HTML_STRING)
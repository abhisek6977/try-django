'''
To render html web pages
'''
import random
from django.http import HttpResponse
from articals.models import Artical


def home_view(request):

    #from database

    name = "abhisek"
    random_id = random.randint(1, 3)
    artical_obj = Artical.objects.get(id=random_id)

    H1_STRING = f"""
        <h1> hello {artical_obj.title} (id: {artical_obj.id})!</h1>
        """
    P_STRING = f"""
        <p> hi {artical_obj.content}!</p>
        """
    HTML_STRING = H1_STRING + P_STRING
    return HttpResponse(HTML_STRING)
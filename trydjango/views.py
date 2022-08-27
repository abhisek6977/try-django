'''
To render html web pages
'''
import random
from django.http import HttpResponse
from articals.models import Artical
from django.template.loader import render_to_string, get_template


def home_view(request):

    #from database

    name = "abhisek"
    random_id = random.randint(1, 3)
    artical_obj = Artical.objects.get(id=random_id)
    artical_qs = Artical.objects.all()

    my_list = artical_qs #[123, 12 , 34 , 65, 76]

    context = {
        'object_list': my_list,
        'title': artical_obj.title,
        'id': artical_obj.id,
        'content': artical_obj.content
    }

    # handly when you need to use same template but multiple context
    templ = get_template('home-view.html')
    templ_string = templ.render(context=context)
    templ_string1 = templ.render(context=context)
    templ_string2 = templ.render(context=context)
    templ_string3 = templ.render(context=context)


    HTML_STRING = render_to_string('home-view.html', context=context)
    # HTML_STRING = """
    #     <h1> hello {title} (id: {id})!</h1>
    #     <p> hi {content}!</p>
    #     """.format(**context)
    return HttpResponse(HTML_STRING)
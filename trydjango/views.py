'''
To render html web pages
'''
import random
from django.http import HttpResponse
from articles.models import Article
from django.template.loader import render_to_string, get_template


def home_view(request, *args, **kwargs):

    #from database
    print(args, kwargs)

    name = "abhisek"
    random_id = random.randint(1, 3)
    article_obj = Article.objects.get(id=random_id)
    article_qs = Article.objects.all()

    my_list = article_qs #[123, 12 , 34 , 65, 76]

    context = {
        'object_list': my_list,
        'object': article_obj,
        'title': article_obj.title,
        'id': article_obj.id,
        'content': article_obj.content
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
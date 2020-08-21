import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','unttest.settings')
import django
django.setup()
from testapp.models import Category, Page


def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c


def add_page(cat, name, url):
    p = Page.objects.get_or_create(category=cat, name=name)[0]
    p.url = url
    p.save()
    return p

def populate():
    #catsn = {"python": python_pages,"django": django_pages,"other": other_pages}
    python_pages = [
        {"title": "Official Python Tutorial",
         "url": "http://docs.python.org/2/tutorial/"},
        {"title": "How to Think like a Computer Scientist",
         "url": "http://www.greenteapress.com/thinkpython/"},
        {"title": "Learn Python in 10 Minutes",
         "url": "http://www.korokithakis.net/tutorials/python/"}
    ]
    django_pages = [
        {"title": "Bottle", "url": "http://bottlepy.org/docs/dev/"},
        {"title": "Flask", "url": "http://flask.pocoo.org"}
    ]
    other_pages = [
        {"title": "Bottle",
         "url": "http://bottlepy.org/docs/dev/"},
        {"title": "Flask",
         "url": "http://flask.pocoo.org"}
    ]
    cats = {"Python": {"pages": python_pages},
        "Django": {"pages": django_pages},
        "Other Frameworks": {"pages": other_pages}}
    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for cd in cat_data["pages"]:
            add_page(c,cd['title'],cd['url'])
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))
if __name__ == '__main__':
    print("Starting Rango population scrtpt...")
    populate()
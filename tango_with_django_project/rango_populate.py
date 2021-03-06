import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

django.setup()      # django基础设施初始化，导入django项目的配置
from rango.models import Category, Page    # 导入模型


def populate():
    python_pages = [
        {"title": "Official Python Tutorial", "url": "http://doc.python.org/2/tutorial/"},
        {"title": "How to think like a computer Scientist", "url": "http://www.greenteapress.com/thinkpython/"},
        {"title": "Learn Python in 10 Minutes", "url": "http://www.korokitakis.net/tutorials/python"},
    ]

    django_pages = [
        {"title": "Official Django Tutorial", "url":  "https://docs.djangoproject.com/en/1.9/intro/tutorial01/"},
        {"title": "Django Rocks", "url": "http://www.djangorocks.com/"},
        {"title": "How to Tango with Django", "url": "http://www.tangowithdjango.com/"},
    ]

    other_pages = [
        {"title": "Bottle", "url": "http://bottlepy.org/docs/dev/"},
        {"title": "Flask", "url": "http://flask.pocoo.org"},
    ]

    cats = {
        "Python": {"pages": python_pages},
        "Django": {"pages": django_pages},
        "Other Frameworks": {"pages": other_pages},
    }

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"])

    for c in Category.objects.all():
        for p in Page.objects.filter(Category=c):
            print(f"- {c} - {p}")


def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    # Returns a tuple of (object, created), where object is the retrieved or created object and
    # created is a boolean specifying whether a new object was created.
    c.save()
    return c


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(Category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p


if __name__ == '__main__':
    print("starting rango population script...")
    populate()


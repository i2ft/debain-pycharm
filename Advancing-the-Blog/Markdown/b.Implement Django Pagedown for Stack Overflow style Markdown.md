``pip install django-pagedown``

``python manage.py collectstatic``

**settings.py**

install app -> 
``'pagedown',``

**froms.py**
class PostForm-> add code

    content = forms.CharField(widget=PagedownWidget)
    publish = forms.DateField(widget=forms.SelectDateWidget)
    
**base.html**

    {% block style %}{% endblock style %} 
    </style> 
     
    {% block head_extra %} {% endblock head_extra %} 
    </head> 
    

**post_detail.html**
    
    {% extends "base.html" %} 
     
     
    {% block head_extra %}  
    {{ form.media }} 
     
    {% endblock head_extra %} 
     
     
     
    {% block content %} 
    
**post_list.html**

~~
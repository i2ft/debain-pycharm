`pip install django-crispy-forms`

`settings.py`

install app :
`'crispy_forms',`

독립적으로 추가
`CRISPY_TEMPLATE_PACK = 'bootstrap3'`

**static_cdn -> css -> base.css**

추가

.wmd-panel {
    margin-right: 0px !important;
    margin-left: 0px !important;
}

**post_form.html**

추가

`{% load crispy_forms_tags %}`


`{{ form.as_p }}`
->
`{{ form|crispy }}`

----------

슬러그 유니코드

**settings.py**

`pip install unidecode`

**models.py**

추가

    from unidecode import unidecode
    from django.template import defaultfilters
    
def create_slug(instance, new_slug=None):
->


`slug = slugify(instance.title)`
->
`slug = defaultfilters.slugify(unidecode(instance.title))` 

컨텐츠 인코딩 처리

**views.py**

def post_detail(request, slug=None):
-->

`share_string = quote_plus(instance.content)`
->
`share_string = quote_plus(instance.content.encode(encoding='utf-8'))`


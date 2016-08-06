``pip install django-markdown-deux``

**settings.py**

install app -> 'markdown_deux'

**models.py**

++
``from django.utils.safestring import mark_safe``
``from markdown_deux import markdown``

++ 

class post : ->

     def get_markdown(self):
            content = self.content
            markdown_text = markdown(content)
            return mark_safe(markdown_text)
            
            
            
 **base.html**
 
 --
 ``console.log(content)``
 
 ``console.log(markedContent)``
 
 
 ``$(".content-markdown img").each(function(){``
 ->
 ``$(".post-detail-item img").each(function(){``


**post_detail.html**

``<div class='content-markdown'>{{ instance.content }}</div>``
->
``<div class='post-detail-item'>{{ instance.get_markdown }}</div>``


**post_list.html**


``<div class="caption">``
->
`<div class="caption post-detail-item">`

----------------------------------

`<p class='content-markdown'>{{ obj.content }}</p>`
->
`{{ obj.get_markdown }}`

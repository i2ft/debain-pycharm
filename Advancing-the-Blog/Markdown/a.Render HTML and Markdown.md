**base.html**

~~``<title>{% block head_title %}Try Django 1.9{% endblock head_title %}</title>``~~
>``<title>{% block head_title %}Advancing the Blog{% endblock head_title %}</title> ``

add
``<script   src="http://code.jquery.com/jquery-1.12.2.min.js"   integrity="sha256-lZFHibXzMHo3GGeehn1hudTAP3Sc0uKXBXAzHX1sjtk="   crossorigin="anonymous"></script> 
 ``
        
    <script src='https://cdnjs.cloudflare.com/ajax/libs/marked/0.3.5/marked.min.js'></script> 
    <script type="text/javascript"> 
    $(document).ready(function(){ 
        $(".content-markdown").each(function(){ 
                var content = $(this).text() 
                console.log(content) 
                var markedContent = marked(content) 
                console.log(markedContent) 
                $(this).html(markedContent) 
        }) 
     
    }) 
     
    </script> 

**post_detail.html**
delete

    <div class='col-sm-12'>
     
    {{ instance.content|linebreaks }} 
     
    <hr/> 
    <br/> 
    <div class="fb-comments" data-href="{{ request.build_absolute_uri }}" data-numposts="5"></div> 
    
edit

    <div class='col-sm-12 '> 
     
       <div class='content-markdown'>{{ instance.content }}</div> 
     
     
        <hr/> 
        <br/> 
        <div class="fb-comments" data-href="{{ request.build_absolute_uri }}" data-numposts="5"></div> 
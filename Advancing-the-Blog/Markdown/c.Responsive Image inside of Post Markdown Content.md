**base.html**
34

    $(".content-markdown img").each(function(){
            $(this).addClass("img-responsive");
    })
    
**post_list.html**


23

``<p class='content-markdown'>{{ obj.content|truncatechars:120 }}</p``

->
       
        <p class='content-markdown'>{{ obj.content }}</p>
    

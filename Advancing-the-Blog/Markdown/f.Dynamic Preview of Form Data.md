**from.html**

`content = forms.CharField(widget=PagedownWidget)`
->
`content = forms.CharField(widget=PagedownWidget(show_preview=False))`

**base.html**

 +++ ``<script type="text/javascript">`` ->
 

    var contentInput = $("#id_content");

    function setContent(value){
        var markedContent = marked(value)
        $("#preview-content").html(markedContent)
        $("#preview-content img").each(function(){
            $(this).addClass("img-responsive")
        })
    }
    setContent(contentInput.val())

    contentInput.keyup(function(){
        var newContent = $(this).val()
        setContent(newContent)
    })

    var titleInput = $("#id_title");
    


    function setTitle(value) {
        $("#preview-title").text(value)
    }
    setTitle(titleInput.val())

    titleInput.keyup(function(){
        var newContent = $(this).val()
        setTitle(newContent)
    })


    // preview-title
    // preview-content


**post_form.html**

`<div class='col-sm-6 col-sm-offset-3'>`
->

    <div class='col-sm-6'>
    <h1>Preview</h1>
    <hr/>
    <div class='content-preview'>
        <h3 id='preview-title'></h3>
        <p id='preview-content'></p>
    </div>
    </div>
    <div class='col-sm-6'>
    
    
``<h1>Form</h1>``

++
    
    <hr/>
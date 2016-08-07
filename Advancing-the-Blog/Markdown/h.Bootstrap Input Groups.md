**base.html**

참고사이트 : http://fontawesome.io/

추가

`<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css' >`

**post_list.html**

    <form method='GET' action=''>
    <input type='text' name='q' placeholder='Search posts' value='{{ request.GET.q }}'/>
    <input type='submit' value='Search' />
    
-> 변경

    <form method='GET' action='' class='row'>
            <div class='col-sm-6'>
                <div class='input-group'>
                    <input class='form-control' type='text' name='q' placeholder='Search posts' value='{{ request.GET.q }}'/>
                    <span class='input-group-btn'>
                        <!-- <input class='btn btn-default' type='submit' value='Search' /> -->
                        <button class='btn btn-default' type='submit'>Search <i class="fa fa-search"></i></button>
                    </span>
                </div>
            </div>
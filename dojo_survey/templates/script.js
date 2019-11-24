
$( document ).ready(function() {
    $(".btn btn-secondary dropdown-toggle").click(function(){
        $(".btn btn-secondary dropdown-toggle").html($(this).text()+' <span class="caret"></span>');
    });
});

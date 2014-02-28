// From http://stackoverflow.com/a/6533544
function getCookie(c_name)
{
    if (document.cookie.length > 0)
    {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1)
        {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
 }


$(function() {

    $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie('csrftoken') }
    });



    $( ".draggable" ).draggable({revert:true, revertDuration: 0});
    $( ".droppable" ).droppable({
      //hoverClass: "glyphicon glyphicon-folder-open dd-folder-icon",
      over: function( event, ui ) {
         $( this ).find("span").removeClass( "glyphicon-folder-close" );    
         $( this ).find("span").addClass( "glyphicon-folder-open" );    
      },
      out: function( event, ui ) {
         $( this ).find("span").removeClass( "glyphicon-folder-open" );    
         $( this ).find("span").addClass( "glyphicon-folder-close" );    
      },
      //activeClass: "light-blue-folder",
      tolerance: "intersect",
      drop: function( event, ui ) {

         $( this ).animate({
            color: "#79697A",
            }, 300 );
         $( this ).find(".folder-message").text( "Adding link..." );
         ui.draggable.css('visibility', 'hidden');
         ui.draggable.slideUp();                 
         var that=this;
         
      // THIS IS THE WRONG URL!!!!
      $.post("/dragondrop/userpage/jea/",
             {query: "a wee POST test"},
             function(data) {
                alert( "success" );
      })
          .fail(function() {
            alert( "There was an error adding the bookmark" );
          });


         
         window.setTimeout(function() {
                             $( that ).find(".folder-message").html( "&nbsp;" );
                             $( that ).animate({
                                color: "black",
                                }, 500 );
                             $( that ).find("span").removeClass( "glyphicon-folder-open" );    
                             $( that ).find("span").addClass( "glyphicon-folder-close" );
                           },
                           800);
         
      }
    });
    
    
});
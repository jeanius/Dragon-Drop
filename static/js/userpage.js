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

    $( "#folder-filter" ).keyup(function() {
        $( ".droppable" ).each (function() {
            // If the typed string is in the name of this folder...
            if ($(this).find(".folder-name").text().toLowerCase()
                         .indexOf($( "#folder-filter" ).val().toLowerCase()) != -1) {
                $(this).show();
            } else {
                $(this).hide();
            }
        });
    });

    $( ".draggable" ).draggable({revert:true, revertDuration: 0});
    $( ".droppable" ).droppable({
      //hoverClass: "glyphicon glyphicon-folder-open dd-folder-icon",
      over: function( event, ui ) {
         $( this ).find("span").not(".keep-folder-open").removeClass( "glyphicon-folder-close" );    
         $( this ).find("span").not(".keep-folder-open").addClass( "glyphicon-folder-open" );    
      },
      out: function( event, ui ) {
         $( this ).find("span").not(".keep-folder-open").removeClass( "glyphicon-folder-open" );    
         $( this ).find("span").not(".keep-folder-open").addClass( "glyphicon-folder-close" );    
      },
      //activeClass: "light-blue-folder",
      tolerance: "pointer",
      drop: function( event, ui ) {

         $( this ).animate({
            color: "#79697A",
            }, 300 );
         $( this ).find(".folder-message").text( "Adding link..." );
         ui.draggable.css('visibility', 'hidden');
         ui.draggable.slideUp();                 
         var that=this;
         

         $.post("/dragondrop/ajax-drop-to-folder/",
             { url: ui.draggable.find("a").attr("href") //,
               //foldername: $( this ).find(".folder-name").text()
               //btitle: "",
               //bdescr: ""
             },
             function(data) {
                alert( data + '. All bookmarks are currently being saved to /dragondrop/Online_Editors/');
         })
            .fail(function() {
               alert( "There was an error adding the bookmark" );
            });


         
         window.setTimeout(function() {
                             $( that ).find(".folder-message").html( "&nbsp;" );
                             $( that ).animate({
                                color: "black",
                                }, 500 );
                             $( that ).find("span").not(".keep-folder-open").removeClass( "glyphicon-folder-open" );    
                             $( that ).find("span").not(".keep-folder-open").addClass( "glyphicon-folder-close" );
                           },
                           800);
         
      }
    });
    
    
});
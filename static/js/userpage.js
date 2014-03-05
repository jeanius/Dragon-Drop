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

    var removeMessageAfterShortDelay = function(that) {
        window.setTimeout(function() {
                     $( that ).find(".folder-message").html( "&nbsp;" );
                     $( that ).animate({
                        color: "black",
                        }, 500 );
                   },
                   800);
    }

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

    $( ".draggable" ).draggable({cursor: "move",
                                 cursorAt: { top: 0, left: -12 },
                                 helper: function( event ) {
                                     return $( "<div class='ui-widget-header' style='width: 140px;background: yellow;box-shadow: 1px 1px 2px 2px rgba(0,0,0,0.3)'>Drag to a folder</div>" );
                                 },
                                 start: function() {
                                     $(".bin p").first().text("Drop here if you don't want to see this page in search results again.");
                                 },
                                 stop: function() {
                                     $(".bin p").first().text(originalBinText);
                                 }
                                });
    $( ".droppable" ).droppable({
      //hoverClass: "glyphicon glyphicon-folder-open dd-folder-icon",
      over: function( event, ui ) {
         console.log(ui.draggable.attr('class'))
         // The next line needs to be changed (first, give the draggable folders a more specific class name)
         if (!ui.draggable.hasClass("droppable")) {
             $( this ).find("span").not(".keep-folder-open").removeClass( "glyphicon-folder-close" );    
             $( this ).find("span").not(".keep-folder-open").addClass( "glyphicon-folder-open" );    
         }
      },
      out: function( event, ui ) {
         // The next line needs to be changed (first, give the draggable folders a more specific class name)
         if (!ui.draggable.hasClass("droppable")) {
             $( this ).find("span").not(".keep-folder-open").removeClass( "glyphicon-folder-open" );    
             $( this ).find("span").not(".keep-folder-open").addClass( "glyphicon-folder-close" );
         }
      },
      //activeClass: "light-blue-folder",
      tolerance: "pointer",
      drop: function( event, ui ) {

         $( this ).animate({
            color: "#79697A",
            }, 300 );
         $( this ).find(".folder-message").text( "Adding link..." );
         //ui.draggable.css('visibility', 'hidden');
         //ui.draggable.slideUp();                 
         var that=this;
         

         $.post("/dragondrop/ajax-drop-to-folder/",
             { url: ui.draggable.find("a").attr("href") },
             function(data) {
                $( that ).find(".folder-message").text( "Link added" );
                $( that ).find("span").not(".keep-folder-open").removeClass( "glyphicon-folder-open" );    
                $( that ).find("span").not(".keep-folder-open").addClass( "glyphicon-folder-close" );
                removeMessageAfterShortDelay(that);
             })
                .fail(function() {
                   $( that ).find(".folder-message").text( "Error adding bookmark" );
                   $( that ).find("span").not(".keep-folder-open").removeClass( "glyphicon-folder-open" );    
                   $( that ).find("span").not(".keep-folder-open").addClass( "glyphicon-folder-close" );
                   removeMessageAfterShortDelay(that);
                });



         
      }
    });
    
    var originalBinText = $(".bin p").first().text();
    // To do: Use a more descriptive class name for the draggable folders than .droppable
    $( ".droppable" ).draggable({cursor: "move",
                                 cursorAt: { top: 0, left: -12 },
                                 helper: function( event ) {
                                     return $( "<div class='ui-widget-header' style='width: 100px;z-index:30;background: yellow;box-shadow: 1px 1px 2px 2px rgba(0,0,0,0.3)'>Drag to the bin to delete</div>" );
                                 },
                                 start: function() {
                                     $(".bin p").first().text("Drop here to delete");
                                 },
                                 stop: function() {
                                     $(".bin p").first().text(originalBinText);
                                 }
                                });    
});
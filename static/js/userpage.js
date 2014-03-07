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
                     $( that ).find(".folder-message").html( "" );
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
    $( "#bookmarks-filter" ).keyup(function() {
        $( ".draggable" ).each (function() {
            // If the typed string is in the name of this folder...
            if ($(this).text().toLowerCase()
                         .indexOf($( "#bookmarks-filter" ).val().toLowerCase()) != -1) {
                $(this).show();
            } else {
                $(this).hide();
            }
        });
    });

    var dragStart = function() {
        $(".bin p").first().text("Drop here if you don't want to see this page in search results again.");
        $(".bin span, .glyphicon-folder-open, .glyphicon-folder-close").addClass( "highlight-droppable" );
    }
    var dragStop = function() {
        $(".bin p").first().text(originalBinText);
        $(".bin span, .glyphicon-folder-open, .glyphicon-folder-close").removeClass( "highlight-droppable" );   
    }
    var draggableHelper = function(event) {
        return $( "<div class='ui-widget-header draggable-helper'>Drag to a folder</div>" );    
    }
    
    $( "#sortable" ).sortable({start: dragStart,
                               stop: dragStop
                              });
    
    $( ".search-result" ).draggable({cursor: "move",
                                     cursorAt: { top: 0, left: -12 },
                                     helper: draggableHelper,
                                     start: dragStart,
                                     stop: dragStop
                                    });

    var makeDroppable = function() {
        $( ".droppable" ).droppable({
          over: function( event, ui ) {
             var folderIcon = $( this ).find("span.glyphicon").not(".keep-folder-open, .glyphicon-trash");
             folderIcon.removeClass( "glyphicon-folder-close" );    
             folderIcon.addClass( "glyphicon-folder-open" );
             $( this ).find(".glyphicon").addClass("highlight-droppable-hover");
          },
          out: function( event, ui ) {
             var folderIcon = $( this ).find("span.glyphicon").not(".keep-folder-open, .glyphicon-trash");
             folderIcon.removeClass( "glyphicon-folder-open" );    
             folderIcon.addClass( "glyphicon-folder-close" );
             $( this ).find(".glyphicon").removeClass("highlight-droppable-hover");
          },
          //activeClass: "light-blue-folder",
          tolerance: "pointer",
          drop: function( event, ui ) {
             $( this ).animate({
                color: "#79697A",
                }, 300 );
             $( this ).find(".folder-message").text( "Adding link..." );                
             var that=this;
             
             $( this ).find(".glyphicon").removeClass("highlight-droppable-hover");
             var folderIcon = $( that ).find("span.glyphicon").not(".keep-folder-open, .glyphicon-trash");
             $.post("/dragondrop/ajax-drop-to-folder/",
                 { url: ui.draggable.find("a").attr("href"),
                   folder_name: $( that ).find(".folder-name").first().text() },
                 function(data) {
                    $( that ).find(".folder-message").text( "Link added" );
                    folderIcon.removeClass( "glyphicon-folder-open" );    
                    folderIcon.addClass( "glyphicon-folder-close" );
                    removeMessageAfterShortDelay(that);
                 })
                    .fail(function() {
                       $( that ).find(".folder-message").text( "Error adding bookmark" );
                       folderIcon.removeClass( "glyphicon-folder-open" );    
                       folderIcon.addClass( "glyphicon-folder-close" );
                       removeMessageAfterShortDelay(that);
                    });  
          }
        });
    }
    makeDroppable();
    
    $("#add-folder-button")
        .click(function() {
             var folderName = $("#new-folder-name-input").val();      
             $.post("/dragondrop/ajax-create-folder/",
             { folderName: folderName },
             function(data) {
                $("#folder-add-message").text(data);
                if (data==="Folder created") {
                    $("#folder-list")
                        .append(   '<div class="col-lg-12 col-md-12 col-sm-6 col-xs-12 droppable">'
                                 + ' <a href="/dragondrop/' + folderName.replace(" ", "_") + '/">'
                                 + '  <span class="glyphicon lighter-colour dd-folder-icon glyphicon-folder-close"></span>'
                                 + '  <span class="folder-name">' + folderName + '</span>'
                                 + ' </a>'
                                 + ' <span class="folder-message"></span>'
                                 + '</div>');
                    makeDroppable();
                }
                $("#new-folder-name-input").val("");
             })
                .fail(function() {
                   $("#folder-add-message").text("An error occurred when attempting to add the folder. Please try again.");
                });
    });
    
    // Add folder when Enter key is pressed
    // http://stackoverflow.com/questions/155188/trigger-a-button-click-with-javascript-on-the-enter-key-in-a-text-box
    $("#new-folder-name-input").keyup(function(event){
        if(event.keyCode == 13){
            $("#add-folder-button").click();
        }
    });
    
    var originalBinText = $(".bin p").first().text();
                                                         
});


// hovering over the bin area
// I've moved this code to the events for dragging - James
/*$( ".bin span" ).hover(
  function() {
    $( this ).toggleClass( "highlight-droppable" );
  }, function() {
    $( this ).removeClass( "highlight-droppable" );
  }
);*/


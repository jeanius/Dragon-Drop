$(function() {

    $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie('csrftoken') }
    });

    // Filter folder names based on typed text
    $( "#folder-filter" ).keyup(function() {
        $( ".droppable" ).each (function() {
            if (textAppearsIn($("#folder-filter").val(), $(this).find(".folder-name").text())) {
                $(this).show();
            } else {
                $(this).hide();
            }
        });
    });
    
    // Filter bookmarks in folder based on typed text
    $( "#bookmarks-filter" ).keyup(function() {
        $( ".draggable" ).each (function() {
            if (textAppearsIn($("#bookmarks-filter").val(), $(this).text())) {
                $(this).show();
            } else {
                $(this).hide();
            }
        });
    });

    var elementsToHighlightOnDrag = $(".bin span, .dd-folder-icon");
    var dragStart = function() {
        elementsToHighlightOnDrag.addClass("highlight-droppable");
		// display the bin message
		$(".bin-message").show();
    }
    var dragStop = function() {
        elementsToHighlightOnDrag.removeClass("highlight-droppable");   
		// hide the bin message
		$(".bin-message").hide();
    }
    
    // The helper is the small div that moves when a search result is dragged
    var draggableHelper = function(event) {
        return $( "<div class='ui-widget-header draggable-helper'>Drag to a folder</div>" );    
    }
    
    $( "#sortable" ).sortable({start: dragStart, stop: dragStop});
    
    $( ".search-result" ).draggable({cursor: "move",
                                     cursorAt: { top: 0, left: -12 },
                                     helper: draggableHelper,
                                     start: dragStart,
                                     stop: dragStop
                                    });

    makeDroppable();
    
    $("#add-folder-button")
        .click(function() {
             var folderName = $("#new-folder-name-input").val();      
             $.post("/dragondrop/ajax-create-folder/",
             { folderName: folderName },
             function(data) {
                $("#folder-add-message").text(data);
                if (data === "Folder created") {
                    $("#folder-list").append(makeNewFolderElement(folderName));
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
                                                         
});






//
// Some utilities
//

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

function textAppearsIn(needle, haystack) {
    return haystack.toLowerCase()
              .indexOf(needle.toLowerCase()) != -1;
}



function removeMessageAfterShortDelay(folderElement) {
	window.setTimeout(function() {folderElement.find(".folder-message").html("");}, 800);
}


function ajaxDropToFolder(dropTarget, ui) {
    var folderIcon = dropTarget.find(".dd-folder-icon").not(".keep-folder-open");
	$.post("/dragondrop/ajax-drop-to-folder/",
		 { url: ui.draggable.find("a").attr("href"),
		   folder_name: dropTarget.find(".folder-name").first().text() },
		   function(messageFromPython) {
			  dropTarget.find(".folder-message").text( messageFromPython );
			  folderIcon
				  .removeClass( "glyphicon-folder-open" )   
				  .addClass( "glyphicon-folder-close" );
		      ui.draggable.addClass("saved-bookmark")
			  removeMessageAfterShortDelay(dropTarget);
		   })
			.fail(function() {
			   dropTarget.find(".folder-message").text( "Error adding bookmark" );
			   folderIcon
				   .removeClass( "glyphicon-folder-open" )   
				   .addClass( "glyphicon-folder-close" );
			   removeMessageAfterShortDelay(dropTarget);
			}); 
}


function makeNewFolderElement(folderName) {
return '<div class="col-lg-12 col-md-12 col-sm-6 col-xs-12 droppable">'
       + ' <a href="/dragondrop/' + folderName.replace(" ", "_") + '/">'
       + '  <span class="glyphicon lighter-colour dd-folder-icon glyphicon-folder-close"></span>'
       + '  <span class="folder-name">' + folderName + '</span>'
       + ' </a>'
       + ' <span class="folder-message"></span>'
       + '</div>';
}


function makeDroppable() {
	$( ".droppable" ).droppable({
	  over: function( event, ui ) {
		 $( this ).find(".dd-folder-icon").not(".keep-folder-open")
			 .removeClass( "glyphicon-folder-close" )
			 .addClass( "glyphicon-folder-open" );
		 $( this ).find(".glyphicon").addClass("highlight-droppable-hover");
	  },
	  out: function( event, ui ) {
		 $( this ).find(".dd-folder-icon").not(".keep-folder-open")
			 .removeClass( "glyphicon-folder-open" )
			 .addClass( "glyphicon-folder-close" );
		 $( this ).find(".glyphicon").removeClass("highlight-droppable-hover");
	  },
	  tolerance: "pointer",
	  drop: function( event, ui ) {
		 var dropTarget = $(this);
		 dropTarget.find(".folder-message").text( "Adding link..." );                          
		 dropTarget.find(".glyphicon").removeClass("highlight-droppable-hover");
		 ajaxDropToFolder(dropTarget, ui)
	  }
	});
}

// hovering over the bin area
// I've moved this code to the events for dragging - James
/*$( ".bin span" ).hover(
  function() {
    $( this ).toggleClass( "highlight-droppable" );
  }, function() {
    $( this ).removeClass( "highlight-droppable" );
  }
);*/



//Deleting the folder -- please fix this :(

$( ".folder-name" ).mouseover(function() {
  $( ".delete-folder" ).show();
});

$( ".folder-name", ".delete-folder" ).mouseout(function() {
  $( ".delete-folder" ).hide();
});


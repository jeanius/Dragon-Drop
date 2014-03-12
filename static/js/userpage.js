$(function() {

    $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie('csrftoken') }
    });

    
    // Add a message and disable button when the search or add button is clicked
    var addBtnMessage = function(button, message, keepWidth) {
        var btnWidth = button.css("width");
        button.addClass("disabled");
        button.text(message);
        if (!keepWidth) {
            button.css("width", btnWidth);
        }
    }
    
    $(".btn-primary-folder").click(function() {
        addBtnMessage($(this), "Adding...");
    });
    $(".btn-primary-search").click(function() {
        addBtnMessage($(this), "Searching...", true);
    });    
    

    $(".droppable")
        .mouseover(function() {
            allowBookmarkReorder = false;
            // Only allow re-ordering of bookmarks if the user isn't about to
            // drop onto a folder or the bin
            $( "#sortable" ).sortable( "option", "disabled", true );
        })
        .mouseout(function() {
            allowBookmarkReorder = true;
            $( "#sortable" ).sortable( "option", "disabled", false );
        })
    
    
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
    var dragStop = function(event, ui) {
        elementsToHighlightOnDrag.removeClass("highlight-droppable");   
        // hide the bin message
        $(".bin-message").hide();
    }
    
    var sortStop = function(event, ui) {
        dragStop(event, ui);
        var prevBmRank = ui.item.prev().attr('data-bfrank');
        var nextBmRank = ui.item.next().attr('data-bfrank');
        var thisBmRank = ui.item.attr('data-bfrank');
        // Set the rank (a floating-point value) to be between the ranks of the
        // bookmarks above and below. If the bookmark is dropped at the top or bottom
        // of the list, set its rank highest or lowest, respectively.
        if (thisBmRank < nextBmRank) {
            if (typeof prevBmRank === 'undefined') {
                changeBookmarkRank(ui.item, +nextBmRank + 1);
            } else {
                changeBookmarkRank(ui.item, (+prevBmRank + (+nextBmRank)) / 2);
            }
        } else if (thisBmRank > prevBmRank) {
            if (typeof nextBmRank === 'undefined') {
                changeBookmarkRank(ui.item, +prevBmRank - 1);
            } else {
                changeBookmarkRank(ui.item, (+prevBmRank + (+nextBmRank)) / 2);
            }        
        }
    }

    // The helper is the small div that moves when a search result is dragged
    var draggableHelper = function(event) {
        return $( "<div class='ui-widget-header draggable-helper'>Drag to a folder</div>" );    
    }
    
    $( "#sortable" ).sortable({start: dragStart, stop: sortStop});
    
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
             $.post("/ajax-create-folder/",
             { folderName: folderName },
             function(data) {
                $("#folder-add-message").text(data);
                if (data === "Folder created") {
                    $("#folder-list").append(makeNewFolderElement(folderName));
                    makeDroppable();
                    makeFoldersDeleteable();
                }
                $("#new-folder-name-input").val("");
             })
                .fail(function() {
                   $("#folder-add-message").text("An error occurred when attempting to add the folder. Please try again.");
                });
    });


    // delete a bookmark
    $(".glyphicon-remove")
        .click(function() {
             var deleteButton = $(this);
             deleteButton.hide();
             var bookmarkUrl = deleteButton.parent().parent().find("strong").find("a").first().attr("href");
             $.post("/ajax-delete-bookmark/",
             { bookmarkUrl: bookmarkUrl, folderName: $("#current-folder-name").text() },
             function(data) {
                 deleteButton.parent().parent().slideUp();
                 deleteButton.show();
             })
                .fail(function() {
                    alert("An error occurred while attempting to delete the bookmark.");
                    deleteButton.show();
                });
    });


    makeFoldersDeleteable();
    
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

// Call this to add a url to a folder.
// Parameters:
//   url
//   folder_name
//   success_function: A function with one parameter(the message returned by Django)
//   failure_function: A function with no parameters, which is called if the POST request fails
function ajaxAddToFolder(url, folder_name, success_function, failure_function) {
    $.post("/ajax-drop-to-folder/",
           { url: url, folder_name: folder_name },
           success_function)
            .fail(failure_function); 
}

function ajaxDropToFolder(dropTarget, ui) {
    var folderIcon = dropTarget.find(".dd-folder-icon").not(".keep-folder-open");
    ajaxAddToFolder(ui.draggable.find("strong").find("a").attr("href"),
                    dropTarget.find(".folder-name").first().text(),
                    function(messageFromPython) {
                      dropTarget.find(".folder-message").text( messageFromPython );
                      folderIcon
                          .removeClass( "glyphicon-folder-open" )   
                          .addClass( "glyphicon-folder-close" );
                      ui.draggable.addClass("saved-bookmark");
                      //if ($("#current-folder-name").text()=="Bin Folder") {ui.draggable.slideUp()};
                      removeMessageAfterShortDelay(dropTarget);
                    },
                    function() {
                       dropTarget.find(".folder-message").text( "Error adding bookmark" );
                       folderIcon
                           .removeClass( "glyphicon-folder-open" )   
                           .addClass( "glyphicon-folder-close" );
                       removeMessageAfterShortDelay(dropTarget);
                    });
};


// Call this to add a url to the bin folder.
// Parameters:
//   url
//   success_function: A function with one parameter(the message returned by Django)
//   failure_function: A function with no parameters, which is called if the POST request fails
function ajaxAddToBin(url, success_function, failure_function) {
    $.post("/ajax-drop-to-bin/",
           { url: url },
           success_function)
            .fail(failure_function); 
}

function ajaxDropToBin(dropTarget, ui) {
    var folderIcon = dropTarget.find(".dd-folder-icon").not(".keep-folder-open");
    ajaxAddToBin(ui.draggable.find("strong").find("a").attr("href"),
                 function(messageFromPython) {
                      dropTarget.find(".folder-message").text( messageFromPython );
                      ui.draggable.addClass("saved-bookmark")
                      ui.draggable.slideUp();
                      removeMessageAfterShortDelay(dropTarget);
                 },
                 function() {
                     dropTarget.find(".folder-message").text( "Error adding bookmark" );
                     removeMessageAfterShortDelay(dropTarget);
                 });
}



function makeNewFolderElement(folderName) {
return '<div class="col-lg-12 col-md-12 col-sm-6 col-xs-12 droppable">'
       + ' <span class="glyphicon glyphicon-remove-circle delete-folder"></span>'
       + ' <a href="/' + folderName.split(" ").join("_") + '/">'
       + '  <span class="glyphicon lighter-colour dd-folder-icon glyphicon-folder-close"></span>'
       + '  <span class="folder-name">' + folderName + '</span>'
       + ' </a>'
       + ' <span class="folder-message"></span>'
       + '</div>';
}

function makeFoldersDeleteable() {
    $(".delete-folder")
        .click(function() {
           var deleteButton = $(this);
           deleteButton.hide();
           var folderName = deleteButton.parent().find(".folder-name").text();
           $('#delete-folder-name').text(folderName);
           $('#confirm-folder-deletion-modal').modal();
           $('#confirm-folder-deletion-button').click(function() {
               deleteFolder(folderName, deleteButton);
           });
           $('#cancel-folder-deletion-button').click(function() {
               deleteButton.show();
           });
    });
}

function deleteFolder(folderName, deleteButton) {
     $.post("/ajax-delete-folder/",
     { folderName: folderName },
     function(data) {
         deleteButton.parent().slideUp();
         deleteButton.show();
     })
        .fail(function() {
            deleteButton.show();
        });
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
            if (dropTarget.hasClass("bin")) {
                ajaxDropToBin(dropTarget, ui);
            } else {
                ajaxDropToFolder(dropTarget, ui);
            }
        }
    });
}


function changeBookmarkRank(bookmarkDiv, newRank) {
    bookmarkDiv.attr('data-bfrank', newRank)
    $.post("/ajax-change-bookmark-rank/",
       { new_rank: bookmarkDiv.attr("data-bfrank"),
         url: bookmarkDiv.find("strong").find("a").attr("href"),
         folder_name: $("#current-folder-name").text() },
       function(messageFromPython) {

       })
        .fail(function() {
           alert("Error changing rank");
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

$( "#folder-box" ).mouseover(function() {
  $( ".delete-folder" ).show();
});

$( "#folder-box" ).mouseout(function() {
  $( ".delete-folder" ).hide();
});


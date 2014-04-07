
var encodeUrl = function(folderName) {
    return folderName.split(" ").join("_");
}

// This will be used to prevent sorting and dropping of a bookmark at the same time
var hoveringOverDroppable = false;

$(function() {

    // Set the height of the folder list in the first column
    // (Desktop devices only)
    var setFolderListHeight = function() {
        window.scrollTo(0,0);
        if ($(window).width() >= 992) {
            var folderBoxHeight = $("#folder-box").height();
            var resultsBoxHeight = $(".results").height();
            var folderListTop = $("#scrollable").position().top;
            $("#scrollable").css("height", (folderBoxHeight - folderListTop - 93) + "px");
            if ($("#scrollable-bookmarks").length > 0) {
                var bookmarkListTop = $("#scrollable-bookmarks").position().top;
                $("#scrollable-bookmarks").css("height", (resultsBoxHeight - bookmarkListTop - 82) + "px");
            }
        } else {
            $("#scrollable").css("height", "");
            $("#scrollable-bookmarks").css("height", "");
        }
        if ($(window).height() < 770) {
            $(".glyphicon-trash").css("padding-top", "0px")
        } else {
            $(".glyphicon-trash").css("padding-top", "0px")
        }
    }
    setFolderListHeight();
    $(window).resize(setFolderListHeight);
    

    // Get the CSRF token, which will be needed for Ajax POST requests
    $.ajaxSetup({ headers: { "X-CSRFToken": getCookie('csrftoken') } });
 
    // Set up Bootstrap dropdown menus
    $('.dropdown-toggle').dropdown();
 
    // Add a message and disable the button when the search or add button is clicked
    var addBtnMessage = function(button, message, keepWidth) {
        var btnWidth = button.css("width");
        button.addClass("disabled");
        button.text(message);
        if (keepWidth) {
            button.css("width", btnWidth);
        }
    }
    $(".btn-primary-add").click(function() {addBtnMessage($(this), "Adding..."); });
    $(".btn-primary-folder").click(function() {addBtnMessage($(this), "Adding..."); });
    $(".btn-primary-search").click(function() {addBtnMessage($(this), "Searching..."); });   
 
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
        $("#folder-page-search-button").removeClass("disabled");
        var nMatches = 0;
        $( ".draggable" ).each (function() {
            if (textAppearsIn($("#bookmarks-filter").val(), $(this).text())) {
                $(this).show();
                nMatches++
            } else {
                $(this).hide();
            }
        });
        if (nMatches == 0) {  // If no matches were found
            $("#folder-page-search-button-div").css("display", "block");
            $("#folder-search-query").text($("#bookmarks-filter").val());
            $("#folder-page-search-button").attr("href", "/userpage/" + encodeURIComponent($("#bookmarks-filter").val()));
        } else {
            $("#folder-page-search-button-div").css("display", "none");
        }
    });
 
    var elementsToHighlightOnDrag = $(".bin span, .dd-folder-icon");
    
    // Highlight bin and folders when a bookmark or search result is being dragged
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

    // Save changes when a bookmark is moved to a new position on the list
    var sortStop = function(event, ui) {
        dragStop(event, ui);
        
        // Only change order if not hovering over a folder or bin
        if (hoveringOverDroppable) { // We've just dropped to a folder, so don't change rank
            $(this).sortable('cancel');
        } else {
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

    // Call the function defined below that makes the
    // droppable folders and bin icon functional
    makeDroppable();
 
    // When the user clicks on the button to add a folder, make a POST
    // request to create the folder
    $("#add-folder-button")
        .click(function() {
             var folderName = $("#new-folder-name-input").val();
             var addFolderButton = $(this);             
             $.post("/ajax-create-folder/",
             { folderName: folderName },
             function(data) {
                $("#folder-add-message").text(data);
                addFolderButton.removeClass("disabled");
                addFolderButton.html('<span class="glyphicon glyphicon-plus"/>');
                if (data === "Folder created") {
                    $("#folder-list").append(makeNewFolderElement(folderName));
                    makeDroppable();
                    makeFoldersDeleteable();
                }
                $("#new-folder-name-input").val("");
             })
                .fail(function() {
                   $("#folder-add-message")
                       .text("An error occurred when attempting to add the folder. Please try again.");
                        addFolderButton.removeClass("disabled");
                        addFolderButton.html('<span class="glyphicon glyphicon-plus"/>');
                   });
    });
 
 
    // Delete a bookmark when user clicks the X
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
 
    // Call the function below that set up the functionality for deleting folders
    makeFoldersDeleteable();
 
    // Add folder when Enter key is pressed
    $("#new-folder-name-input").keyup(function(event){
        if(event.keyCode == 13){
            $("#add-folder-button").click();
        }
    });
 
    // Set up the dropdown menu actions
    $(".dropdown-to-folder, .dropdown-to-bin").click(function(event) {
        event.preventDefault();  // Prevent default "a" element click action
        var clickedItem = $(this);
        var dropDownButton = clickedItem.parent().parent().prev();
        var dropDownHtml = dropDownButton.html();
        dropDownButton.css("width", dropDownButton.css("width"));     // Make sure width doesn't change
        dropDownButton.css("height", dropDownButton.css("height"));   // Make sure height doesn't change
        var url = clickedItem.attr("data-url");
        if (clickedItem.hasClass("dropdown-to-folder")) {
            var folderName = clickedItem.text();
            ajaxAddToFolder(url,
                            folderName,
                            function() {dropDownButton.text("Added!");
                                        dropDownButton.parent().parent().addClass("saved-bookmark");
                                        window.setTimeout(function() {
                                            dropDownButton.html(dropDownHtml);
                                        }, 800);
                                       },
                            function() {alert("There was a problem adding to the folder.")});
        } else {
            ajaxAddToBin(url,
                            function() {dropDownButton.text("Added!");
                                        window.setTimeout(function() {
                                            // Hide the bookmark that has been binned
                                            dropDownButton.parent().parent().slideUp();
                                        }, 400);
                                       },
                            function() {alert("There was a problem adding to the bin folder.")});
        }
    });
    
    
    // If a bookmark has just been added by pasting URL, make it glow
    var bgOpacity = 0.15;
    var decInterval, incInterval;
    var decreaseOpacity = function () {
        if (bgOpacity > 0.7) {
            bgOpacity -= 0.02;
        } else {
            bgOpacity -= 0.05;
        }
        $(".just-added").css("background-color", "rgba(255,255,50," + bgOpacity + ")");
        if (bgOpacity < 0.2) {
            $(".just-added").css("background-color", "rgba(255,255,50,.15)");
            clearInterval(decInterval);
        }
    }
    var increaseOpacity = function () {
        bgOpacity += 0.05;
        $(".just-added").css("background-color", "rgba(255,255,50," + bgOpacity + ")");
        if (bgOpacity > 0.9) {
            clearInterval(incInterval);
            decInterval = setInterval(decreaseOpacity, 30);
        }
    }
    var incInterval = setInterval(increaseOpacity, 30);
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

// This is called when a user drops a bookmark to a folder.
// An Ajax POST request is made, and success or failure messages are shown 
function ajaxDropToFolder(dropTarget, ui) {
    var folderIcon = dropTarget.find(".dd-folder-icon").not(".keep-folder-open");
    var url = ui.draggable.find("strong").find("a").attr("href");
    var title = ui.draggable.find("strong").find("a").text();
    var folderName = dropTarget.find(".folder-name").first().text();
    ajaxAddToFolder(url,
                    folderName,
                    function(messageFromPython) {
                      dropTarget.find(".folder-message").html( "<br>" + messageFromPython );
                      folderIcon
                          .removeClass( "glyphicon-folder-open" )  
                          .addClass( "glyphicon-folder-close" );
                      ui.draggable.addClass("saved-bookmark");
                      // Add to list of latest bookmarks
                      if ($('#latest-five').find('a[href="' + url + '"]').length == 0) {
                          if ($('#latest-five').find('li').length == 0) {
                              var new_li = $('<li></li>')
                              $('#latest-five').append(new_li);
                              new_li.append('<a href="' + url + '" target="_blank">' + title + '</a>');
                          } else {
                              $('<li><a href="' + url + '" target="_blank">' + title + '</a></li>')
                                  .insertBefore($('#latest-five').find("li").first());   
                            if ($('#latest-five').find('li').length > 5) {
                              $('#latest-five').find('li').last().remove();
                            }                
                          }
                          $('.top-five-heading').css('display', 'block');
                      }
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

// This is called when a user drops a bookmark to the bin folder.
// An Ajax POST request is made, and success or failure messages are shown  
function ajaxDropToBin(dropTarget, ui) {
    var folderIcon = dropTarget.find(".dd-folder-icon").not(".keep-folder-open");
    var url = ui.draggable.find("strong").find("a").attr("href");
    ajaxAddToBin(url,
                 function(messageFromPython) {
                      dropTarget.find(".folder-message").text( messageFromPython );
                      ui.draggable.addClass("saved-bookmark")
                      ui.draggable.slideUp();
                      // Remove from list of latest bookmarks
                      $('#latest-five').find('a[href="' + url + '"]').parent().remove();
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
       + ' <a href="/' + encodeUrl(folderName) + '/">'
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



// Set up folders to receive dropped bookmarks and to call
// the Ajax POST functions
function makeDroppable() {
    $( ".droppable" ).droppable({
        over: function( event, ui ) {
            $( this ).find(".dd-folder-icon").not(".keep-folder-open")
                .removeClass( "glyphicon-folder-close" )
                .addClass( "glyphicon-folder-open" );
            $( this ).find(".glyphicon").addClass("highlight-droppable-hover");
            // We will only allow re-ordering of bookmarks if the user isn't
            // about to drop onto a folder or the bin
            hoveringOverDroppable = true;
        },
        out: function( event, ui ) {
            $( this ).find(".dd-folder-icon").not(".keep-folder-open")
                .removeClass( "glyphicon-folder-open" )
                .addClass( "glyphicon-folder-close" );
            $( this ).find(".glyphicon").removeClass("highlight-droppable-hover");
            hoveringOverDroppable = false;
        },
        tolerance: "pointer",
        drop: function( event, ui ) {
            var dropTarget = $(this);
            dropTarget.find(".folder-message").html( "<br>Adding link..." );                         
            dropTarget.find(".glyphicon").removeClass("highlight-droppable-hover");
            if (dropTarget.hasClass("bin")) {
                ajaxDropToBin(dropTarget, ui);
            } else {
                ajaxDropToFolder(dropTarget, ui); 
            }
            // Wait a moment before allowing sorting of bookmarks.
            // This will prevent accidentally re-ordering when the user drops to a folder
            setTimeout(function() {hoveringOverDroppable = false}, 200)
        }
    });
}

 
// Saved the changed bookmark rank in the HTML element's data attribute and in the database
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
 

// Show the delete folder buttons only on hover 
$( "#folder-box" ).mouseover(function() {
  $( ".delete-folder" ).show();
});
$( "#folder-box" ).mouseout(function() {
  $( ".delete-folder" ).hide();
});
 
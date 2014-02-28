$(function() {

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
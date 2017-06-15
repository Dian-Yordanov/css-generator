
 $( document ).ready(function() {
     var checkboxes = document.getElementsByTagName('input');

for (var i=0; i<checkboxes.length; i++)  {
  if (checkboxes[i].type == 'checkbox')   {
    checkboxes[i].checked = false;
  }
}

$( "#dialogAddNewCssFunction" ).dialog({ autoOpen: false });

     // jQuery(document).ready(function($){
$('#webpageexampleId').iframeTracker({
    blurCallback: function(){
        console.log('dfsdf');
        $('<div class="alert alert-info">').html('Click on iframe : #' + this._overId).appendTo('#consoleDebug').delay(3000).fadeOut();
        // Do something when the iframe is clicked (like firing an XHR request)
    }
});
    // });
     
});


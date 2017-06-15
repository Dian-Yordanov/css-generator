
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

			this._overId = $(element).parents('.webpageexampleId').attr('id'); // Saving the iframe wrapper id
			console.log(this._overId);
			console.log(this.id);

			// Do something when iframe is clicked (like firing an XHR request)
			// You can know which iframe element is clicked via this._overId
		},
		overCallback: function(element){
			this._overId = $(element).parents('.webpageexampleId').attr('id'); // Saving the iframe wrapper id
			console.log(this._overId);
			console.log(this.id);

		},
		outCallback: function(element){
			this._overId = null; // Reset hover iframe wrapper id
		},
		_overId: null
	});

	 window.addEventListener("message", function(event) {
    console.log("Hello from " + event.data);
});

        // $('<div class="alert alert-info">').html('Click on iframe : #' + this._overId).appendTo('#consoleDebug').delay(3000).fadeOut();
        // Do something when the iframe is clicked (like firing an XHR request)

    // });
     
});


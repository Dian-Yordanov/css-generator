
 $( document ).ready(function() {
     var checkboxes = document.getElementsByTagName('input');

for (var i=0; i<checkboxes.length; i++)  {
  if (checkboxes[i].type == 'checkbox')   {
    checkboxes[i].checked = false;
  }
}

$( "#dialogAddNewCssFunction" ).dialog({ autoOpen: false });

     
});


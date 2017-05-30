var obj;
var w;
const MAX_SENSORS = 4;
const SLEEPING = 0;
const ACTIVE = 1;
const OFFLINE = 2;
const ALARM = 3;
const OFF = 0;
const ON = 1;

window.onload = function() {
    document.getElementById("Black").checked = false;
    document.getElementById("White").checked = false;
    document.getElementById("Pointer").checked = false;
    document.getElementById("specific").checked = false;
    document.getElementById("DarkMinimalisticScrollbar").checked = false;
    document.getElementById("YouTubeCustomColors").checked = false;

}

function mutuallyExclusive(id, id1) {
    var c = document.getElementById(id);
    if (c.checked == true) {
        document.getElementById(id1).checked = false;
    }
}

function Black(checkbox) {
    mutuallyExclusive("Black","White");
    if (checkbox.checked) {
        $.get("api/foo/?a=Blackon", function(response) {});
    }
    if (!checkbox.checked) {
        $.get("api/foo/?a=Blackoff", function(response) {});
    }
}

  function White(checkbox) {
      mutuallyExclusive("White","Black");
    if (checkbox.checked) {
        $.get("api/foo/?a=Whiteon", function(response) {});
    }
    if (!checkbox.checked) {
        $.get("api/foo/?a=Whiteoff", function(response) {});
    }
}

function Pointer(checkbox) {
    if (checkbox.checked) {
        $.get("api/foo/?a=Pointeron", function(response) {});
    }
    if (!checkbox.checked) {
        $.get("api/foo/?a=Pointeroff", function(response) {});
    }
}

  function specific(checkbox) {
    if (checkbox.checked) {
        $.get("api/foo/?a=specificon", function(response) {});
    }
    if (!checkbox.checked) {
        $.get("api/foo/?a=specificoff", function(response) {});
    }
}

function generateCss() {
        $.get("api/foo/?a=generateCss", function(response) {});
        document.getElementById('webpageexampleId').src = document.getElementById('webpageexampleId').src
}
function getCssFromJson() {
        $.get("api/foo/?a=getCssFromJson", function(response) {});
}
function resetCss() {
        $.get("api/foo/?a=resetCss", function(response) {});
        document.getElementById("White").checked = false;
        document.getElementById("Black").checked = false;
        document.getElementById("Pointer").checked = false;
        document.getElementById("specific").checked = false;
}

function colourPickerFunction() {
    var x = document.getElementById("myColor").value;
    document.getElementById("demo").innerHTML = x;
    var y = "api/foo/?a=colour".concat(x).replace(/#/g, "")
    $.get(y, function(response) {});
}

function DarkMinimalisticScrollbar(checkbox) {
    if (checkbox.checked) {
        $.get("api/foo/?a=DarkMinimalisticScrollbaron", function(response) {});
    }
    if (!checkbox.checked) {
        $.get("api/foo/?a=DarkMinimalisticScrollbaroff", function(response) {});
    }
}
function YouTubeCustomColors(checkbox) {
    if (checkbox.checked) {
        $.get("api/foo/?a=YouTubeCustomColorson", function(response) {});
    }
    if (!checkbox.checked) {
        $.get("api/foo/?a=YouTubeCustomColorsoff", function(response) {});
    }
}


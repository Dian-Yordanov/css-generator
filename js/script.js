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
    document.getElementById("embededModifications").checked = false;
    document.getElementById("facebookSpecificModifications").checked = false;
    document.getElementById("redditSpecificModifications").checked = false;


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
function showGeneratedCss(typeOfCssFile) {
    
    var newWindow = window.open('htmlPages',typeOfCssFile.id,'width=1100,height=1000');
    newWindow.my_special_setting = typeOfCssFile.id;

    window.somefunction = function(){
        // alert('sdasdas');
        location.reload();
    }
    
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
function embededModifications(checkbox) {
    if (checkbox.checked) {
        $.get("api/foo/?a=embededModificationson", function(response) {});
    }
    if (!checkbox.checked) {
        $.get("api/foo/?a=embededModificationsoff", function(response) {});
    }
}
function facebookSpecificModifications(checkbox) {
    if (checkbox.checked) {
        $.get("api/foo/?a=facebookSpecificModificationson", function(response) {});
    }
    if (!checkbox.checked) {
        $.get("api/foo/?a=facebookSpecificModificationsoff", function(response) {});
    }
}
function redditSpecificModifications(checkbox) {
    if (checkbox.checked) {
        $.get("api/foo/?a=redditSpecificModificationson", function(response) {});
    }
    if (!checkbox.checked) {
        $.get("api/foo/?a=redditSpecificModificationsoff", function(response) {});
    }
}


// var site = 'http://www.reddit.com/'
// document.getElementById('webpageexampleId').src = site;

var iframe1;

function setiFrame(iframe){
    iframe1 = iframe;
}

function getiFrame(){
    return iframe1;
}

var getData = function (data) {
        var iframe = getiFrame();
        if (data && data.query && data.query.results && data.query.results.resources && data.query.results.resources.content
            && data.query.results.resources.status == 200) loadHTML(data.query.results.resources.content, iframe);
        else if (data && data.error && data.error.description) loadHTML(data.error.description, iframe);
        else loadHTML('Error: Cannot load ' + url, iframe);
    };
var loadURL = function (src, iframe) {
    url = src;
    setiFrame(iframe);
    var script = document.createElement('script');
    script.src = 'http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20data.headers%20where%20url%3D%22'
        + encodeURIComponent(url) + '%22&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback=getData';
    document.body.appendChild(script);
};
var loadHTML = function (html, iframe) {
    iframe.src = 'about:blank';
    iframe.contentWindow.document.open();

    var linkToStaticCss = "<link ".concat('rel="stylesheet" ').concat('type="text/css" ').concat('href="/static/data.css" />');
    var htmlText = html.replace(/<head>/i, '<head><base href="' + url + '"><scr'
        + 'ipt>document.addEventListener("click", function(e) { if(e.target && e.target.nodeName == "A") ' +
        '{ e.preventDefault(); parent.loadURL(e.target.href); } });</scr' + 'ipt>');

    htmlText = htmlText.replace('<!doctype html>', '<!DOCTYPE html>');
    htmlText = htmlText.replace('<!DOCTYPE html>', '<!DOCTYPE html><link rel="stylesheet" type="text/css" href="/static/data.css" />');
    
    // console.log(linkToStaticCss);
    console.log(htmlText);

    iframe.contentWindow.document.write(htmlText);
    iframe.contentWindow.document.close();
}

function GoToWebsite1(){
    var iframe = document.getElementById('webpageexampleId');
    var site = 'https://www.theguardian.com/';
    loadURL(site, iframe);
}
function GoToWebsite2(){
    var iframe = document.getElementById('webpageexampleId');
    var site = 'https://www.reddit.com/';
    loadURL(site, iframe);
}

function GoToWebsite3(){
    var iframe = document.getElementById('webpageexampleId');
    var site = 'https://www.youtube.com/';
    loadURL(site, iframe);
}

function GoToWebsite4(){
    var iframe = document.getElementById('webpageexampleId');
    var site = 'https://www.facebook.com/';
    loadURL(site, iframe);
}

function completeAndRedirect(edit){
    var iframe = document.getElementById('webpageexampleId');
    var site = edit.value;
    loadURL(site, iframe);
    // alert(edit.value);
}

function callParentWindowToEditCss(typeOfCssFile){

    var newWindow = window.open('htmlPages',typeOfCssFile.id,'width=1100,height=1000');
    newWindow.my_special_setting = typeOfCssFile.id;

    window.somefunction = function(){
        location.reload();
    }

}

function GetExternalCss(thisDiv) {
    console.log('pressed');
}

function AddNewCssFunction(thisDiv) {
    console.log('AddNewCssFunction');
    $('<div class="iviewer_image_mask" style="background: url(http://somesite.com/path/to/image.jpg);"></div>').appendTo(this.container);
}

function RemoveNewCssFunction(thisDiv) {
    console.log('RemoveNewCssFunction');
}




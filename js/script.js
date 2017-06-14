var obj;
var w;
var AddNewCssFunctionBoolean;

window.onload = function() {
    AddNewCssFunctionBoolean = false;
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


function executeFunctionTest(thisDiv) {
    // console.log('AddNewCssFunction');
    //  console.log('sssssssssss');
    AddNewCssFunctionBoolean = true;
    $( "#dialogAddNewCssFunction" ).dialog( "close" );
    location.reload();
    postSomethingType2( $( "#fieldForDialog" ).val() );
    // $.get("api/foo/?a=AddNewCssFunction"+$( "#dialogAddNewCssFunction" ).value, function(response) {});
}

function postSomethingType2(data) {
    // data="|||"+variableToSendBack+"|||"+"\n"+data;
    var dataToBePosted;
     if(AddNewCssFunctionBoolean == true){
        dataToBePosted = 'AddNewCssFunction'+'|||SPLITTER|||' + data;
        }
    if(AddNewCssFunctionBoolean == false){
        dataToBePosted = 'RemoveNewCssFunction'+'|||SPLITTER|||' + data;
        }
  $.post('/api2', {javascript_data: dataToBePosted}, function(result) {

  });
}

function AddNewCssFunction(thisDiv) {
    $( "#dialogAddNewCssFunction" ).dialog( "open" );

}

function RemoveNewCssFunction(thisDiv) {
    AddNewCssFunctionBoolean = false;
    location.reload();
    postSomethingType2('NODATA');

}

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
    if (iframe === 'null') { iframe = document.getElementById('webpageexampleId');
    }
    iframe = document.getElementById('webpageexampleId');
    // if(Object.keys(iframe).length === 0 && iframe.constructor === Object){}
    // var iframe2 = iframe;
    // iframe2.src = 'about:blank';
    // iframe2.src = '';
    // iframe2.src = iframe.src;
    // iframe2.attr('src', '');
    iframe.contentWindow.document.open();

    // var linkToStaticCss = "<link ".concat('rel="stylesheet" ').concat('type="text/css" ').concat('href="/static/data.css" />');
    var htmlText = html.replace(/<head>/i, '<head><base href="' + url + '"><scr'
        + 'ipt>document.addEventListener("click", function(e) { if(e.target && e.target.nodeName == "A") ' +
        '{ e.preventDefault(); parent.loadURL(e.target.href); } });</scr' + 'ipt>');

    // headers.append('Access-Control-Allow-Origin', 'http://localhost:5000');
    // headers.append('Access-Control-Allow-Credentials', 'true');

    htmlText = htmlText.replace('<!doctype html>', '<!DOCTYPE html>');
    // htmlText = htmlText.replace('<!DOCTYPE html>', '<!DOCTYPE html><link rel="stylesheet" type="text/css" href="/static/data.css" />');
        htmlText = htmlText.replace
        ('<!DOCTYPE html>', '<!DOCTYPE html><link rel="stylesheet" type="text/css" href="/static/data.css" /><?php header("Access-Control-Allow-Origin: http://localhost:5000"); ?><?php header("Access-Control-Allow-Credentials: true"); ?>');



    // console.log(linkToStaticCss);
    console.log(htmlText);

    iframe.contentWindow.document.write(htmlText);
    iframe.contentWindow.document.close();
}

function getCssFromStylish(thisDiv) {

  if (performance === undefined) {
    console.log("= Calculate Load Times: performance NOT supported");
    return;
  }

  var resources = performance.getEntriesByType("resource");
  if (resources === undefined || resources.length <= 0) {
    console.log("= Calculate Load Times: there are NO `resource` performance records");
    return;
  }

  console.log("= Calculate Load Times");
  for (var i=0; i < resources.length; i++) {
    console.log("== Resource[" + i + "] - " + resources[i].name);
    // Redirect time
    // var t = resources[i].redirectEnd - resources[i].redirectStart;
    // console.log("... Redirect time = " + t);
    //
    // // DNS time
    // t = resources[i].domainLookupEnd - resources[i].domainLookupStart;
    // console.log("... DNS lookup time = " + t);
    //
    // // TCP handshake time
    // t = resources[i].connectEnd - resources[i].connectStart;
    // console.log("... TCP time = " + t);
    //
    // // Secure connection time
    // t = (resources[i].secureConnectionStart > 0) ? (resources[i].connectEnd - resources[i].secureConnectionStart) : "0";
    // console.log("... Secure connection time = " + t);
    //
    // // Response time
    // t = resources[i].responseEnd - resources[i].responseStart;
    // console.log("... Response time = " + t);
    //
    // // Fetch until response end
    // t = (resources[i].fetchStart > 0) ? (resources[i].responseEnd - resources[i].fetchStart) : "0";
    // console.log("... Fetch until response end time = " + t);
    //
    // // Request start until reponse end
    // t = (resources[i].requestStart > 0) ? (resources[i].responseEnd - resources[i].requestStart) : "0";
    // console.log("... Request start until response end time = " + t);
    //
    // // Start until reponse end
    // t = (resources[i].startTime > 0) ? (resources[i].responseEnd - resources[i].startTime) : "0";
    // console.log("... Start until response end time = " + t);
  }

}

function callParentWindowToGetCss(typeOfCssFile){

    // var newWindow = window.open('htmlPages',typeOfCssFile.id,'width=1100,height=1000');
    // newWindow.my_special_setting = typeOfCssFile.id;
    //
    // window.somefunction = function(){
    //     location.reload();
    // }

    console.log('typeOfCssFile');
    console.log(typeOfCssFile.id);

    if('buttonForLaunchingSecondWindow-Button1'==typeOfCssFile.id){
        var iframe = document.getElementById('webpageexampleId');
        var site = 'https://userstyles.org/';
        loadURL(site, iframe);
    }
    if('buttonForLaunchingSecondWindow-Button2'==typeOfCssFile.id){
        // var iframe = document.getElementById('webpageexampleId');
        // var site = 'https://userstyles.org/styles/100478/004-diymyfonts-chinese-firefoxchromeedge-catcat520';
        // loadURL(site, iframe);
        // window.open('https://userstyles.org/styles/100478/004-diymyfonts-chinese-firefoxchromeedge-catcat520', 'test', 'width=400, height=400');
        
        var newWindow = window.open('https://userstyles.org/styles/100478/004-diymyfonts-chinese-firefoxchromeedge-catcat520',typeOfCssFile.id,'width=1100,height=1000');
        newWindow.my_special_setting = typeOfCssFile.id;

        window.somefunction = function(){
            location.reload();
        }

    }
}


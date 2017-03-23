// Enable JavaScript's strict mode. Strict mode catches some common
// programming errors and throws exceptions, prevents some unsafe actions from
// being taken, and disables some confusing and bad JavaScript features.
"use strict";

console.log("")
//links to open in new window
$(document).ready(function () {
                var localhost = window.location.host;
                //console.log(localhost)
                var parts = localhost.split(".").slice(-2);
                localhost = parts.join(".");
                $("a").each(function (i) {                    
                    var linkUrl = $(this).attr('href');
                    if (!linkUrl)
                        linkUrl = "";
                    linkUrl=linkUrl.toLowerCase();
                    if(linkUrl.length > 0 && !(linkUrl.charAt(0)=='/') && !(linkUrl.charAt(0)=='#') && !(linkUrl.indexOf('mailto')==0)
                        && !(linkUrl.indexOf('javascript')==0) && !(linkUrl.indexOf(localhost)>-1)) {
                        // now we have an external website as link.
                        $(this).attr('target','_blank');
                    }
                });
   });

//open links in new window and close elements with class modal
$(function () {
    $(".custom-close").on('click', function() {
        $('.modal').modal('hide');
    });
});



//ckan.module('message_target', function ($, _) {
//  return {
//    initialize: function () {
//      console.log("I've been initialized for element")
//    }
//  };
//});

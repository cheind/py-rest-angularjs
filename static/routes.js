'use strict';

/* 
All AngularJS local routes are defined here. 

Note, adding a route here requires the same route to be added 
to the backend (flask / aiohttp), Otherwise calling 'localhost/xx' 
will be handled by the backend and not AngularJS.
*/
angular
.module('demoapp')
.config(['$locationProvider', '$routeProvider', function($locationProvider, $routeProvider) {    
    $routeProvider
    .when("/", {
        templateUrl : "static/main.html",
        controller : "RestAPICtrl"
    })
    $locationProvider.html5Mode(true);                   
}]);
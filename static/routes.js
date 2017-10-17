'use strict';

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
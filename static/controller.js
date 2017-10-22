'use strict';

/*
A controller for 'main.html' page that handles communication with the 
REST API exposed by the Python backend.
*/
angular.module('demoapp')
.controller('RestAPICtrl',  ['$scope', '$http', function($scope, $http) {

    $scope.message = null;
    $scope.name = 'Anonymous'

    $scope.greet = function(){
        $http
        .get('/api/greet/' + $scope.name) // invoke backend API
        .then(function(response) {
            $scope.message = response.data['message'];
        });
    }

}]);
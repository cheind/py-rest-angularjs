'use strict';

angular.module('demoapp')
.controller('RestAPICtrl',  ['$scope', '$http', function($scope, $http) {

    $scope.result = null;

    $scope.invokeAPI = function(){
        $http.get('/api').
            then(function(response) {
                $scope.result = response.data;
            });
    }

}]);
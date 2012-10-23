'use strict';

function MyCtrl1($scope, $http) {
  $scope.params = {'wctoken': window.WCTOKEN};

  // get person info (in JSON)
  $http.get('/getPersonInfo', {params: $scope.params}).success(function(data) {
    $scope.name = data.name;
  });

  // get weights as array
  $http.get('/getWeightMeasurements', {params: $scope.params}).success(function(data) {
    $scope.weights = data;
  });
}
MyCtrl1.$inject = ['$scope', '$http'];

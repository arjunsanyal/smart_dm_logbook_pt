'use strict';

function Controller($scope, $http) {
  var debug = true;
  if (debug) {
    $scope.name = 'John Doe';
    $scope.weights = [
          {'day': 'Sun', 'count': 1},
          {'day': 'Mon', 'count': 10},
          {'day': 'Tue', 'count': 3},
          {'day': 'Wed', 'count': 1},
          {'day': 'Thu', 'count': 5},
          {'day': 'Fri', 'count': 1},
          {'day': 'Sat', 'count': 9},
        ]
    } else {
      // get info (in JSON)
      $scope.params = {'wctoken': window.WCTOKEN};
      $http.get('/getPersonInfo', {params: $scope.params})
           .success(function(data) { $scope.name = data.name; })
           .error(function(data, status) { alert('error in getPersonInfo'); })

      $http.get('/getWeightMeasurements', {params: $scope.params})
           .success(function(data) { $scope.weights = data; })
           .error(function(data, status) { alert('error in getWeightMeasurements'); })
  }
};
Controller.$inject = ['$scope', '$http'];

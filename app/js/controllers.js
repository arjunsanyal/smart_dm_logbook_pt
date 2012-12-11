'use strict';

function Controller($scope, $http) {
  $scope.DEBUG = false;
  $scope.master = {};

  $scope.update = function(measurement) {
    $scope.master = angular.copy(measurement);
    measurement['wctoken'] = sessionStorage.getItem('wctoken');
    $http.post('/newGlucoseMeasurement', measurement)
         .success(function(data) { $scope.get_glucoses(); })
  };

  $scope.is_unchanged = function(measurement) {
    return angular.equals(measurement, $scope.master);
  }

  $scope.reset = function() {
    var d = new Date();
    $scope.meas = {
      'month': d.getMonth(),
      'day': d.getDate(),
      'year': d.getFullYear(),
      'hours24': d.getHours(),
      'hours': d.getHours() > 12 ? d.getHours() - 12 : d.getHours(),
      'am_or_pm': d.getHours() > 12 ? 'pm' : 'am',
      'minutes': d.getMinutes(),
      '12_hour_p': true,
      'unit': 'mmol_per_l',
      'whole_or_plasma': 'whole',
      'value': $scope.DEBUG ? 7.5 : null,
    };
  };

  $scope.get_glucoses = function() {
    $http.get('/getGlucoseMeasurements', {params: $scope.params})
         .success(function(data) {
           // todo: have a consistent standard for this array or {}}?
           var glucoses = [];
           data.forEach(function(d) {
             glucoses.push({'when': d[0], 'value': d[1]});
           })
           $scope.glucoses = glucoses;
          })
          .error(function(data, status) { alert('error in getGlucoseMeasurements'); })
  }

  // main init
  $scope.params = {
    'wctoken': sessionStorage.getItem('wctoken'),
    'auth_token': sessionStorage.getItem('auth_token'),
    'shared_secret': sessionStorage.getItem('shared_secret'),
    'record_id': sessionStorage.getItem('record_id')
  };
  $scope.name = sessionStorage.getItem('name');

  if ($scope.DEBUG) {
    $scope.glucoses = [
          {'when': '2012-10-23T08:04:11', 'value': 6.5},
          {'when': '2012-10-23T18:04:11', 'value': 7.9},
          {'when': '2012-10-22T08:04:11', 'value': 5.8},
          {'when': '2012-10-22T18:04:11', 'value': 7.0},
          {'when': '2012-10-21T08:04:11', 'value': 5.9},
          {'when': '2012-10-21T18:04:11', 'value': 6.5},
          {'when': '2012-10-20T08:04:11', 'value': 6.8},
          {'when': '2012-10-20T18:04:11', 'value': 5.3},
          {'when': '2012-10-19T08:04:11', 'value': 6.5},
          {'when': '2012-10-19T18:04:11', 'value': 5.2},
          {'when': '2012-10-18T08:04:11', 'value': 7.6},
          {'when': '2012-10-18T18:04:11', 'value': 8.1},
          {'when': '2012-10-17T08:04:11', 'value': 6.5},
          {'when': '2012-10-17T18:04:11', 'value': 5.8},
          {'when': '2012-10-16T08:04:11', 'value': 6.4},
          {'when': '2012-10-16T18:04:11', 'value': 7.9},
        ]
    } else {
      $scope.get_glucoses();
    }

  $scope.reset();
};

Controller.$inject = ['$scope', '$http'];

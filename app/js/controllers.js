'use strict';

function Controller($scope, $http) {
  $scope.DEBUG = false;
  $scope.master = {};

  $scope.update = function(measurement) {
    $scope.master = angular.copy(measurement);
    measurement['wctoken'] = sessionStorage.getItem('wctoken');

    // convert the 12 hour value to 24 hour
    if (measurement['am_or_pm'] == 'pm') {
      measurement['hours24'] = measurement['hours'] + 12;
    } else {
      measurement['hours24'] = measurement['hours'];
    }

    $http.post('/newGlucoseMeasurement', measurement)
         .success(function(data) { $scope.get_glucoses(); })
  };

  $scope.is_unchanged = function(measurement) {
    return angular.equals(measurement, $scope.master);
  }

  $scope.reset = function() {
    var d = new Date();
    $scope.meas = {
      'month': d.getMonth() + 1, // Mistakes were made: January is month 0!
      'day': d.getDate(),
      'year': d.getFullYear(),
      'hours24': d.getHours(),
      'hours': d.getHours() > 12 ? d.getHours() - 12 : d.getHours(),
      'am_or_pm': d.getHours() > 12 ? 'pm' : 'am',
      'minutes': d.getMinutes(),
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
  $scope.get_glucoses();
  $scope.reset();
};

Controller.$inject = ['$scope', '$http'];

'use strict';

// simplified module definition: no filters, services, or directives
// and only one view without a parital. It's also configured with
// alternate interpolation delimiters as to not conflict with Django
angular.module('myApp', [])
  .config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/view1')
    $routeProvider.otherwise({redirectTo: '/view1'});
  }])
  .config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
  });

// Declare app level module which depends on filters, and services
//angular.module('myApp', ['myApp.filters', 'myApp.services', 'myApp.directives']).
//  config(['$routeProvider', function($routeProvider) {
//    $routeProvider.when('/view1', {templateUrl: 'partials/partial1.html', controller: MyCtrl1});
//    $routeProvider.when('/view2', {templateUrl: 'partials/partial2.html', controller: MyCtrl2});
//    $routeProvider.otherwise({redirectTo: '/view1'});
//  }]);

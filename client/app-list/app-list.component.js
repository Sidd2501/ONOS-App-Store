'use strict';

// Register `app-list` component, along with its associated controller and template
angular.
  module('app').
  component('app-list', {
    templateUrl: 'app-list/app-list.template.html',
    controller: ['$http',
      function AppListController($http) {

        vat ctrl = this;
        this.a = 'test';

      	$http.get('localhost:5000/api/apps')
      	.then(function(data){
      		console.log(data);
          ctrl.apps = data.apps;
      	})
      	.catch(function(e){
      		console.log(e);
      	}); 
      }
    ]
  });
angular
  .module('app')
  .component('appList', {
    templateUrl: 'app/hello.html',
    controller: ['$http',
      function AppController($http) {
      	var ctrl = this;
        $http.get('http://localhost:5000/api/apps')
      	.then(function(res){
      		ctrl.apps = res.data.apps;
      	})
      	.catch(function(e){
      		console.log('we are here');
      		console.log(e);
      	}); 
      }
    ]
  });

(function() {

    var app = angular.module('MessageApp',['ngRoute']);

    app.config(['$routeProvider', '$locationProvider', function ($routeProvider, $locationProvider, $location) {
        $routeProvider.when('/login', {
            templateUrl: 'pages/login.html',
            controller: 'LoginController',
            controllerAs : 'logingCtrl'
        }).when('/register', {
            templateUrl: 'pages/register.html',
            controller: 'RegisterController',
            controllerAs : 'registerCtrl'
        }).when('/register', {
            templateUrl: 'pages/register.html',
            controller: 'RegisterController',
            controllerAs : 'registerCtrl'
        }).when('/users/:pid/mygroups', {
            templateUrl: 'pages/mygroups.html',
            controller: 'MyGroupsController',
            controllerAs : 'mygroupsCtrl'
        }).when('/groups/:gid/messages', {
            templateUrl: 'pages/groupmessages.html',
            controller: 'GroupMessagesController',
            controllerAs : 'groupMessagesCtrl'
        }).when('/chat', {
            templateUrl: 'pages/chat.html',
            controller: 'ChatController',
            controllerAs : 'chatCtrl'
        }).otherwise({
            redirectTo: '/login'
        });
    }]);

})();

var app = angular.module('myApp', []);
app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});
app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
}]);
app.controller('HeaderController', function($scope, $location, $anchorScroll) {
    $scope.Alllist = "";
    $scope.list1 = "";
    $scope.list2 = "hidden";
    $scope.blocklink = function() {
        $scope.list1 = "hidden";
        $scope.list2 = "";
    };
    $scope.hiddenlink = function() {
        $scope.list1 = "";
        $scope.list2 = "hidden";
    };
});
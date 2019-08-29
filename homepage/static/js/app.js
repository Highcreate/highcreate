var app = angular.module('myApp', []);
app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});

app.controller('AppController', function($scope) {

    $scope.username = '';

    $scope.users = [];

    $scope.addlink = function() {
        console.log('1', $scope.username);

        if (!$scope.username) return;

        $scope.users.push({
            username: $scope.username,
            url: '//twitter.com/' + $scope.username
        });

        //$scope.username =  '';
        //$scope.password =  '';
    };

    $scope.deleteUser = function(index) {
        $scope.users.splice(index, 1);
    };
});
app.controller('HeaderController', function($scope, $location, $anchorScroll) {
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

    $scope.gotomap = function(id) {
        // set the location.hash to the id of
        // the element you wish to scroll to.
        $location.url('index.html');
        //$location.absUrl() == 'C:/Users/z64113zz/Desktop/test/realsase2/'
        //$location.path('/index.html');


        var ed = $location.hash();
        $location.hash(id);
        $anchorScroll();
        $location.hash(ed);
    };

});


app.controller('ScrollController', function($scope, $location, $anchorScroll) {

    $scope.gotoBottom = function(id) {
        // set the location.hash to the id of
        // the element you wish to scroll to.
        var ed = $location.hash();
        $location.hash(id);
        $anchorScroll();
        $location.hash(ed);
    };
});
app.directive("scroll", function($window) {
    return function($scope) {
        angular.element($window).bind("scroll", function() {
            if (this.pageYOffset >= 500 && this.pageYOffset < 1000) {
                $scope.frame1 = "fade-in";
                $scope.leftenter1 = "left-enter";
                $scope.centerenter1 = "center-enter";
                $scope.rightenter1 = "right-enter";
                //console.log(this.pageYOffset);
            } else if (this.pageYOffset >= 1000 && this.pageYOffset < 1500) {
                $scope.frame2 = "fade-in";
                $scope.leftenter2 = "left-enter";
                $scope.centerenter2 = "center-enter";
                $scope.rightenter2 = "right-enter";
               // console.log(this.pageYOffset);
            } else if (this.pageYOffset >= 1500) {
                $scope.frame3 = "fade-in";
                $scope.leftenter3 = "left-enter";
                $scope.centerenter3 = "center-enter";
                $scope.rightenter3 = "right-enter";
                //console.log(this.pageYOffset);
            } else {
                //console.log(this.pageYOffset);
            }
            $scope.$apply();
        });
    };
});
var app = angular.module('myApp', []);
app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});
app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
}]);
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
    $scope.gotoBottom = function(id) {
        var ed = $location.hash();
        $location.hash(id);
        $anchorScroll();
        $location.hash(ed);
    };
});

app.controller('ScrollController', function($scope, $location, $anchorScroll) {
    $scope.init = function(id) {
        var ed = $location.hash();
        $location.hash(id);
        $anchorScroll();
        $location.hash(ed);
    };
    $scope.gotoBottom = function(id) {
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
            } else if (this.pageYOffset >= 1000 && this.pageYOffset < 1500) {
                $scope.frame2 = "fade-in";
                $scope.leftenter2 = "left-enter";
                $scope.centerenter2 = "center-enter";
                $scope.rightenter2 = "right-enter";
            } else if (this.pageYOffset >= 1500) {
                $scope.frame3 = "fade-in";
                $scope.leftenter3 = "left-enter";
                $scope.centerenter3 = "center-enter";
                $scope.rightenter3 = "right-enter";
            }
            $scope.$apply();
        });
    };
});

app.controller('footerController', function($scope, $location, $anchorScroll) {
    $scope.gotoBottom = function(id) {
        var ed = $location.hash();
        $location.hash(id);
        $anchorScroll();
        $location.hash(ed);
    };
});

app.controller('Ctrl', function($scope, $http) {
    $scope.sendMail = function() {
        if ($scope.hsForm.$invalid != true) {
            $http.post('/SendMail/', {
                fromemail: $scope.user.email,
                company: $scope.user.company + ' from ' + $scope.user.name,
                text: $scope.user.message
            }).then(res => {
                $scope.user.email = "";
                $scope.user.company = "";
                $scope.user.name = "";
                $scope.user.message = "";
                $scope.sendmailresult = "メールを送信しました。";
            });
        }
        $scope.sendmailresult = "";
    };
});
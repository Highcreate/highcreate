// app.js

var app = angular.module('myApp', []).config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
    });

app.controller('AppController', function($scope) {
    // 入力されたユーザー名を保持
    $scope.username = '';
    // ユーザー一覧（空の配列で初期化）
    $scope.users = [];
    // 登録を押されたときの関数
    $scope.submit = function() {
        console.log('1', $scope.username);
      // 空だったら何もしない
      if (!$scope.username) return;
      // 新しいユーザーをユーザー一覧に登録する
      $scope.users.push({
        username: $scope.username,
        url: '//twitter.com/' + $scope.username
      });
      // 登録完了したらINPUTを空にしておく
      //scope.username =  '';
    };
    // ユーザー一覧からユーザーを削除
    $scope.deleteUser = function(index) {
      $scope.users.splice(index, 1);
    };
  });
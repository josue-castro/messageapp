angular.module('MessageApp').controller('LoginController', ['$http', '$log', '$scope', '$location',
    function($http, $log, $scope, $location) {

        var thisCtrl = this;


        thisCtrl.signin = function(){

            var username = document.getElementById("loginusername").value;
            var password = document.getElementById("loginpassword").value;

            console.log(username);
            console.log(password);

            // Build the data object
            var data = {};
            data.username = username;
            data.password = password;
            console.log(data);

            data = JSON.stringify(data);

            // Now create the url with the route to talk with the rest API
            var reqURL = "http://localhost:5000/MessageApp/login";
            console.log("reqURL: " + reqURL);

            // configuration headers for HTTP request
            var config = {
                headers : {
                  'Content-Type': 'application/json;charset=utf-8;'
                  //  'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8;'
                }
            }

            // Now issue the http request to the rest API
            $http.post(reqURL, data, config).then(
                // Success function
                function (response) {
                    console.log("data: " + JSON.stringify(response.data));
                    // tira un mensaje en un alert
                    //alert("Login attempt: " + response.data);


                    var user_pid = response.data.User.pid;

                    localStorage.setItem("currentLoggedUser", user_pid);
                    localStorage.setItem("currentLoggedUserId", user_pid);
                    localStorage.setItem("currentLoggedUserUsername", response.data.User.username);

                    console.log('/users/'+user_pid+'/mygroups');
                    $location.url('/users/'+user_pid+'/mygroups');
                }, //Error function
                function (response) {
                    // This is the error function
                    // If we get here, some error occurred.
                    // Verify which was the cause and show an alert.
                    console.log(response);
                    var status = response.status;
                    console.log("Error: " + reqURL);
                    alert(response.data.Error);
                    if (status == 0) {
                        alert("No hay conexion a Internet");
                    }
                    else if (status == 401) {
                        alert("Su sesion expiro. Conectese de nuevo.");
                    }
                    else if (status == 403) {
                        alert("No esta autorizado a usar el sistema.");
                    }
                    else {
                        alert("Error interno del sistema.");
                    }
                }
            );
        };

        thisCtrl.goRegister = function() {
            $location.url('/register');
        };



}]);

angular.module('MessageApp').controller('RegisterController', ['$http', '$log', '$scope', '$location',
    function($http, $log, $scope, $location) {

        var thisCtrl = this;


        thisCtrl.register = function(){


            var firstname = document.getElementById("registerfirstname").value;
            var lastname = document.getElementById("registerlastname").value;
            var username = document.getElementById("registerusername").value;
            var phone = document.getElementById("registerphone").value;
            var email = document.getElementById("registeremail").value;
            var password = document.getElementById("registerpassword").value;

            if(phone == null && email == null){

            }else if(phone == null){
                phone = null;
            }else{
                email = null;
            }

            // Build the data object
            var data = {};
            data.firstname = firstname;
            data.lastname = lastname;
            data.username = username;
            data.phone = phone;
            data.email = email;
            data.password = password;

            console.log(data);

            data = JSON.stringify(data);

            console.log(data);

            //$log.error("Message Loaded: ", JSON.stringify(thisCtrl.loginform));

            // Now create the url with the route to talk with the rest API
            var reqURL = "http://localhost:5000/MessageApp/register";
            console.log("reqURL: " + reqURL);

            // configuration headers for HTTP request
            var config = {
                headers : {
                  'Content-Type': 'application/json;charset=utf-8;'
                  //'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8;'
                }
            }

            // Now issue the http request to the rest API
            $http.post(reqURL, data, config).then(
                // Success function
                function (response) {
                    console.log("data: " + JSON.stringify(response.data));
                    // tira un mensaje en un alert
                    alert("Te has registrado exitosamente.");
                    $location.url('/login');
                }, //Error function
                function (response) {
                    // This is the error function
                    // If we get here, some error occurred.
                    // Verify which was the cause and show an alert.
                    var status = response.status;
                    console.log("Error: " + reqURL);
                    alert(response.data.Error);

                    //alert("Cristo");
                    if (status == 0) {
                        alert("No hay conexion a Internet");
                    }else if (status == 400) {
                        alert("Tienes algún error con tu información.");
                    }
                    else if (status == 401) {
                        alert("Su sesion expiro. Conectese de nuevo.");
                    }
                    else {
                        alert("Error interno del sistema.");
                    }
                }
            );
        };

        thisCtrl.goLogin = function() {
            $location.url('/login');
        };


        //this.loadMessages();
}]);

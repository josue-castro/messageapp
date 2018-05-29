angular.module('MessageApp').controller('GroupMessagesController', ['$http', '$log', '$scope', '$location', '$routeParams',
    function($http, $log, $scope, $location, $routeParams) {

        var thisCtrl = this;

        this.likesList = {};
        this.dislikesList = {};
        this.counter = 2;
        this.newText = "";
        this.gid = $routeParams.gid;

        if(localStorage.getItem("currentLoggedUser")==null){
            $location.url('/login');
        }


        this.username = localStorage.getItem("currentLoggedUserUsername");

        this.messages = function(){

            var loggedUser = localStorage.getItem("currentLoggedUser");

            var url = "http://localhost:5000/MessageApp/groups/"+thisCtrl.gid+"/messages";
            console.log("http://localhost:5000/MessageApp/groups/"+thisCtrl.gid+"/messages");

            $http.get(url).then(// success call back
                function (response){

                    console.log("response: " + JSON.stringify(response.data));
                    console.log(response.data.Messages_in_group);

                    thisCtrl.messageList = response.data.Messages_in_group;
                    console.log(thisCtrl.messageList);
            },
            function (response){

                var status = response.status;
                if (status == 0){
                    alert("No hay conexion a Internet");
                }
                else if (status == 401){
                    alert("Su sesion expiro. Conectese de nuevo.");
                }
                else if (status == 403){
                    alert("No esta autorizado a usar el sistema.");
                }
                else if (status == 404){
                    alert("No se encontro la informacion solicitada.");
                }
                else {
                    alert("Error interno del sistema.");
                }
            });

        };

        this.loadMessages = function(gid){
            $location.url('/MessageApp/groups/'+gid+'/messages');
        };

        this.loadLikes = function(mid){

            var url = "http://localhost:5000/MessageApp/messages/"+mid+"/likes";
            console.log("http://localhost:5000/MessageApp/messages/"+mid+"/likes");

            $http.get(url).then(
                function (response){

                    console.log("response: " + JSON.stringify(response.data));
                    console.log(response.data.Likes);

                    thisCtrl.likesList[mid] = response.data.Likes;
            },
            function (response){

                var status = response.status;
                if (status == 0){
                    alert("No hay conexion a Internet");
                }
                else if (status == 401){
                    alert("Su sesion expiro. Conectese de nuevo.");
                }
                else if (status == 403){
                    alert("No esta autorizado a usar el sistema.");
                }
                else if (status == 404){
                    alert("No se encontro la informacion solicitada.");
                }
                else {
                    alert("Error interno del sistema.");
                }
            });


        };

        this.loadDislikes = function(mid){

            var url = "http://localhost:5000/MessageApp/messages/"+mid+"/dislikes";
            console.log("http://localhost:5000/MessageApp/messages/"+mid+"/dislikes");

            $http.get(url).then(
                function (response){

                    console.log("response: " + JSON.stringify(response.data));
                    console.log(response.data.Dislikes);

                    thisCtrl.dislikesList[mid] = response.data.Dislikes;
            },
            function (response){

                var status = response.status;
                if (status == 0){
                    alert("No hay conexion a Internet");
                }
                else if (status == 401){
                    alert("Su sesion expiro. Conectese de nuevo.");
                }
                else if (status == 403){
                    alert("No esta autorizado a usar el sistema.");
                }
                else if (status == 404){
                    alert("No se encontro la informacion solicitada.");
                }
                else {
                    alert("Error interno del sistema.");
                }
            });


        };

        thisCtrl.postLike = function(mid){

            var loggedUser = localStorage.getItem("currentLoggedUser");

            // Build the data object
            var data = {};
            data.pid = loggedUser;

            console.log(data);

            data = JSON.stringify(data);

            console.log(data);

            //$log.error("Message Loaded: ", JSON.stringify(thisCtrl.loginform));

            // Now create the url with the route to talk with the rest API
            var reqURL = "http://localhost:5000/MessageApp/messages/"+mid+"/likes";
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
                    //alert("Tu like se ha registrado exitosamente.");
                    thisCtrl.loadLikes(mid);
                }, //Error function
                function (response) {
                    // This is the error function
                    // If we get here, some error occurred.
                    // Verify which was the cause and show an alert.
                    var status = response.status;
                    console.log("Error: " + reqURL);
                    //alert("Cristo");
                    if (status == 0) {
                        alert("No hay conexion a Internet");
                    }else if (status == 400) {
                        alert("Tienes algún error con tu información.");
                    }
                    else if (status == 401) {
                        alert("Su sesion expiro. Conectese de nuevo.");
                    }
                    else if (status == 403) {
                        alert("No esta autorizado a usar el sistema.");
                    }
                    else if (status == 404) {
                        alert("No se encontro la informacion solicitada.");
                    }
                    else {
                        alert("Error interno del sistema.");
                    }
                }
            );
        };

        thisCtrl.postDislike = function(mid){

            var loggedUser = localStorage.getItem("currentLoggedUser");

            // Build the data object
            var data = {};
            data.pid = loggedUser;

            console.log(data);

            data = JSON.stringify(data);

            console.log(data);

            //$log.error("Message Loaded: ", JSON.stringify(thisCtrl.loginform));

            // Now create the url with the route to talk with the rest API
            var reqURL = "http://localhost:5000/MessageApp/messages/"+mid+"/dislikes";
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
                    //alert("Tu like se ha registrado exitosamente.");
                    thisCtrl.loadDislikes(mid);
                }, //Error function
                function (response) {
                    // This is the error function
                    // If we get here, some error occurred.
                    // Verify which was the cause and show an alert.
                    var status = response.status;
                    console.log("Error: " + reqURL);
                    //alert("Cristo");
                    if (status == 0) {
                        alert("No hay conexion a Internet");
                    }else if (status == 400) {
                        alert("Tienes algún error con tu información.");
                    }
                    else if (status == 401) {
                        alert("Su sesion expiro. Conectese de nuevo.");
                    }
                    else if (status == 403) {
                        alert("No esta autorizado a usar el sistema.");
                    }
                    else if (status == 404) {
                        alert("No se encontro la informacion solicitada.");
                    }
                    else {
                        alert("Error interno del sistema.");
                    }
                }
            );
        };

        thisCtrl.postMessage = function(){

            var loggedUser = localStorage.getItem("currentLoggedUser");
            var content = document.getElementById("textarea1").value;

            // Build the data object
            var data = {};

            data.content = content;

            data.pid = parseInt(loggedUser);

            console.log(data);

            data = JSON.stringify(data);

            console.log(data);

            //$log.error("Message Loaded: ", JSON.stringify(thisCtrl.loginform));

            // Now create the url with the route to talk with the rest API
            var reqURL = "http://localhost:5000/MessageApp/groups/"+thisCtrl.gid+"/messages";
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
                    thisCtrl.messages();
                }, //Error function
                function (response) {
                    // This is the error function
                    // If we get here, some error occurred.
                    // Verify which was the cause and show an alert.
                    var status = response.status;
                    console.log("Error: " + reqURL);
                    //alert("Cristo");
                    if (status == 0) {
                        alert("No hay conexion a Internet");
                    }else if (status == 400) {
                        alert("Tienes algún error con tu información.");
                    }
                    else if (status == 401) {
                        alert("Su sesion expiro. Conectese de nuevo.");
                    }
                    else if (status == 403) {
                        alert("No esta autorizado a usar el sistema.");
                    }
                    else if (status == 404) {
                        alert("No se encontro la informacion solicitada.");
                    }
                    else {
                        alert("Error interno del sistema.");
                    }
                }
            );
        };

        this.searchHashtagsMessages = function(){

            var hashtag = document.getElementById("textarea2").value;

            var url = "http://localhost:5000/MessageApp/groups/"+thisCtrl.gid+"/messages";
            console.log("http://localhost:5000/MessageApp/groups/"+thisCtrl.gid+"/messages");

            $http.get(url, { params: {hashtag:hashtag}}).then(
                function (response){

                    console.log("response: " + JSON.stringify(response.data));
                    console.log(response.data);

                    thisCtrl.messageList = response.data.Messages;

            },
            function (response){

                var status = response.status;
                if (status == 0){
                    alert("No hay conexion a Internet");
                }
                else if (status == 401){
                    alert("Su sesion expiro. Conectese de nuevo.");
                }
                else if (status == 403){
                    alert("No esta autorizado a usar el sistema.");
                }
                else if (status == 404){
                    alert("No se encontro la informacion solicitada.");
                }
                else {
                    alert("Error interno del sistema.");
                }
            });


        };

        this.loadWriteMessageBox = function(){
            document.getElementById("writemessagebox").style.display = "block";
            document.getElementById("searchhashtagbox").style.display = "none";
        };

        this.loadSearchHashtagBox = function(){
            document.getElementById("writemessagebox").style.display = "none";
            document.getElementById("searchhashtagbox").style.display = "block";
        };

        this.showWriteReplyBox = function(mid){
            document.getElementById("enterreplymessagebox").style.display = "block";
            localStorage.setItem("currentSelectedMessage", mid);
        };

         this.hideWriteReplyBox = function(){
            document.getElementById("enterreplymessagebox").style.display = "none";
        };

        this.postReplyMessage = function(mid){

            var loggedUser = localStorage.getItem("currentLoggedUser");
            var content = document.getElementById("textarea3").value;

            // Build the data object
            var data = {};

            data.content = content;

            data.pid = parseInt(loggedUser);

            console.log(data);

            data = JSON.stringify(data);

            console.log(data);

            //$log.error("Message Loaded: ", JSON.stringify(thisCtrl.loginform));

            // Now create the url with the route to talk with the rest API
            var reqURL = "http://localhost:5000/MessageApp/groups/"+thisCtrl.gid+"/messages/"+localStorage.getItem("currentSelectedMessage");
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
                    thisCtrl.messages();
                }, //Error function
                function (response) {
                    // This is the error function
                    // If we get here, some error occurred.
                    // Verify which was the cause and show an alert.
                    var status = response.status;
                    console.log("Error: " + reqURL);
                    //alert("Cristo");
                    if (status == 0) {
                        alert("No hay conexion a Internet");
                    }else if (status == 400) {
                        alert("Tienes algún error con tu información.");
                    }
                    else if (status == 401) {
                        alert("Su sesion expiro. Conectese de nuevo.");
                    }
                    else if (status == 403) {
                        alert("No esta autorizado a usar el sistema.");
                    }
                    else if (status == 404) {
                        alert("No se encontro la informacion solicitada.");
                    }
                    else {
                        alert("Error interno del sistema.");
                    }
                }
            );


        }

        this.hideListWhoLikes = function(){
            document.getElementById("peopleWhoLike").style.display = "none";
        }

        this.hideListWhoDislikes = function(){
            document.getElementById("peopleWhoDislike").style.display = "none";
        }


        this.loadWhoLikes = function(mid){


            var url = "http://localhost:5000/MessageApp/messages/"+mid+"/likes";
            console.log("http://localhost:5000/MessageApp/messages/"+mid+"/likes");

            $http.get(url, {params: {"who":true}}).then(
                function (response){

                    console.log("response: " + JSON.stringify(response.data));
                    console.log(response.data);
                    thisCtrl.peopleWhoLike = response.data.Like_list;
                    document.getElementById("peopleWhoLike").style.display = "block";
                    document.getElementById("listwholike").innerHTML = "";


                    console.log(thisCtrl.peopleWhoLike);
                    for(var people in thisCtrl.peopleWhoLike){
                        var z = document.createElement('p'); // is a node
                        z.style = "margin-left:10px;"
                        z.innerHTML = thisCtrl.peopleWhoLike[people].username;
                        document.getElementById("listwholike").appendChild(z);
                    }

            },
            function (response){

                var status = response.status;
                alert(response.data.Error);

                if (status == 0){
                    alert("No hay conexion a Internet");
                }
                else if (status == 401){
                    alert("Su sesion expiro. Conectese de nuevo.");
                }
                else {
                    alert("Error interno del sistema.");
                }
            });

        };

        this.loadWhoDislikes = function(mid){



            var url = "http://localhost:5000/MessageApp/messages/"+mid+"/dislikes";
            console.log("http://localhost:5000/MessageApp/messages/"+mid+"/dislikes");

            $http.get(url, {params: {"who":true}}).then(
                function (response){

                    console.log("response: " + JSON.stringify(response.data));
                    console.log(response.data);

                    thisCtrl.peopleWhoLike = response.data.Dislike_list;

                    document.getElementById("peopleWhoDislike").style.display = "block";

                    console.log(thisCtrl.peopleWhoLike);

                    document.getElementById("listwhodislike").innerHTML = "";
                    for(var people in thisCtrl.peopleWhoLike){
                        var z = document.createElement('p'); // is a node
                        z.style = "margin-left:10px;"
                        z.innerHTML = thisCtrl.peopleWhoLike[people].username;
                        document.getElementById("listwhodislike").appendChild(z);
                    }

            },
            function (response){
                alert(response.data.Error);

                var status = response.status;
                if (status == 0){
                    alert("No hay conexion a Internet");
                }
                else if (status == 401){
                    alert("Su sesion expiro. Conectese de nuevo.");
                }
                else {
                    alert("Error interno del sistema.");
                }
            });

        };


        this.messages();

}]);
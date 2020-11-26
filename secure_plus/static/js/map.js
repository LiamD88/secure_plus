function initMap() { //initialises map
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 16,
        center: {lat: 53.271301, lng: -6.204100}
      });
      var office = {lat: 53.271301, lng: -6.204100};var marker = new google.maps.Marker({position: office, map: map});
    
    }

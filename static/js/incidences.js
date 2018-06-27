var map;

$(document).ready(function(){
map = L.map('map').setView([-0.261360, 35.050093], 10);
        mapLink ='<a href="http://openstreetmap.org">OpenStreetMap</a>';
        L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: 'Map data &copy; ' + mapLink,
          maxZoom:32,
          }).addTo(map);

        function onMapClick(e) {
            alert("hello")
          var lat = e.latlng.lat;
          var lng = e.latlng.lng;   
          if (typeof marker != 'undefined') {
              map.removeLayer(marker);  // delete previous marker
              marker = L.marker([lat, lng]).addTo(map);  // add new marker
          }
          else {
              marker = L.marker([lat, lng]).addTo(map);  // add new marker
          }
          $('#coordinates').val(lng + ',' + lat)         
        }
        map.on('click', onMapClick);
    });
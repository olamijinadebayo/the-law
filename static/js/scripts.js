var mymap;
var lyrOSM;
var lyrImagery;
var lyrTopo;
var lyrWaterColor;
var lyrOutdoors;
var lyrSearch;
var lyrLawyers;
var lyrAllLawyers;
var lyrMarkerCluster;
var popZocalo;

var ctlAttribute;
var ctlScale;
var ctlPan;

var ctlZoomslider;
var ctlMouseposition;
var ctlMeasure;

var ctlEasybutton;
var ctlSidebar;
var ctlSearch;

var ctlLayers;
var ctlStyle;
var ctlRouting;

var objBasemaps;
var ObjOverlays;
var ctlDraw;
var drawnItems;
var animatedMarker;
var markerCurrentLocation;
var closest;

var criminalIcn;
var cilvilIcn;
var globalGeolocationCoordinates;
var jsnBuffer;

var coords;
var lat;
var lng;
var pointlyrbuffer;


$(document).ready(function () {
    mymap = L.map('mapdiv', {
        center: [-0.245, 35.567],
        zoom: 16,
        zoomControl: false,
        attributionControl: false
    })
    ctlPan = L.control.pan().addTo(mymap);
    ctlZoomslider = L.control.zoomslider({
        position: 'topright'
    }).addTo(mymap);
    ctlSidebar = L.control.sidebar('side-bar').addTo(mymap);
    ctlEasybutton = L.easyButton('glyphicon-transfer', function () {
        ctlSidebar.toggle();
    }).addTo(mymap);
    ctlSearch = L.Control.openCageSearch({
        limit: 10
    }).addTo(mymap);
    ctlAttribute = L.control.attribution({
        position: 'bottomleft'
    }).addTo(mymap);
    ctlAttribute.addAttribution('OSM');
    ctlAttribute.addAttribution('&copy; <a href="http://reactgis"</a>');
    // **********layer initialization *************

    lyrOSM = L.tileLayer.provider('OpenStreetMap.Mapnik');
    lyrImagery = L.tileLayer.provider('Esri.WorldImagery');
    lyrTopo = L.tileLayer.provider('OpenTopoMap');
    lyrWaterColor = L.tileLayer.provider('Stamen.Watercolor');
    lyrOutdoors = L.tileLayer.provider('Thunderforest.Outdoors');
    mymap.addLayer(lyrOSM);



    // icons
    criminalIcn =  "static/images/theater.png",
    cilvilIcn = "/static/images/museum.png"
    //    **********************overlay layer control ************

    objBasemaps = {
        "Open Street Maps": lyrOSM,
        "Topo Map": lyrTopo,
        "Imagery": lyrImagery,
        "Outdoors": lyrOutdoors,
        "Watercolor": lyrWaterColor
    };

    drawnItems = new L.FeatureGroup();
    drawnItems.addTo(mymap);
    //   overlaysvar

// all layers
    lyrAllLawyers = L.geoJSON.ajax('http://127.0.0.1:8000/lawyer/google',
    {
        pointToLayer: function(feature, latlng){
        var att = feature.properties;
        return L.marker(latlng, {
            icon: L.icon({
                iconUrl: att.icon,
                iconSize: [24, 28],
                iconAnchor: [12, 28],
                popupAnchor: [0, -25]
              }),
           riseOnHover: true
        })
    },
    onEachFeature: function(feature, layer){
        var attr = feature.properties;
            if (attr) {
              var content = 
              "<table class='table table-striped table-bordered table-condensed'>" + 
              "<tr><th>first name</th><td>" + attr.name + 
              "<tr><th>last name</th><td>" + attr.description + 
              "</td></tr>" + "<tr><th>Phone</th><td>" + attr.phone + 
              "</td></tr>" + "<tr><th>category</th><td>" + attr.category +" lawyer" +
              "<table>";
              layer.on({
                click: function (e) {
                  layer.bindPopup(content)
                }
              });
            }

    }
}
).addTo(mymap)
    lyrMarkerCluster = L.markerClusterGroup();
    lyrLawyers = L.geoJSON.ajax('http://127.0.0.1:8000/lawyer/data', {
        pointToLayer: function (feature, latlng) {
            var attr = feature.properties;
            if(attr.category == 'criminal'){
                icon = criminalIcn;
            }else{
                icon = cilvilIcn;
            }

            return L.marker(latlng, {
              icon: L.icon({
                iconUrl: icon,
                iconSize: [24, 28],
                iconAnchor: [12, 28],
                popupAnchor: [0, -25]
              }),
              riseOnHover: true
            });
          }, 
          filter:filterByCategory,
          onEachFeature: function (feature, layer) {
            var attr = feature.properties;
            if (attr) {
              var content = 
              "<table class='table table-striped table-bordered table-condensed'>" + 
              "<tr><th>first name</th><td>" + attr.first_name + 
              "<tr><th>last name</th><td>" + attr.last_name + 
              "</td></tr>" + "<tr><th>Phone</th><td>" + attr.phone + 
              "</td></tr>" + "<tr><th>category</th><td>" + attr.category +" lawyer" +
              "<table>";
              layer.on({
                click: function (e) {
                  layer.bindPopup(content)
                }
              });
            }
          }
    }).addTo(mymap);
    

    // console.log(heat)
    ObjOverlays = {
        "incidences": lyrLawyers,
        "clusters": lyrMarkerCluster,
        'google':lyrAllLawyers
    }
    
    lyrLawyers.on('data:loaded', function(){
        mymap.fitBounds(lyrLawyers.getBounds());

    });


    ctlDraw = new L.Control.Draw({
        draw : {
            polyline: false,
            polygon: false,
            rectangle: false,
            circle:false
        },
        edit:{
            featureGroup: drawnItems,
            remove: true
        }

    });
    ctlDraw.addTo(mymap);


    

    // all
    ctlLayers = L.control.layers(objBasemaps, ObjOverlays).addTo(mymap);
    lyrLawyers.on('data:loaded', function () {
        mymap.fitBounds(lyrLawyers.getBounds());
        lyrMarkerCluster.addLayer(lyrLawyers);
        lyrMarkerCluster.addTo(mymap);
     

    });
//    ctlRouting = L.Routing.control({waypoints:[L.latLng(-0.3978268, 36.9612328),L.latLng(-0.378268, 36.7612328)], router: L.Routing.mapbox('pk.eyJ1IjoiZGVyeSIsImEiOiJjaWY5anJyN3YwMDI5dGNseHoyZzM4Z3R4In0.dToOXYIZ30LH_7VtFbKW4A')}).addTo(mymap);


    lyrLawyers.on('data:loaded', function(){
        mymap.fitBounds(lyrLawyers.getBounds());
        

        $("#geolocate").click(function(){
            mymap.locate();
            mymap.on('locationfound', function (e) {
                coords = e.latlng
                
            });
            if(coords){
            lat = $("#latitude").attr('value',coords['lat'])
            lng = $("#longitude").attr('value',coords['lng'])
            }else{
                lat = $("#latitude").attr('value',-1.1912899)
                lng = $("#longitude").attr('value',36.911893299999996)
            }
           })

        $('#bufferbtn').click(function(){
           
           var bufferval = parseInt($("#bufferradius").val());
           lat = parseInt($("#latitude").val())
           lng = parseInt($("#longitude").val())
        //    var point = turf.point([lng, lat]);
        var point = {
            "type": "Feature",
            "properties": {},
            "geometry": {
              "type": "Point",
              "coordinates": [lng, lat]
            }
          };
           jsnBuffer = turf.buffer(point, bufferval, 'kilometers');
  
           pointlyrbuffer = L.geoJSON(jsnBuffer,{style:{color:'black', dashArray:'5,5', fillOpacity:0.3}}).addTo(mymap);
           lyrLawyers.bringToFront()
           mymap.fitBounds(pointlyrbuffer.getBounds())
           

        })
    });
   








mymap.on('click', function(e){
    if(closest){
        closest.remove();
    }
    var llRef = e.latlng;
    var strTable = "<table class='table table-hover'>";
    strTable += "<tr><th>First name</th><th>second name</th><th>phone</th><th>Distance</th><th>Direction</th></tr>";
    
    var nrLawyer= returnClosestlayer(lyrLawyers, llRef);
    
    strTable += "<tr><td>"+nrLawyer.att.first_name+"</td><td>"+nrLawyer.att.last_name+"</td><td>"+nrLawyer.att.phone+"</td><td>"+nrLawyer.distance.toFixed(0)+" m</td><td>"+nrLawyer.bearing.toFixed(0)+"</td></tr>";
    
    var geolocatemarker = L.marker(e.latlng,{draggable:true}).addTo(mymap).bindPopup(strTable,{maxWidth:600});
    geolocatemarker.on('dragend',e);
    // ctlRouting = L.Routing.control({waypoints:[L.latLng(-0.3978268, 36.9612328),L.latLng(-0.378268, 36.7612328)], router: L.Routing.mapbox('pk.eyJ1IjoiZGVyeSIsImEiOiJjaWY5anJyN3YwMDI5dGNseHoyZzM4Z3R4In0.dToOXYIZ30LH_7VtFbKW4A')}).addTo(mymap);
    closest = L.marker(nrLawyer.latlng).addTo(mymap);
    });

// will come back to geolocation 

    $('#btnLocate').click((event) => {
        mymap.locate();
    });

    mymap.on('locationfound', function (e) {

        if (markerCurrentLocation) {
            markerCurrentLocation.remove();
        }
        var llRef = e.latlng;
        globalGeolocationCoordinates = e.latlng;
        var strTable = "<table class='table table-hover'>";
        strTable += "<tr><th>First name</th><th>second name</th><th>phone</th><th>Distance</th><th>Direction</th></tr>";
        
        var nrLawyer= returnClosestlayer(lyrLawyers, llRef);
        
        strTable += "<tr><td>"+nrLawyer.att.first_name+"</td><td>"+nrLawyer.att.last_name+"</td><td>"+nrLawyer.att.phone+"</td><td>"+nrLawyer.distance.toFixed(0)+" m</td><td>"+nrLawyer.bearing.toFixed(0)+"</td></tr>";
        
        var geolocatemarker = L.marker(e.latlng).addTo(mymap).bindPopup(strTable,{maxWidth:600});
        var closest = L.marker(nrLawyer.latlng).addTo(mymap);
    
    });
    mymap.on('locationerror', function (e) {
        alert('location was not found');
    });

    // filter categories
    function filterByCategory(json){
        var att = json.properties;
        var optFilter = $("input[name=fltCategory]:checked").val();
        if(optFilter == "ALL"){
            return true
        }else{
            return (att.category == optFilter)
        }
    }
    $("input[name=fltCategory]").click(function(){
        // arEventIDs=[];
        lyrLawyers.refresh();
    });

    



});


function returnClosestlayer(lyrGroup, llRef) {
    var arLyrs = lyrGroup.getLayers();
    var nearest = L.GeometryUtil.closestLayer(mymap, arLyrs, llRef);
    nearest.distance = llRef.distanceTo(nearest.latlng);
    nearest.bearing = L.GeometryUtil.bearing(llRef, nearest.latlng);
    if (nearest.bearing<0){
        nearest.bearing = nearest.bearing+360;
    }
    nearest.att = nearest.layer.feature.properties;
    return nearest;
}
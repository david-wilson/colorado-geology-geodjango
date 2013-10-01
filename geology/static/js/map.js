(function() {
    var loc = $("#location");
    var rocks = $("#rocks");

    var getLocation = function() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(handlePosition);
            } else {
                loc.html("GeoLocation not supported");
            } 
        }
    var handlePosition = function(position) {
        var lat = position.coords.latitude;
        var lon = position.coords.longitude;
        $.get(url, {"lat": lat,
                    "lon": lon },
                    function(data) {
                        rocks.empty();
                        $.each(data.features, function(index, val) {
                            var name = val.properties.name;
                            var description = val.properties.description;
                            rocks.append(name);
                            rocks.append(description);
                            makeMap(val, lon, lat);
                        });
                    }); 
        }

    var featurePopup = function(feature, layer) {
            var popupContent = feature.properties.name;

            if (feature.properties && feature.properties.popupContent) {
                popupContent += feature.properties.popupContent;
            }

            layer.bindPopup(popupContent);
        }



    var makeMap = function(feature, lon, lat) {
        var map = L.map('map').setView([lat, lon], 13);
        
        //Unit
        var unit = L.geoJson(feature, {
            onEachFeature: featurePopup
        }).addTo(map);

        //OSM layer
        L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);

        // Marker
        L.marker([lat, lon]).addTo(map)
            .bindPopup(feature.properties.name)
            .openPopup();
    }

    getLocation();
})();
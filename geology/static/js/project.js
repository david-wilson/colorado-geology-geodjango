window.onload = function() {
    var loc = $('#location');

    var getLocation = function() {
        if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(getUnits);
            } else {
                loc.html("Geolocation not supported");
            }
    }

    var getUnits = function(position)
    var makeMap = function(units, lon, lat) {
        var map = L.map('map').setView([lat,lon], 13);

        L.tileLayer('http:/{s}.tile.osm.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);

        $.each(units, function(index, unit) {
            var thisUnit = L.geoJson(unit).addTo(map);
        }

        L.marker([lat, lon]).addTo(map);
    }
};

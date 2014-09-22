navigator.geolocation.getCurrentPosition(GetLocation);
function GetLocation(location) {
    alert(location.coords.latitude);
    alert(location.coords.longitude);
    alert(location.coords.accuracy);
}
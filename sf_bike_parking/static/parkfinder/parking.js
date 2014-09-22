window.onload = function() {
	var button = document.getElementById("location-trigger");
	button.onclick = function() {
    	getLocation();
    	return false;
    }
}


function getLocation() {
	document.getElementById("location-trigger").value="Please wait..."
	navigator.geolocation.getCurrentPosition(GetLocation);
}

function GetLocation(location) {
	document.getElementById("latitude").value = location.coords.latitude;
	document.getElementById("longitude").value = location.coords.longitude;
	document.getElementById("location-trigger").value="Fill my location!"
    // alert(location.coords.accuracy);
}

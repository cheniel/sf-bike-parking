window.onload = function() {

	if (!"geolocation" in navigator) {
	  document.getElementById("location-trigger").style.display = 'none';
	}

	var button = document.getElementById("location-trigger");
	button.onclick = function() {
    	getLocation();
    	return false;
    }
}

function getLocation() {
	document.getElementById("location-trigger").value="please wait...";
	document.getElementById("latitude").value = "finding...";
	document.getElementById("longitude").value = "finding...";
	navigator.geolocation.getCurrentPosition(fillLocation, showError);
}

function fillLocation(location) {
	document.getElementById("latitude").value = location.coords.latitude;
	document.getElementById("longitude").value = location.coords.longitude;
	document.getElementById("location-trigger").value="refresh location";
    // alert(location.coords.accuracy);
}

function showError(error) {
    switch(error.code) {
        case error.PERMISSION_DENIED:
            alert("Need to allow location services. Refresh and try again.");
            resetForm();
            break;
        case error.POSITION_UNAVAILABLE:
            alert("Location information is unavailable.");
            resetForm();
            break;
        case error.TIMEOUT:
            alert("The request to get user location timed out.");
            resetForm();
            break;
        case error.UNKNOWN_ERROR:
            alert("An unknown error occurred.");
            resetForm();
            break;
    }
}

function resetForm() {
	document.getElementById("location-trigger").value="fill my location";
	document.getElementById("latitude").value = "";
	document.getElementById("longitude").value = "";
}

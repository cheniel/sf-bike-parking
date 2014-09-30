window.onload = function() {

	if (!"geolocation" in navigator) {
	  document.getElementById("location-trigger").style.display = 'none';
	}

    retrieveLocationButton = document.getElementById("location-trigger");
    if (retrieveLocationButton) {
        retrieveLocationButton.onclick = function() {
            getLocation();
            return false;
        }
    }

    if (document.getElementById("location-search-options")) {
        if (document.getElementById("latitude").getAttribute("value") == "None") {
            document.getElementById("latitude").value = "";
        }

        if (document.getElementById("longitude").getAttribute("value") == "None") {
            document.getElementById("longitude").value = "";
        }  
    }

    if (document.getElementById("street-search-options")) {
        if (document.getElementById("street").getAttribute("value") == "None") {
            document.getElementById("street").value = "";
        }
    }

    locationSearchButton = document.getElementById("location-search-button");
    if (locationSearchButton) {
        locationSearchButton.onclick = function() {
            document.getElementById("location-search-options").style.display = 'block';
            document.getElementById("search-type-selection").style.display = 'none';
            document.getElementById("latitude").focus();
        }
    }

    streetSearchButton = document.getElementById("street-search-button");
    if (streetSearchButton) {
        streetSearchButton.onclick = function() {
            document.getElementById("street-search-options").style.display = 'block';
            document.getElementById("search-type-selection").style.display = 'none';
            document.getElementById("street").focus();
        }
    }

}

function getLocation() {
	document.getElementById("location-trigger").value="please wait...";
	document.getElementById("latitude").value = "finding...";
	document.getElementById("longitude").value = "finding...";
	navigator.geolocation.getCurrentPosition(fillLocation, locErrorHandler);
}

function fillLocation(location) {
	document.getElementById("latitude").value = location.coords.latitude;
	document.getElementById("longitude").value = location.coords.longitude;
	document.getElementById("location-trigger").value="refresh location";
}

function locErrorHandler(error) {
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

function showSearchTypes() {
    document.getElementById("location-search-options").style.display = 'none';
    document.getElementById("street-search-options").style.display = 'none';
    document.getElementById("search-type-selection").style.display = 'block';
}

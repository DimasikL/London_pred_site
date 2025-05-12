function getBathroomsValue() {
    var uiBathrooms = document.getElementsByName("uiBathrooms");
    for(var i in uiBathrooms) {
      if(uiBathrooms[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; // Invalid Value
  }
  
function getBedroomsValue() {
    var uiBedrooms = document.getElementsByName("uiBedrooms");
    for(var i in uiBedrooms) {
      if(uiBedrooms[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; // Invalid Value
  }
  
function getReceptionsValue() {
    var uiReceptions = document.getElementsByName("uiReceptions");
    for(var i in uiReceptions) {
      if(uiReceptions[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; // Invalid Value
  }

function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var sqft = document.getElementById("uiSqft");
    var bedroom = getBedroomsValue();
    var bathroom = getBathroomsValue();
    var reception = getReceptionsValue();
    var location = document.getElementById("uiLocations");
    var estPrice = document.getElementById("uiEstimatedPrice");
  
    var url = "http://127.0.0.1:5000/predict_home_price";
  
    $.post(url, {
        sqft: parseFloat(sqft.value),
        bedroom: bedroom,
        bathroom: bathroom,
        reception: reception,
        location: location.value
    },function(data, status) {
        console.log(data.estimated_price);
        estPrice.innerHTML = "<h2>GBP " + data.estimated_price;
        console.log(status);
    });
  }
  
function onPageLoad() {
    console.log( "document loaded" );
    var url = "http://127.0.0.1:5000/get_location_names"; 
    $.get(url,function(data) {
        console.log("got response for get_location_names request");
        if(data) {
            var locations = data.locations;
            var uiLocations = document.getElementById("uiLocations");
            $('#uiLocations').empty();
            for(var i in locations) {
                var opt = new Option(locations[i]);
                $('#uiLocations').append(opt);
            }
        }
    });
  }
  
window.onload = onPageLoad;
function getBathValue(){
    var uiBathrooms =document.getElementsByName("uiBathrooms");
    for(var i in uiBathrooms){
        if (uiBathrooms[i].checked){
            return parseInt(i)+1;
        }
    }
    return -1
}
function getBHKValue(){
    var uiBHK = document.getElementsByName("uiBHK");
    for(var i in uiBHK){
        if (uiBHK[i].checked){
            return parseInt(i)+1;
        }
    }
    return -1
}

function onClickEstimatePrice(){
    var location = document.getElementById("uiLocations");
    var size = document.getElementById("uiSqft");
    var bhk= getBHKValue();
    var baths = getBathValue();
    var estprice = document.getElementById("uiEstimatedPrice");

    var url = "http://127.0.0.1:5000/predict_price";
    $.post(url ,{
        location : location.value,
        size:parseFloat(size.value),
        bhk :bhk,
        baths:baths
        
    },function (data,status){
        console.log(data.price);
        estprice.innerHTML = "<h2>"+data.price +"</h2>";
        console.log(status);
    });
}
// getting locations on page load
function onPageLoad(){
    console.log(".....loading complete");
    var url = "http://127.0.0.1:5000/get_locations";
    $.get(url,function(data, status){
        console.log("request accepted..");
        if(data){
            var locations = data.locations;
            var uiLocations = document.getElementById("uiLocations");
            $('#uiLocations').empty();
            for (var i in locations){
                var opt =new Option(locations[i]);
                $('#uiLocations').append(opt);
            }
        }
    });
}
window.onload =onPageLoad;
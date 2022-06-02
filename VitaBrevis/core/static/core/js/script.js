function iniciarMap(){
    var coord = {lat:-33.383858 ,lng:-70.668157};
    var map = new google.maps.Map(document.getElementById('map'),{
        zoom: 17,
        center: coord
    });
    var marker = new google.maps.Marker({
        position: coord,
        map: map
    });
}
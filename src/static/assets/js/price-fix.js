function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  }
  
  var hotelPrices = document.getElementsByClassName("js__price");
  
  for (var i = 0; i < hotelPrices.length; i++) {
    hotelPrices[i].textContent = numberWithCommas(hotelPrices[i].textContent);
  }
  
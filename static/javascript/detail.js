var dropdownItems = document.querySelectorAll('.dropdown-item');
var dropdownButton = document.querySelector('.dropdown-toggle');

dropdownItems.forEach(function(item) {
  item.addEventListener('click', function() {
    var selectedProduct = this.innerHTML;
    var input = document.getElementById('numInput');
    dropdownButton.innerHTML = selectedProduct;
    input.value = input.value || 1;
    updateTotal();
  });
});

function decrease() {
  var input = document.getElementById('numInput');
  if (input.value > 1) {
    input.value--;
    updateTotal();
  }
}

function increase() {
  var input = document.getElementById('numInput');
  input.value++;
  updateTotal();
}

function checkValue() {
  var input = document.getElementById('numInput');
  if (input.value < 1) {
    input.value = 1;
  }
}

function updateTotal() {
  var input = document.getElementById('numInput');
  var selectedProduct = document.querySelector('.dropdown-toggle').textContent.trim();
  var price = 49900;
  var total = price * parseFloat(input.value);
  if (isNaN(total)) {
    total = 0;
  }
  document.getElementById('totalAmount').innerHTML = "옵션 : " + selectedProduct + " " + "수량 : " + input.value + " / 총 상품금액: " + total.toLocaleString('ko-KR') + "원";
}

const thumbnails = document.querySelectorAll('.thumbnail');
const largeImage = document.querySelector('.col-6 img');

thumbnails.forEach(thumbnail => {
  thumbnail.addEventListener('mouseover', () => {
    largeImage.src = '/static/img/clothes/' + thumbnail.dataset.largeImage
  });
});

largeImage.addEventListener('mouseout', () => {
  largeImage.src = "/static/img/clothes/2028326_2_500.jpg";
});
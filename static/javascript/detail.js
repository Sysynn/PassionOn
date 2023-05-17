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
  // var selectedProduct = document.querySelector('.dropdown-toggle').textContent.trim();
  var productSize = document.getElementById('clothSize').textContent
  var quantityInput = document.getElementById('quantityInput')
  var purchaseQuantityInput = document.getElementById('purchaseQuantityInput')
  var price = document.getElementById('clothesPrice').textContent;
  var total = price * parseFloat(input.value);
  if (isNaN(total)) {
    total = 0;
  }
  quantityInput.value = input.value
  purchaseQuantityInput.value = input.value
  document.getElementById('totalAmount').innerHTML = "사이즈 : " + productSize + " " + "수량 : " + input.value + " / 총 상품금액: " + total.toLocaleString('ko-KR') + "원";
}

const thumbnails = document.querySelectorAll('.thumbnail');
const largeImage = document.querySelector('.col-6 img');

thumbnails.forEach(thumbnail => {
  thumbnail.addEventListener('mouseover', () => {
    // largeImage.src = '/static/img/clothes/' + thumbnail.dataset.largeImage
    largeImage.src = thumbnail.dataset.largeImage
    console.log(largeImage.src)
  });
  let imgChangeTimer
  thumbnail.addEventListener('mouseout', () => {
    // 마우스 아웃시 화면전환이 너무 어지럽다 판단되어 delay 추가
    clearTimeout(imgChangeTimer)
    imgChangeTimer = setTimeout(() => {
      largeImage.src = thumbnail.dataset.thumbnailImage;
    }, 700)
    console.log(largeImage.src)
  });
});

// largeImage.addEventListener('mouseout', () => {
//   largeImage.src = '/static/img/clothes/detail_2028326_17_500-s.jpg';
//   console.log(largeImage.src)
// });


// Like axios
const form = document.querySelector('#likes-form');
    const heartIcon = document.querySelector('#cloth-heart');

    form.addEventListener('submit', function (event) {
      event.preventDefault();
      const clothId = event.target.dataset.clothId;
      const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

      axios({
        method: 'post',
        url: `/clothes/${clothId}/likes/`,
        headers: { 'X-CSRFToken': csrftoken },
      })
        .then((response) => {
          const isLiked = response.data.is_liked;
          const likesCount = response.data.likes_count;
          if (isLiked) {
            heartIcon.classList.remove('bi-suit-heart');
            heartIcon.classList.add('bi-suit-heart-fill');
          } else {
            heartIcon.classList.remove('bi-suit-heart-fill');
            heartIcon.classList.add('bi-suit-heart');
          }
          // 좋아요 수 js
          // const likesCountElement = document.querySelector('#likes-count');
          // likesCountElement.textContent = likesCount;
        })
        .catch((error) => {
          console.error(error);
        });
    });
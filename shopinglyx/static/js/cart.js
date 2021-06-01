var updateBtns = document.getElementsByClassName('update-cart');

for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function(){
      var action = this.dataset.action;
      var productId = this.dataset.product;
      console.log(action, productId);
      console.log( 'user : ', user)
      if (user==='AnonymousUser'){
          console.log('not logged In')
      }else{
          updateUserOrder(productId, action)
      }
    });
  }


  function updateUserOrder(productId, action){
    console.log('user is logged in and try to send some data')
    const url = '/update_item/'
    fetch(url, {
      method: 'POST',
      headers:{
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken,
      },
      body:JSON.stringify({'productId':productId, 'action':action})
    })
    .then(response => response.json())
    .then(data => console.log(data));
  }
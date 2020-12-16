function review(){
    let foodReviewer   = $('.food-reviewer').val()
    let foodName       = $('.food-name').val()
    let foodStar       = $('.food-star').val()
    let foodMenu       = $('.food-menu').val()
    let foodPrice      = $('.food-price').val()
    let foodReview     = $('.food-review').val();

    $.ajax({
      type: "POST",
      url: "/review",
      data: {
        'reviewer': foodReviewer,
        'name': foodName,
        'Star': foodStar,
        'Menu': foodMenu,
        'Price': foodPrice,
        'Review': foodReview,
      },
    success: function (response) {
      if (response['result'] == 'success') {
        window.location.reload()
    }
  }
})

  }
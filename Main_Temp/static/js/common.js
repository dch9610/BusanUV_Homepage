function review() {
  let foodReviewer = $('.reviewer').val()
  let foodName = $('.name').val()
  let foodStar = $('.star').val()
  let foodMenu = $('.menu').val()
  let foodPrice = $('.price').val()
  let foodReview = $('.review').val()

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

function promote() {
  let promoter = $('.promoter').val()
  let promname = $('.prom_name').val()
  let promote  = $('.promote').val()

  $.ajax({
    type: "POST",
    url: "/promote",
    data: {
      'promoter': promoter,
      'promote': prom_name,
      'promote': promote
    },
    success: function (response) {
      if (response['result'] == 'success') {
        window.location.reload()
      }
    }
  })
}
document.addEventListener("DOMContentLoaded", function () {

  const confirmButtons = document.getElementsByClassName('confirm-button');
  const cancelButtons = document.getElementsByClassName('cancel-button');
  const deleteButtons = document.getElementsByClassName('delete-button');

  /**
   * Functionality to confirm a booking by clicking confirm button
   */
  for (var a = 0; a < confirmButtons.length; a++) {

    confirmButtons[a].addEventListener("click", (event) => {
      // Prevent default behavior of the click event
      event.preventDefault();
      // Access the event target
      const target = event.target;
      // Get booking id from dataset of button clicked
      let bookingId = target.dataset.booking_id;
      // Insert inner text to cancelled booking button
      target.innerText = "Confirmed!";
      // Read current URL
      let currentUrl = window.location.href;
      // Remove unused part of URL
      let newUrl = currentUrl.replace('/all-bookings/', '');
      // Redirect to confirm booking URL with booking number as argument
      window.location.href = `${newUrl}/confirm_booking/${bookingId}`;
    });
  }


/**
 * Functionality to cancel a booking by clicking cancel button
 */
for (var b = 0; b < cancelButtons.length; b++) {

  cancelButtons[b].addEventListener("click", (event) => {
  event.preventDefault();
  const target = event.target;
  let bookingId = target.dataset.booking_id;
  target.innerText = "Cancelled!";
  let currentUrl = window.location.href;
  var newUrl = '';
  if (currentUrl.includes('your-bookings')) {
    newUrl = currentUrl.replace('/your-bookings/', '');
  } else {
    newUrl = currentUrl.replace('/all-bookings/', '');
  }
  window.location.href = `${newUrl}/cancel_booking/${bookingId}`;
});
}


/**
 * Functionality to delete a booking by clicking delete button
 */
for (var c = 0; c < deleteButtons.length; c++) {

  deleteButtons[c].addEventListener("click", (event) => {
  event.preventDefault();
  const target = event.target;
  let bookingId = target.dataset.booking_id;
  target.innerText = "Deleted!";
  let currentUrl = window.location.href;
  var newUrl = '';
  if (currentUrl.includes('your-bookings')) {
    newUrl = currentUrl.replace('/your-bookings/', '');
  } else {
    newUrl = currentUrl.replace('/all-bookings/', '');
  }
  window.location.href = `${newUrl}/delete_booking/${bookingId}`;
});
}

});
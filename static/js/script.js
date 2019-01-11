// var submitReview = document.getElementById("submitReviewBtn");
// submitReview.addEventListener("click", function() {
// 	var content = document.getElementById("review-content");
// 	console.log(content)
// 	var ourRequest = new XMLHttpRequest();
// 	ourRequest.open('GET', '/addreview?content=' + content);
// 	ourRequest.onload = function() {
// 		if (ourRequest.status >= 200 && ourRequest.status < 400) {
// 			console.log("Everything went fine!");
// 		} else {
// 			console.log("We connected to the server, but ut returned an error!");
// 		}
// };

// function sendReview() {
// 	var content = document.forms["reviewForm"]["name"].value;
// 	console.log(content);
// }
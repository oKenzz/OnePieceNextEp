
//Fetch data from python flask api through json


// Define the function to update the HTML content

var now = 1
console.log("Hello World")

function updateContent() {
  now += 1
  document.getElementById("content").innerHTML = now;
}

// Call the function every 1 second
setInterval(updateContent, 1000);

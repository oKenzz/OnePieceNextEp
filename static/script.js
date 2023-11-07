
//Fetch data from python flask api through json


let epNumber;
let timeUntilAiring;

const url = "http://0.0.0.0:5000/data"
// Define the function to update the HTML content


fetch(url)
  .then(response => response.json())
  .then(data => {
    epNumber = data.epNum;
    timeUntilAiring = data.timeUntilAiring;
  })
  .catch(error => {
    console.error(error);
});
  
function updateContent() {
  timeUntilAiring--
  let min, sec;
  [min, sec] = [Math.floor(timeUntilAiring / 60), timeUntilAiring % 60];
  let hours;
  [hours, min] = [Math.floor(min / 60), min % 60];
  let days;
  [days, hours] = [Math.floor(hours / 24), hours % 24];

  const content = `${days}d ${hours}h ${min}m ${sec}s`;
  document.getElementById('TimeUntilAiring').innerHTML = content;

}


// Call the function every 1 second
setInterval(updateContent, 1000);

// let regx = new RegExp('^[a-z]+$',i); // Create a regular expression to match lowercase letters
// let pattern = /[a-z]/g;

// const reg = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|.(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/

// var t= reg.test("#123_est@gmil.com")
// console.log(t); 

// const regphone = /^(\+201|01|00201)[0-2,5]{1}[0-9]{8}/;

// let phone = "1234567890";
// console.log(regphone.test(phone)); // true


// try {
//     if (password.length < 6) { // Check if the password length is less than 6
//         console.log("Password invalid") // Throw an error if the condition is met
//     }
//     console.log("Password is valid"); // Output a message if the password is valid
// } catch (error) {
//     console.log("An error occurred:", error); // Output the error message to the console
// } 
// finally {
//     console.log("This will always execute"); // Output a message that will always execute
// }

// alert(window.screenTop)
// alert(window.screenLeft)
// alert(window.screenLeft)
// alert(window.screen.availHeight)
// alert(window.screen.availWidth)
// alert() // Display the number of entries in the session history
// let res = confirm("Are you sure you want to proceed?")
// let win
// function goGoogle() {
//     win = window.open("", "_blank",'width=500,height=500,screenX=333,screenY=111'); // Open Google in a new tab
// }
// function closeWindow() {
//     if (win) {
//         win.close(); // Close the new window if it exists
//     } else {
//         console.log("No window to close"); // Output a message if no window is open
//     }
// }

// function focusWin(){
//     if (win) {
//         win.focus(); // Focus on the new window if it exists
//     } else {
//         console.log("No window to focus on"); // Output a message if no window is open
//     }
// }
// setInterval(() => {
//     console.log(count); // Output the current count to the console
//     count--; // Decrement the count by 1
// }, 1000); // Call the function every 1000 milliseconds (1 second)
// let count = 10

// let myEl = document.getElementById("output"); //

// myEl.innerHTML = count; // Set the inner HTML of the element to the current count

// let intervalId = setInterval(() => {
//     if (count > 0) {
//         count--; // Decrement the count by 1
//         myEl.innerHTML = count; // Update the inner HTML of the element with the new count
//     }
//     else {
//         clearInterval(intervalId); // Stop the interval when count reaches 0
//         myEl.innerHTML = "Time's up!"; // Update the inner HTML to indicate time is up
//     } 
// }, 1000); // Call the function every 1000 milliseconds (1 second)

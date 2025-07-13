// let myEl = document.getElementById("myDiv");
// let myEl = document.getElementsByTagName("input");
// myEl.value = "Type something here...";
// console.log(myEl);
// myEl.onfocus = () => {
//     myEl.value = "";
// };
// myEl.onblur = () => {
//     myEl.value = "Type something here...";
// };
// myEl.innerHTML = "<b>Type something here...</b>";

// console.log(myEl);
// myEl.style.backgroundColor = "yellow";

// myEl.onfocus = () => {
//     myEl.style.backgroundColor = "lightblue";
// };
// function changeColor(myEl) {
//     myEl.style.backgroundColor = "yellow";
// }
// console.log(myEl);
// myEl.addEventListener("focus", function() {
//     myEl.style.backgroundColor = "lightblue";
// });

// let myDiv = document.getElementById("myDiv");
// let myParagraph = document.createElement("p");
// myParagraph.textContent = "Hello, this is a new paragraph! From JavaScript.";
// document.body.appendChild(myParagraph);  
// const myImages = [
//     "p1.avif",
//     "p2.avif",
//     "p3.avif",
//     "p4.avif",
//     "p5.avif"
// ];
// let counter = 0;
// function changeImage() {
    
//     // Get a random index from the myImages array
//     // const randomIndex = Math.floor(Math.random() * myImages.length);
//     // Select the image element
//     // console.log(randomIndex);
//     let myImage = document.querySelector("img");
//     myImage.src = myImages[counter] // Change to the new image source

//     counter++;
//     if (counter >= myImages.length) {
//         counter = 0; // Reset the counter if it exceeds the array length
//     }
// }

// function test(event) {
//     event.preventDefault()
//     console.log(event)
//     if(document.getElementById("myInput").value.length > 3 ){
//         event.target.submit()
//     }

// }

// elements
let myForm = document.querySelector("form");
let nameInput = document.getElementById("name");
let emailInput = document.getElementById("email");
let pwdInput = document.getElementById("password");
let showPwd = document.getElementById("showPwd");
// messages
let nameMessage = document.getElementById("nameMsg");
let emailMessage = document.getElementById("emailMsg");
let pwdMessage = document.getElementById("pwdMsg");
let errorsList = {};
let errorCount = 0;
// event listeners
showPwd.addEventListener("click", function() {
    if (pwdInput.type === "password") {
        pwdInput.type = "text"; // Show the password
        showPwd.value = "Hide Password"; // Change button text
    } else {
        pwdInput.type = "password"; // Hide the password
        showPwd.value = "Show Password"; // Change button text
    }
});


nameInput.addEventListener("input", function() {
    if (nameInput.value.length < 3) {
        nameMessage.textContent = "* Name must be at least 3 characters long.";
        nameMessage.style.color = "red";
        nameMessage.style.display = "block";
        errorsList['name'] = 1;
    } else {
        nameMessage.textContent = "Valid name.";
        nameMessage.style.color = "green";
        nameMessage.style.display = "block";
        delete errorsList['name'] // Remove the first error if it exists
    }
})

emailInput.addEventListener("input", function() {
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(emailInput.value)) {
        emailMessage.textContent = "* Please enter a valid email address.";
        emailMessage.style.color = "red";
        emailMessage.style.display = "block";
        errorsList['email'] = 1;
    } else {
        emailMessage.textContent = "Valid email.";
        emailMessage.style.color = "green";
        emailMessage.style.display = "block";
       delete errorsList['email'] // Remove the second error if it exists
    }
})

pwdInput.addEventListener("input", function() {
    if (pwdInput.value.length < 6) {
        pwdMessage.textContent = "* Password must be at least 6 characters long.";
        pwdMessage.style.color = "red";
        pwdMessage.style.display = "block";    
         errorsList['pwd'] = 1;
    } else {
        pwdMessage.textContent = "Valid password.";
        pwdMessage.style.color = "green";
        pwdMessage.style.display = "block";
        formFlag = true;
        delete errorsList['pwd'] // Remove the third error if it exists
    }
})

myForm.addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent the default form submission
    console.log(errorsList)
    if (!errorsList['name'] && !errorsList['email'] && !errorsList['pwd']) {
        myForm.submit()
    }
    
});
// let myStr = "Hello From ITI fullstack python course";
// console.log(myStr.charAt(11)); // I
// console.log(myStr.charAt(11)); // I
// console.log(myStr[11]); // 11
// console.log(myStr.lastIndexOf(" ")); 
// console.log(myStr.substring(6, 11)); // From
// console.log(myStr.replaceAll('I','@'));

// // Hello From @T@ fullstack python course

// function returnDomain(email) {
//     indexOfAt = email.indexOf('@');
//     subStr = email.substring(indexOfAt + 1, email.length);
//     return subStr;
// }

// console.log(returnDomain("youssef@gmail.com")); // should return "gmail.com"

// let myStr = "    Hello From ITI fullstack python course  ";

// console.log(myStr); // I
// console.log(myStr.trim()); // I
// console.log(myStr.trimStart()); // I
// console.log(myStr.trimEnd()); // I

// let myStr = "Hello From ITI fullstack python course";
// console.log(myStr.split(' ')); // youssef
// console.log(myStr.toLowerCase()); // youssef
// console.log(myStr.toUpperCase()); // YOUSSEF
// console.log(myStr.bold()); // YOUSSEF
// document.write(myStr.bold()); // YOUSSEF
// document.write(myStr.fontcolor("red")); // YOUSSEF
// let firstName = "Youssef";
// let lastName = "Mohamed";
// let fullName = firstName.concat(" ", lastName);
// console.log(fullName); // Youssef Mohamed

// let myArr = new Array();
// console.log(myArr); // [ <10 empty items> ]

// let myArr = new Array([10,20,30,40,50,60,70,80,90,100]);
// console.log(myArr); // [10, 20, 30, 40,

// let myArr = [10,20,30,40,50,60,70,80,90,100];
// console.log(typeof myArr); // [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

// let myStudents = ['Mohamed','Abdo','Ibrahim',
//                     'Anton','Alaa','Ali','Ahmed'];
// console.log(myStudents[0]); // Mohamed
// console.log(myStudents.length); // ['Mohamed','Abdo','Ibrahim','Anton','Alaa']
// console.log(myStudents.join(',')); // Mohamed
// myStudents.push('Ahmed')
// console.log(myStudents); // ['Mohamed','Abdo','Ibrahim','Anton','Alaa','Ahmed']
// myStudents[myStudents.length] = 'Ahmed';
// console.log(myStudents); // ['Mohamed','Abdo','Ibrahim','Anton','Alaa',undefined,'Ahmed']
// delete myStudents[myStudents.length - 1];
// let removedEl = myStudents.pop(); // Removes the last element
// console.log(removedEl); // ['Mohamed','Abdo','Ibrahim','Anton','
// myStudents.shift()
// myStudents.unshift('Mohamed'); // Adds an element to the beginning
// console.log(myStudents); // ['Mohamed','Abdo','Ibrahim','Anton','Alaa']

//  myStudents.copyWithin(1,1)
//  console.log(myStudents); // ['Mohamed','Abdo','Mohamed','Abdo','Ibrahim','Anton','Alaa']

// myStudents[2] = myStudents[0];
// console.log(myStudents); // ['Mohamed','Abdo','Mohamed','Anton','A

// console.log(myStudents.reverse())
// console.log(myStudents.slice(1, 4)); // ['Abdo','Ibrahim']
// console.log(myStudents.sort()); // ['Abdo','Ahmed','Alaa','Anton','Ibrahim','Mohamed']

// let assosciativeArray = []
// assosciativeArray['name'] = 'Youssef';
// assosciativeArray['name'] = 'Mohamed';

// console.log(assosciativeArray); // Youssef

// let multiDimensionalArray = [['Youssef', 'Mohamed', 'Ahmed'],['Ali', 'Alaa', 'Ibrahim'],['Anton', 'Abdo', 'Mohamed']];
// console.log(multiDimensionalArray); // Mohamed
// fname = 'Youssef';
// lname = 'Mohamed';
// let myObject = {
//     fname: 'Youssef',
//     lname: 'Mohamed',
//     age: 25,
//     fullname: () => {
//         return this.fname + ' ' + this.lname;
//     },
//     subjects: ['Math', 'Science', 'English'],}

// // console.log(myObject.age); // { name: 'Youssef', age: 25, isStudent: true, subjects: [ 'Math', 'Science', 'English' ] }
// delete myObject.age;
// // console.log(myObject); // { name: 'Youssef', isStudent: true,
// // myObject['degree'] = 'Bachelor of Science';
// console.log(myObject.fullname()); // { name: 'Youssef', isStudent: true,

// console.log(Math.PI); // 3.141592653589793
// console.log(Math.random()); // 2.718281828459045
// let num = 10.5;
// console.log(Math.ceil(num)); // 2.718281828459045
// console.log(Math.floor(num)); // 2.718281828459045
// console.log(Math.round(num)); // 2.718281828459045
// console.log(Math.ceil(Math.random()*10000000)); // 
// let date = new Date(); // 2023-11-14 00:00:00
// var date2 = date.toDateString("YYYY"); // 2023-11-14 00:00:00
// console.log(date2) // 1700000000000
// let myArr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// for (let i = 0;true;i++){
//     console.log(i)// Skip the iteration when i is 5   
//     if (i == 10) break // Output the value of i to the console
// }
// var x = 0
// myArr.forEach(myFunction);
// function myFunction(i) {
//     if (i == 5) {
//         x += i; // Add the value of i to x
//         return; // Skip the iteration when i is 5
//     }
// }
//  // Output the value of x to the console
//  console.log(x);


// let x = 0;  

// while (x < 10) { // Continue the loop while x is less than 10
//     console.log(x); // Output the value of x to the console
//     x++; // Increment x by 1
// }

// do {
//     x++;
//     console.log(x); // Output the value of x to the console
//      // Increment x by 1
// }
// while (false); // Continue the loop while x is less than 10
// let password

// for(;password != "1234"; ) {
   
//     console.log(i); // Output the value of i to the console
// }
// while (password !== "1234") {
//     password = prompt("Please enter your password:");
// }

// alert("Password accepted!");


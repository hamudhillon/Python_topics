/*
Coding and basic
variables
Data Types -> strings (collection of alpha numeric chars)
OP -> arthematic , logical( & , || , !) , condtional, assignment 
Condtions 
collections -> array
loops
functions
class
--------------------
DOM
Document Object Model
*/

// var a = 5;
// let a = 5;
// const a = 5;

// console.log(a);
// alert(a);
// document.write(a);

// var b = prompt("enter a value ");
// console.log(b.length);
// var i = parseInt(b);
// console.log(i);

// if (b.length < 10) {
//   console.log("B should be greater then 10 chars");
// } else if (b.length > 15) {
//   console.log("B should control its length");
// } else {
//   console.log("B is fine!!");
// }

// switch (b) {
//   case "RED":
//     console.log("B is Angery!!");
//     break;
//   case "Green":
//     console.log("B is Happy");
//     break;
//   case "Blue":
//     console.log("B is sad");
//     break;
//   default:
//     console.log("B is confused?????");
//     break;
// }

// var data = Array("a", "v", 3, 4);
// console.log(data[0]);
// for (var i = 0; i < data.length; i++) {
//   console.log(data[i]);
// }

// data.forEach((elemnt) => {
//   console.log(elemnt);
// });

// var a = 0;
// document.write("L<br>");
// while (a < 100) {
//   document.write("O<br>");
//   a++;
// }
// document.write("P<br>");
// var a = 0;
// do {
//   document.write("I am statement <br>");
//   a++;
// } while (a <= 5);

// var data = ["verna", "volvo", "bmw"];

// console.log(data[0]);
// // var data = {
// //   name: "Harman",
// //   phone: 34567890,
// // };

// // console.log(data.phone);
// data.length;
// data.sort();
// console.log(data[data.length - 1]);
// data.push("honda");
// console.log(data);
// data.pop();
// console.log(data);

// function sum(n1, n2) {
//   // console.log(n1 + n2);
//   return n1 + n2;
// }

// console.log(sum(1, 4));
// class A {
//   name = "Class a";
//   show() {
//     console.log(this.name);
//   }
// }

// var obj = new A();
// obj.show();

// DOM
// Selection
// Events
// Form Validation
// Css Munipulatoion

//SELECTIONS

// getElementById();
// getElementsByClassName();
// getElementsByTagName();

// querySelector()
// querySelectorAll()

// var bgcolor = prompt("Enter bgcolor name ");
// var color = prompt("Enter Color name ");
// var h1 = document.querySelector("h1");
// h1.style.background = bgcolor;
// h1.style.color = color;

// var eli = document.createElement("img");

// // eli.innerText = "Bold tag Created With JavaScript";
// eli.setAttribute(
//   "src",
//   "https://images.unsplash.com/photo-1659586548923-77d2029e9b78?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
// );

// document.body.appendChild(eli);

// Q1
var fruits = ["Apple", "Orange", "banana"];

// Q2
var data = [
  {
    Name: "Apple",
    img: "https://images.unsplash.com/photo-1579613832125-5d34a13ffe2a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8YXBwbGV8ZW58MHx8MHx8&auto=format&fit=crop&w=600&q=60",
  },
  {
    Name: "orange",
    img: "https://images.unsplash.com/photo-1547514701-42782101795e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80",
  },
];

// EVENTS

// var h1 = document.querySelector("h1");
// var color_pointer = 0;
// var colors = ["red", "orange", "green", "blue", "yellow"];
// h1.addEventListener("drag", function () {
//   if (color_pointer < colors.length) {
//     this.style.color = colors[color_pointer];
//   } else {
//     color_pointer = 0;
//     this.style.color = colors[color_pointer];
//   }
//   color_pointer++;
// });

// function colorChnage() {
//   var h1 = document.querySelector("h1");
//   if (color_pointer < colors.length) {
//     h1.style.color = colors[color_pointer];
//     color_pointer++;
//   } else {
//     color_pointer = 0;
//     h1.style.color = colors[color_pointer];
//   }
// }

var btn = document.querySelector("button");
let ul = document.createElement("ul");
var check_list = [];
btn.addEventListener("click", function () {
  var val = document.querySelector('input[name="list_value"]').value;
  if (!check_list.includes(val)) {
    let li = document.createElement("li");
    li.innerText = val;
    ul.appendChild(li);
    check_list.push(val);
  }
});

document.body.appendChild(ul);

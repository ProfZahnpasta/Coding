console.log(`program works`);
//window.alert(`this is alert`);

document.getElementById("myh1").textContent = "Hello";
document.getElementById("lorem").textContent = "lorem";

let myname = "ProfZ"
let age = 25;
console.log(`My name is ${myname}.`)
console.log(`You are ${age} years old`);
console.log(typeof age)
console.log(typeof myname)

let computer_on = true;
let on_or_off = null;


if (computer_on == true) {
    on_or_off = "on";
} else {
    on_or_off = "off"; }

console.log(`${myname}'s computer is ${on_or_off} `)
document.getElementById("lorem").textContent = `${myname}'s computer is ${on_or_off} `;
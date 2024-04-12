//prompt the user to write their name
name = prompt("What is your first name? ")
//Make their first name's first Character Capital and the rest of the names lower case 
//step1: isolate the first character by slicing it out
var firstChar = name.slice(0,1);
//step2: capialize the first character
var capFirstChar = firstChar.toUpperCase();
//step3: isolate rest of the name
var restOfName = name.slice(1,name.length);
//step4: make the rest of the characters lower case
var restOfNames = restOfName.toLowerCase();
//step5: concatenate the name to one name following the above instruction
capitalisedName = ("Hello " + capFirstChar + restOfNames);
console.log(capitalisedName);

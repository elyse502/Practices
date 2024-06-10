let text = "javasrcipt is amazing";

let upperCaseText = text.toUpperCase();
let lowerCaseText = text.toLowerCase();

console.log("upper case : ", upperCaseText);
console.log("lower case : ", lowerCaseText);


let lyrics = "oh i wanna dance with somebody!";

let sliceText = lyrics.slice(4, 10);
let subStringText = lyrics.substring(11, 17);

console.log("Sliced text : ", sliceText);
console.log("SubString text : ", subStringText);


let song = " i will always love you ";

let newSong = song.replace("love", "music");

console.log("original song : ", song);
console.log("modified song : ", newSong);
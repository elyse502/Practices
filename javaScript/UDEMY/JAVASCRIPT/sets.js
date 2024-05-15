const uniqueNumbers = new Set([1, 2, 3, 4, 5, 1, 2]);
console.log(uniqueNumbers);


const programmingLanguages = new Set();

programmingLanguages.add("javascript");
programmingLanguages.add("python");
programmingLanguages.add("java");

console.log(programmingLanguages);
console.log(programmingLanguages.size);
console.log(programmingLanguages.has("javascript"));

programmingLanguages.delete("python");

console.log(programmingLanguages);
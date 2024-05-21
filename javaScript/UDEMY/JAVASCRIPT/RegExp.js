const patterrn = /hello/;
const text = 'hello, javascript!';

console.log(patterrn.test(text));


const patternWithClasses = /[aeiou]/g;
const textWithVowels = 'hello, javascript! this is a demonstration.';

console.log(textWithVowels.match(patternWithClasses));
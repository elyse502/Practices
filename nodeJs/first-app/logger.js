console.log(__filename); // __filename is a global object that represents the file name
console.log(__dirname); // __dirname is a global object that represents the directory name


var url = 'http://mylogger.io/log';

function log(message) {
    // Send an HTTP request
    console.log(message);
}

module.exports.log = log; // Exporting the log function
// module.exports = log; // Exporting the log function as a "function" instead of an "object"
// module.exports.endPoint = url; // Exporting the url variable
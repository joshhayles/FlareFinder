const statusLogPath = 'https://help.datadoghq.com/attachments/token/5bPyRk1nbAbWB1X9m4NLYhXYc/?name=datadog-agent-2023-08-16T22-21-37Z-trace.zip'

// Extract the last part of the URL
const splitLogPath = statusLogPath.split('=')[1];

// Define the REGEX pattern
const regexPattern = /(.+)-(\w+)\.zip/;

// Use RegExp.exec() to search for matches
const match = regexPattern.exec(splitLogPath);

if (match) {
    const status = match[2].charAt(0).toUpperCase() + match[2].slice(1);
    console.log(status);
} else {
    console.log("Unable to extract status information from the URL.");
}

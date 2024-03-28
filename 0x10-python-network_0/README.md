# 0x10. Python - Network #0
- Whenever you issue a URL from your browser to get a web resource using HTTP, e.g. http://www.nowhere123.com/index.html, the browser turns the URL into a request message and sends it to the HTTP server. The HTTP server interprets the request message, and returns you an appropriate response message, which is either the resource you requested or an error message.
- Curl (short for "Client URL") is a command line tool that enables data transfer over various network protocols. It communicates with a web or application server by specifying a relevant URL and the data that need to be sent or received.
- This project is concerned with using curl to communicate with a HTTP server.

0. cURL body size
	* Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
1. cURL to the end
	* Sends a GET request to the URL, and displays the body of the response
    * Display only body of a 200 Status code response
2. cURL Method
	* Ends a DELETE request to the URL passed as the first argument and displays the body of the response
3. cURL only methods
	* Displays all HTTP methods the server will accept
4. cURL headers
	* Sends a GET request to the URL, and displays the body of the response
	* A header variable X-School-User-Id must be sent with the value 98
5. cURL POST parameters
	* Sends a POST request to the given URL
	* A variable email must be sent with the value test@gmail.com
	* A variable subject must be sent with the value I will always be here for PLD
6. Find a peak
	* Function that finds a peak in a list of unsorted integers
7. Only status code
	* Displays only the status code of the response after sending a request to URL
	* Don't use pipe or redirection
8. cURL a JSON file
	* Sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.


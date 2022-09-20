Course: MIS 543 Online - Business Data Communications & Networking

XC: Simple Python Project

<b>Goal</b>: You will develop a python program that can parse a given url to obtain the domain, path, and port number, and write them to a file.

The program will take two command line parameters: the url that has to be parsed and the test filename where the results are stored. Examples of the command are: 'python url_parse.py http://www.arizona.edu/index.html url_parse.txt

Call a function url_parser() that will do the following:
<ul>
  <li> The function argument must be the url and filename obtained form command line arguments</li>
  <li> Parse the url to obtain the domain name, path and port number. If the port number is 'None' then the port number must be recorded as '80'</li>
  <li> Write the url, its domain name, path and port number to the file obtained from second command line argument</li>
</ul>

For example, if the URL is "http://www.eller.arizona.edi:2016/index/html", the following should be written to the file:
> url: http://www.eller.arizona.edu:2016/index.html
>
> host: www.eller.arizona.edu
>
> path:/index.html
>
> port: 2016
>

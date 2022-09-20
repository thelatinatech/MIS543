import sys
from urllib.parse import urlparse

def url_parser(param_url, filename):

    url_parsed = urlparse(param_url)
    # print("url_parsed is ", url_parsed) 

    # GET URL
    url = param_url
    # print(url)

    # GET ATTR_HOST
    attr_host = (url_parsed.hostname)
    # print(attr_host)

    # GET PORT 
    if url_parsed.port is None:
      attr_port = "port: 80"
    else: 
      attr_port = url_parsed.port
    # print(attr_port)

    #GET ATTR_PATH
    attr_path = url_parsed.path
    # print(attr_path)

    # filename for bottom section
    stored_file = open("file2save.txt", "w")
    stored_file.write(f"url: {url} \nhost: {attr_host} \nport: {attr_port} \npath: {attr_path}\n")
    stored_file.close()

    return filename

# obtain the command line parameters for url and filename
url = sys.argv[1] # url
file2save = sys.argv[2] # url_parse.txt

# function call to parse the url and store in file
stored_file = url_parser(url, file2save)

# display the filename which contains the parsed attributes of the url
print("The parsed attributes are stored in: %s" % stored_file)

# examples to test in shell:
# python main.py http://www.arizona.edu/index.html file2save.txt
# python main.py http://www.eller.arizona.edu/index.html file2save.txt

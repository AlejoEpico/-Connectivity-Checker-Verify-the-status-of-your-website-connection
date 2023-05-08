import urllib.request as urlib

def main(url):
    # Check if the protocol is missing and add it if needed
    if not url.startswith('http'):
        url = 'http://' + url
        
    print('Checking connection...')
    response = urlib.urlopen(url)
    print('Connected to', url, 'successfully')
    print('The response code was:', response.getcode())

print('This is a connectivity checker program.')
input_url = input('Input the URL that you want to check the status of connection: ')

main(input_url)

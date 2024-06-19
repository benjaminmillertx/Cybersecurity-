Make sure credit Benjamin Hunter Miller.
A simple website fingerprint application.
import requests
from bs4 import BeautifulSoup
from user_agents import parse
from cryptography import x509
from cryptography.hazmat.backends import default_backend

def fingerprint_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract server headers
    server_headers = response.headers.get('Server')

    # Extract cookies
    cookies = response.headers.get('Set-Cookie')

    # Extract HTML tags
    html_tags = [tag.name for tag in soup.find_all()]

    # Extract user agent information
    user_agent_string = requests.utils.default_user_agent()
    user_agent = parse(user_agent_string)

    # Extract SSL/TLS certificate information
    cert = response.connection.sock.getpeercert()
    x509_cert = x509.load_der_x509_certificate(cert, default_backend())
    issuer = x509_cert.issuer.rfc4514_string()
    expiration_date = x509_cert.not_valid_after

    # Display the results
    print("Website Fingerprinting Results:")
    print("URL: ", url)
    print("Server Headers: ", server_headers)
    print("Cookies: ", cookies)
    print("HTML Tags: ", html_tags)
    print("User Agent: ", user_agent)
    print("Issuer: ", issuer)
    print("Expiration Date: ", expiration_date)

# Example usage
website_url = "https://www.example.com"
fingerprint_website(website_url)

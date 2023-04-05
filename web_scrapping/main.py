# Import the necessary libraries
import requests  # Used for making HTTP requests
# Used for parsing and extracting structured data from HTML/XML documents
import selectorlib
import time

# Define the URL of the webpage to be scraped
URL = "http://programmer100.pythonanywhere.com/tours/"
# Define the headers to be sent along with the HTTP request
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# Define a function for scraping the page source from the URL


def scrape(url):
    """scrape the page source from URL"""
    # Make an HTTP GET request to the URL and retrieve the page source
    response = requests.get(url, headers=HEADERS)
    # Extract the page source as text
    source = response.text
    return source

# Define a function for extracting the relevant data from the page source


def extract(source):
    # Create an extractor object based on a YAML file that defines the structure of the data to be extracted
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    # extract the relevant data from the page source using the extractor object
    value = extractor.extract(source)["tours"]
    return value


def send_email():
    # did not send the email, code in send_email.py
    print("Email was sent")


def store(extracted):
    with open("data.txt", "a") as file:
        file.write(extracted + "\n")


def read(extracted):
    with open("data.txt", "r") as file:
        return file.read()


# defining the main program logic
if __name__ == "__main__":
    while True:
        # calll the scrape function to retrieve the page source of the URL
        scraped = scrape(URL)
        # Call the extract function to extract the relevant data from the page source
        extracted = extract(scraped)
        print(extracted)
        content = read(extracted)
        if extracted != "No upcoming tours":
            if extracted not in content:
                store(extracted)
                send_email()
        time.sleep(2)

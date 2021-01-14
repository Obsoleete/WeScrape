from bs4 import BeautifulSoup
import requests
import json

# Gets the html content for the given url
def get_content(url):

    response = requests.get(url, timeout=5)
    content = BeautifulSoup(response.content, "html.parser")

    return content

# Converts html content to json
def convert_to_json(content):

    json_array = []

    # Finds the needed data on the website
    historical_data = content.find('table', attrs={"data-test": "historical-prices"})
    table_body = historical_data.find('tbody')

    # Creates the array of json objects
    for row in table_body.findAll('tr'):

        data = row.findAll('td')

        json_object = {
            "Date": data[0].get_text(),
            "Open": data[1].get_text(),
            "High": data[2].get_text(),
            "Low": data[3].get_text(),
            "Close": data[4].get_text(), 
            "Adj Close": data[5].get_text(),
            "Volume": data[6].get_text()
        }

        json_array.append(json_object)

    return json_array

# Exports a given array of json objects to a json file
def export_to_json(json_array):

    with open('stockData.json', 'w') as outfile:
        json.dump(json_array, outfile)


if __name__ == "__main__":

    # Test functions
    content = get_content("https://ca.finance.yahoo.com/quote/CL%3DF/history?p=CL%3DF")
    json_array = convert_to_json(content)
    export_to_json(json_array)
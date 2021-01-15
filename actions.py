from bs4 import BeautifulSoup
import requests
import json

# Gets the html content for the given url
def get_content(urls):

    responses = [requests.get(url, timeout=5) for url in urls]
    contents = [BeautifulSoup(response.content, "html.parser") for response in responses]

    return contents

# Converts html content to json
def convert_to_json(contents):

    json_arrays = []

    # Finds the needed data on the website
    historical_datas = [content.find('table', attrs={"data-test": "historical-prices"}) for content in contents]
    table_bodies = [historical_data.find('tbody') for historical_data in historical_datas]

    # Creates the array of json objects
    for table_body in table_bodies:

        json_array = []

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
        
        json_arrays.append(json_array)

    return json_arrays

# Exports a given array of json objects to a json file
def export_to_json(json_arrays):

    for i in range(1, len(json_arrays) + 1):
        with open('stockData' + str(i) + '.json', 'w') as outfile:
            json.dump(json_arrays[i-1], outfile)


if __name__ == "__main__":

    # Test functions
    content = get_content(["https://ca.finance.yahoo.com/quote/CL%3DF/history?p=CL%3DF"])
    json_array = convert_to_json(content)
    export_to_json(json_array)
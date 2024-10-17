import urllib.request as urllib2
import json

while True:
    ip = input("What is Your Target Ip: ")
    url = "http://ip-api.com/json/"

    try:
        response = urllib2.urlopen(url + ip)
        data = response.read()
        values = json.loads(data)

        # Print the full response for debugging
        print("Full response: ", values)

        # Accessing values safely using .get()
        print("IP: " + values.get("query", "Not found"))
        print("City: " + values.get("city", "City not found"))
        print("ISP: " + values.get("isp", "ISP not found"))
        print("Country: " + values.get("country", "Country not found"))
        print("Region: " + values.get("region", "Region not found"))
        print("Timezone: " + values.get("timezone", "Timezone not found"))

    except Exception as e:
        print("An error occurred: ", e)

    break

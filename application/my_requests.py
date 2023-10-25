# import the requests module
import requests


# Create the class
class MyRequests:

    def __init__(self):
        self.base_url = None
        self.url = None

    # method that makes the call to the API using the get method
    def request_data(self):
        return requests.get(self.url)

    # method that assembles the url to request data from the hello endpoint
    def hello(self):
        self.url = f"{self.base_url}hello"
        return self.request_data()

    # method that calls data from the "name" endpoint?
    def name_endpoint(self):
        self.url = f"{self.base_url}name"
        return self.request_data()

    # method that calls data from the "VariantValidator" endpoint?
    def VariantValidator_endpoint(self, genome_build, variant_description, select_transcripts):
        self.url = '/'.join([self.base_url, genome_build, variant_description, select_transcripts])
        return self.request_data()


if __name__ == "__main__":
    mrq = MyRequests()

    # Set the base url
    mrq.base_url = "http://127.0.0.1:5000/"

    # request the data
    response = mrq.hello()

    # print the 3 response sections
    print(response.status_code)
    print(response.headers)
    print(response.text)
    print(response.json())
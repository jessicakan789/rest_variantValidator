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
    def name_endpoint(self, name):
        self.url = f"{self.base_url}name/{name}"
        return self.request_data()

    # method that calls data from the "VariantValidator" endpoint?
    def VariantValidator_endpoint(self, genome_build, variant_description, select_transcripts):
        self.url = f"{self.base_url}VariantValidator/variantvalidator/{genome_build}/{variant_description}/{select_transcripts}"
        return self.request_data()


if __name__ == "__main__":
    mrq = MyRequests()

    # Set the base url
    mrq.base_url = "http://127.0.0.1:5000/"

    # request the data from different endpoints
    response_1 = mrq.hello()
    response_2 = mrq.name_endpoint("Bob")
    response_3 = mrq.VariantValidator_endpoint("GRCh37", "NM_000088.3:c.589G>T", "'all'")

    # method that prints the 3 response sections
    def print_response(response):
        print(response.status_code)
        print(response.headers)
        print(response.text)
        print(response.json())


    # call data using responses
    print_response(response_1)
    print_response(response_2)
    print_response(response_3)


# How to run:
# conda activate variantvalidator
# python app_v5.py
# python my_requests.py

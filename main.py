import boto3
import pprint

domain = input("What domain do you want?: ")
client = boto3.client('route53domains')

response = client.check_domain_availability(
        DomainName=domain )
pprint.pprint(response)
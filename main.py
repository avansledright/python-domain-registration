import boto3
import pprint
import sys


client = boto3.client('route53domains')

if sys.argv[1] == "--help":
    print("USAGE: python3 main.py domainname")
else:
    response = client.check_domain_availability(
            DomainName=sys.argv[1])
    pprint.pprint(response) 
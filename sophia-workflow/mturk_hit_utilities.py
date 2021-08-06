"""
The last usage of this script was to delete HITs from a file named 500_jeb_hits.csv, which contains the 500 JEB HITs
that I had originally posted to MTurk but wanted to have removed.
"""

import boto3
from datetime import datetime
import csv

session = boto3.Session(profile_name='GRC-VE00-PeTaL-Lab-Mturk-sstiles2')
client = session.client(
    service_name='mturk',
    region_name='us-east-1',
    endpoint_url='https://mturk-requester-sandbox.us-east-1.amazonaws.com',
)


def expire_hit():
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    
    with open('500_jeb_hits.csv') as csvfile:  # modify this file name to whatever contains the list of MTurk HITs
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            hit_id, url = row
            response = client.update_expiration_for_hit(
                HITId=hit_id,
                ExpireAt=timestamp,
            )


def delete_hit():
    with open('500_jeb_hits.csv') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            hit_id, url = row
            response = client.delete_hit(
                HITId=hit_id,
            )

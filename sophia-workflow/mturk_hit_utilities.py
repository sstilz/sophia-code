import boto3
from datetime import datetime
import time
import csv

session = boto3.Session(profile_name='GRC-VE00-PeTaL-Lab-Mturk-sstiles2')
client = session.client(
    service_name='mturk',
    region_name='us-east-1',
    endpoint_url='https://mturk-requester-sandbox.us-east-1.amazonaws.com',
)


def update_hit_expiration():
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    
    with open('../sophia-data/50_jeb_hits.csv') as csvfile:  # modify this file name to whatever contains the list of MTurk HITs
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            hit_id, url = row
            response = client.update_expiration_for_hit(
                HITId=hit_id,
                ExpireAt=time.mktime(time.strptime('09/15/2021', "%m/%d/%Y")),  # to just change the expiration date
                # ExpireAt=timestamp  # if you'd like to expire the HIT now
            )


def delete_hit():  # you must expire the HIT before you can delete it!
    with open('../sophia-data/50_jeb_hits.csv') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            hit_id, url = row
            response = client.delete_hit(
                HITId=hit_id,
            )


update_hit_expiration()

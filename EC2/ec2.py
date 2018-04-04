###################################################
# EC2 Subapplication. Used for API access to EC2. #
# Requires AWS CLI with ec2-user profile.         #
###################################################
import sys
import os
import boto3
from collections import defaultdict

class EC2Instances():
    def __init__(self, instances, region):
        self.session = boto3.Session(profile_name='ec2-user')
        self.ec2_client = self.session.client('ec2')

    def get_instance_data(self):
        try:
            self.instances = self.ec2_client.instances.filter(
                    Filters=[{'Name': 'instance-state-name', 'Values': ['running','stopped']}])
            ec2info = defaultdict()
            for instance in self.instances:
                for tag in instance.tags:
                    if 'Name' in tag['Key']:
                        name = tag['Value']
                ec2info[instance.id] = {
                        'Name': name,
                        'Type': instance.instance_type,
                        'State': instance.state['Name'],
                        'Private IP': instance.private_ip_address,
                        'Public IP': instance.public_ip_address,
                        }
                ec2_data = ['Name', 'Type', 'State', 'Private IP', 'Public IP']

    print()

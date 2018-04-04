#!/usr/bin/python3
import boto3
from collections import defaultdict

class AwsRoute53(object):
    def __init__(self, client, ip_service, domain, subdomain, hosted_zone_id, fqdn):
        self.client = boto3.client('route53')
        self.ip_service = "http://httpbin.org/ip"
        self.domain = domain
        self.subdomain = subdomain
        self.hosted_zone_id = hosted_zone_id
        self.fqdn = "{0}.{1}".format(self.subdomain, self.domain)

    def external_ip_check(self):


    def check_record_sets(self):
        records = self.client.list_resourse_record_sets(
            HostedZoneId=self.hosted_zone_id,
            StartRecordName=self.fqdn,
            StartRecordType='A',
        )

    def change_record_sets(self):
        response = self.client.change_resource_record_sets(
                HostedZoneId=self.hosted_zone_id,
                ChangeBatch={
                    'Comment': 'string',
                    'Changes': [
                        {
                            'Action': 'UPSERT',
                            'ResourceRecordSet': {
                                'Name': self.fqdn,
                                'Type': 'A',
                                'TTL': 123,
                                'ResourceRecords': [
                                    {
                                        'Value': self.ip_service
                                    },
                                ],
                            }
                        },
                    ]
                }
            )

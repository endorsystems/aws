#!/usr/bin/python3
##########################################################
#                  AWS Service Master Python             #
#                        For fun. :)                     #
##########################################################

# --Calling--
# r53 = AwsRoute53()
# r53.list_record_sets("VALUE") // r53.change_records()
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

class AwsEc2(object):
    def __init__(self):
        self.ec2 = boto3.client('ec2')

    def get_instance_status(self):
        ec2 = self.ec2
        ins_status = ec2.instances.filter(
            Filters=[{'Name': 'instance-state-name', 'Values': ['running', 'stopped']}])


    # def instance_control(self, ins_control):
    #     ec2 = self.ec2
    #     ins_control.stop = self.ec2.instances.filter(InstanceIds=ids).stop()
    #     ins_control.start = self.ec2.instances.filter(InstanceIds=ids).start()
    #     ins_control.terminate = self.ec2.instances.filter(InstanceIds=ids).terminate()

        # Not really sure this is needed
    # def get_ebs_volumes(self):
    #     ebs = self.ec2.volume('id')
    #     volumes = volume.describe_status(
    #         Filters=[{'Name': 'string', 'Values': ['string']}])
    #     for volume in volumes:
    #         print()

# class AwsS3(object):
#     def __init__(self):
#         self.s3 = boto3.client('s3')
#
#     def s3_pull(self):
#
#     def s3_push(self):
#
# class AwsSns(object):
#     def __init__(self):
#         self.sns = boto3.cliet('sns')
#
#     def sns_success(self):
#
#     def sns_failed(self):

# testing area

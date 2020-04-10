#!/bin/python3

import boto3
session=boto3.session.Session(profile_name="dev_root")
ec2_cli=session.client(service_name="ec2",region_name="us-east-1")

regions=[]
for each region_infor in ec2_cli.describe_regions().get('Regions'):
    regions.append(each_region_info.get('RegionName'))

print 'All regions for ec2 service are: \n',regions
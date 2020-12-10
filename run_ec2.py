#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:yuguang   498049919@qq.com

import os
import boto3

AMI = "ami-1234abcd"
INSTANCE_TYPE = "t2.micro"
KEY_NAME = "public-ec2"
SUBNET_ID = "subnet-123abc"
REGION = "us-west-2"
IAMINSTANCEPROFILE = {'Arn': 'arn:aws:iam::123456789:instance-profile/crawler-ec2'}
SECURITY_GROUP = ["sg-01234abcd"]

ec2 = boto3.client('ec2',region_name="us-west-2")

def lambda_handler(event,context):
    init_script = """#!/bin/bash
                aws s3 cp s3://mytest-us2/crawler.py /tmp/
                python /tmp/crawler.py"""

    instance = ec2.run_instances(
        ImageId=AMI,
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_NAME,
        SubnetId=SUBNET_ID,
        MaxCount=4,
        MinCount=2,
        InstanceInitiatedShutdownBehavior='terminate', 
        UserData=init_script,
        IamInstanceProfile=IAMINSTANCEPROFILE,
        SecurityGroupIds=SECURITY_GROUP
    )
    instance_id = instance['Instances'][0]['InstanceId']
    return instance_id

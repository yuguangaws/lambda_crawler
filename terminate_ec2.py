#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:yuguang   498049919@qq.com 
 
import boto3
from boto3.dynamodb.conditions import Key

def dynamodb_query_ec2():
    
    dynamodb = boto3.resource('dynamodb',region_name='us-west-2')
    table = dynamodb.Table('crawler_verify')
    response = table.query(
        IndexName="status-index",
        KeyConditionExpression=Key('status').eq('OK'),
    )
    return response
    #for item in resp['Items']:
        #return item

def lambda_handler(message,context):
    ec2 = boto3.client('ec2', region_name='us-west-2')
    LIST = dynamodb_query_ec2()
    for ITEM in LIST['Items']:
        EC2_ID = ITEM['EC2_ID']
        ec2.terminate_instances(InstanceIds=[EC2_ID])


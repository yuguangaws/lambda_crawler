# This project include 3 part . 
run_ec2.py to invoke several EC2 to run the crawlers . Replace the parameter of your environment.

crawler.py running on the EC2 when EC2 launched and write result in DynamoDB .

terminate_ec2.py check the crawler result in DynamoDB if the result is OK then terminate the EC2 .

You can define the lambda running rate in Cloudwatch by schedule or event driven.

# this project include 3 part . 
A lambda function invoke several EC2 to run the crawlers . Replace the parameter of your environment.
A crawler  running on the EC2s and write result in DynamoDB when EC2 launched . 
A lambda check the crawler result in DynamoDB if it is OK then terminate the EC2 .

You can define the lambda running rate in Cloudwatch by schedule or event driven.

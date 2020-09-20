import json
import boto3

def lambda_handler(event, context):
    
    for i in event["Records"]:
        action = i["eventName"]
        time = i["eventTime"]
        ip = i["requestParameters"]["sourceIPAddress"]
        bucket_name = i["s3"]["bucket"]["cbsp-alm-data-backup"]
        object = i["s3"]["object"]["key"]
        table_name = object.split('/')
        t = table_name[0]
    client = boto3.client("ses")
    
    subject = 'Notification : ' + str(t) + ' Files Transferred at ' + str(time) + ' - Status: Succeed'
    body = """
        <br>
        <h2>This email is to notify you regarding <em>{}</em> event </h2>
        <br>
        <b>Bucket name :</b> <em>{}</em>
        <br>
        <b>File name :</b>  <em>{}</em>
        <br>
        <b>File uploaded time :</b> <em>{}</em>
        <br>
        <b>Source IP :</b> <em>{}</em>
        <br>
        <b>Status :</b> successfully done
        
    """.format(action,bucket_name,object,time,ip)
    
    message = {"Subject": {"Data" : subject}, "Body": {"Html":{"Data": body}}}
    
    response = client.send_email(Source= "test@XXX.com", Destination = {"ToAddresses": ["test1@xxx.com"]}, Message = message)
 
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
Output:

This email is to notify you regarding ObjectCreated:Put event 

Bucket name : xxx-yyy
File name : test/test/incoming/test.csv 
File uploaded time : 2020-01-21T03:39:22.451Z 
Source IP : 10.0.64.133 
Status : successfully done 
PS:This is an auto generated email
Thanks and Regards,

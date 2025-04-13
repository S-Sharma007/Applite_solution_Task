import boto3
import os
import json

sns = boto3.client('sns')

def lambda_handler(event, context):
    print("Event:", json.dumps(event, indent=2))

    detail = event.get('detail', {})
    request_params = detail.get('requestParameters', {})

    db_identifier = request_params.get('dBInstanceIdentifier') or request_params.get('dBClusterIdentifier')
    deletion_time = detail.get('eventTime')
    initiator = detail.get('userIdentity', {}).get('principalId')
    region = detail.get('awsRegion')

    message = f"""
    RDS Deletion Alert:
    DB Identifier: {db_identifier}
    Deletion Time: {deletion_time}
    Initiator: {initiator}
    Region: {region}
    """

    try:
        response = sns.publish(
            TopicArn=os.environ['SNS_TOPIC_ARN'],
            Message=message,
            Subject='RDS Deletion Alert'
        )
        print('Alert sent successfully:', response)
    except Exception as e:
        print('Error sending alert:', str(e))
        raise e

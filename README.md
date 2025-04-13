**RDS Deletion Monitoring System - Detailed Implementation Guide**

**Navigate to AWS CloudTrail Console**

** 1. Create Trail:**
Name: RDSeventstrail

Storage location: Create new S3 bucket

Enable for all regions: Yes

Management events: Enabled

Ensure RDS is not excluded

![Creation_Cloud_trail_1A](https://github.com/user-attachments/assets/f6edc8b1-327e-4b47-b127-cac343c6f99f)
![S3_Created_CloudTrail_logs_1B](https://github.com/user-attachments/assets/94928514-0876-47cc-8cc5-00ac8c8997cf)
![CloudTrail_Details_Complete_1C](https://github.com/user-attachments/assets/7c7c9795-fa9f-405c-b35f-7908b1cb22b0)


** 2. Creating SNS Topic**

Go to Amazon SNS Console:

**Create Topic:**

- Click "Create topic"
- Type: Standard
- Name: RDSDeleteAlert
- Display name: RDS Delete Monitor

- Protocol: Email
- Endpoint: your-email@domain.com
- Click "Create subscription"
- Confirm via email
- ![SNS_creation_2A](https://github.com/user-attachments/assets/cd44dd74-0154-4300-9016-883e611d1832)
- ![SNS_creation_2B](https://github.com/user-attachments/assets/25fd5453-6e06-4d76-a734-a0fb4a95daea)

** 3. Creating Lambda Function**

- Open Lambda Console
- Click "Create function"
- Configure:  - Author from scratch
- Name: RDS_deletion_function
- Runtime: Python 3.13
- Architecture: x86_64
![Lambdafunction_Creation_3A](https://github.com/user-attachments/assets/faca6f22-49a5-4cae-86d7-96457b2c7e3e)
![Lambda_function_Creation_3B](https://github.com/user-attachments/assets/c71a8c9e-ee7e-47c2-a2f3-0021f5a82c39)

** 4. Creation of the Lambda_function** 

- Check the lambda_function.py

![lambda_functioncode_5E](https://github.com/user-attachments/assets/e066fcb5-8278-4105-a259-472083ce7b93)
![Lambda_trigger_added_5B](https://github.com/user-attachments/assets/6a51745b-b454-4d33-b971-cff404237596)
![Lambda_Destination_added_5C](https://github.com/user-attachments/assets/3de0d1b5-6631-49ad-8f58-0308fc1bc95b)


** 5. Creating IAM Role**

![Policy_Role_attach_EventBridge_5A](https://github.com/user-attachments/assets/2d2eeec4-9bf7-4170-99fe-255788cd6f5b)
![IAM_Role_of_the_Lambda_5F](https://github.com/user-attachments/assets/7966f14d-4111-4403-ba43-9ffff1990adc)

** 6. Creation of the EventBridge_rule**

- FOr event pattern file - check the Event_Pattern.json file 
![EventBridge_rule_4A](https://github.com/user-attachments/assets/602d5796-4991-41ae-af42-8fde3875dd16)
![Event_pattern_code_file_4B](https://github.com/user-attachments/assets/028ea3bb-832d-4557-8d01-72bc90cc4b13)
![Event_Creation_step2_4C](https://github.com/user-attachments/assets/0556b4c8-fe80-46f5-9f5e-61918411b292)
![Event_Creation_Final_4D](https://github.com/user-attachments/assets/3c2561bd-f41a-48f4-b218-798ad642fc5d)
![Event_role_final_4E](https://github.com/user-attachments/assets/0f7ba1e4-9ea6-4837-bf14-e6db3846742e)

** 7. In Lambdafunction set environment Variables**

Key: SNS_TOPIC_ARN

Value: arn:aws:sns:[region]:[account-id]:RDSDeleteAlert

** 8.Code testing**
![Lambda_test_event_code_5D](https://github.com/user-attachments/assets/bd1a8306-0afb-47d7-8254-9513474e33dc)


** 9. Database - RDS**
![RDS_database_6A](https://github.com/user-attachments/assets/79a88ef1-a9ec-4631-88e2-81fb44df9ea2)

** 10. Final Notification in EMAIL**

![Final_email_notification_7A](https://github.com/user-attachments/assets/1dfb040a-0131-4f1e-80bc-2a68b4af97e0)

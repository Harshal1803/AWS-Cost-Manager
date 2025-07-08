Built a personalised AWS expense manager for EC2 instances and other services using AWS Lambda.
Sends messages on whatsapp using Twilio.
Which is all supported by Lambda's customised triggers.


![Screenshot 2025-07-09 004001](https://github.com/user-attachments/assets/8d5ca779-63ee-423e-bb53-8e97076ae62f)

**HOW IT WORKS**
1. Write the code(lambda_fucntion.py)
2. Configure Twilio 
```
pip install twilio
```
4. Generate the auth id, aut sid(it'll be essential in sending messages from twilio)
5. after that, create a new folder(inside the root folder)
```
pip install twilio -t .
   ```
6. zip it under some name 
```
zip -r function.zip .
```
8. Now Deploy this zip file to the AWS Lambda function
9. Add the environment variables for the credentials
10. Add inline policy for this(in JSON)
  ```
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Effect": "Allow",
			"Action": [
		         "ce:GetCostAndUsage"
			],
			"Resource": "*"
		}
	]
} 
```
9. Now Test it on the 'TEST' tab in lambda function
10. Youre good to go!
11. Iffffff, if you wanna add custom triggers, add in the triggers section and update the schedule timer
```
cron(* * * * *)
```
12. Now everything's ready, now you should see something like this on your whatsapp, whenever the lambda function is invoked
    
![Screenshot 2025-07-09 005409](https://github.com/user-attachments/assets/4083a006-a250-46ac-b81d-a1e23f2e1240)

(in my case it was set to trigger the function after every 5 minute lol)

   

 

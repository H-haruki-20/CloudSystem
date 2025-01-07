# クラウドの勉強用レポジトリ
(AWS lambdaから決まった時間にモチベーションを上げる言葉を投げかけるSlack bot)
### AWS Setup Instructions

1. **Create a Slack App:**
   - Go to https://api.slack.com/apps and create a new Slack App.
   - Enable the "Bot" feature and get the API token.
   
2. **Store Slack Bot Token in AWS Secrets Manager:**
   - Go to AWS Secrets Manager.
   - Store the Slack Bot token as `SLACK_API_TOKEN` in a secret named `SlackBotToken`.

3. **Create the Lambda function:**
   - In AWS Lambda, create a new Python 3.x function.
   - Upload the code from `lambda_function.py`.
   - Set the execution role for Lambda with permissions to read from Secrets Manager.

4. **Set up CloudWatch:**
   - In AWS CloudWatch, create a scheduled event rule.
   - Set the cron expression for daily execution at 9 AM UTC (`0 9 * * ? *`).
   - Set the target to trigger the Lambda function.

5. **Test:**
   - Once everything is set up, manually trigger the Lambda function to verify it's working.

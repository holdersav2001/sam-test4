aws --endpoint-url=http://localhost:4566 s3 mb s3://test-data

zip lambda_function.zip lambda_function.py

aws --endpoint-url=http://localhost:4566 lambda create-function --function-name my-lambda-function --zip-file fileb://lambda_function.zip --handler lambda_function.lambda_handler --runtime python3.11 --role arn:aws:iam::000000000000:role/irrelevant


aws --endpoint-url=http://localhost:4566 lambda replace-function --function-name my-lambda-function --zip-file fileb://lambda_function.zip --handler lambda_function.lambda_handler --runtime python3.11 --role arn:aws:iam::000000000000:role/irrelevant


{
  "LambdaFunctionConfigurations": [
    {
      "LambdaFunctionArn": "arn:aws:lambda:us-east-1:000000000000:function:my-lambda-function",
      "Events": ["s3:ObjectCreated:*"]
    }
  ]
}


aws --endpoint-url=http://localhost:4566 s3api put-bucket-notification-configuration --bucket test-data --notification-configuration file://notification.json

aws --endpoint-url=http://localhost:4566 s3api put-object --bucket test-data --key test-file.csv --body=test-file.csv

aws --endpoint-url=http://localhost:4566 logs tail '/aws/lambda/my-lambda-function' --follow


-------------------------------------------

aws --endpoint-url=http://localhost:4566 cloudformation create-stack --stack-name my-serverless-app --template-body file://serverless-application.yaml


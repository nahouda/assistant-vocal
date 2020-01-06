Readme :
1-conversation application :

### A WS Lambda Setup

1. Go to http://aws.amazon.com/. You will need to set-up an AWS account (the basic one will do fine) if you don't have one already. Make sure you use the same Amazon account that your Echo device isregistered to. **Note - you will need a credit or debit card to set up an AWS account - there is no way around this. Please see the AWS Charges section above**
2. Select Lambda from the AWS Services menu at the top left
3. Click on the "Create a Lambda Function" or "Get Started Now" button.
5. Select "Blank Function" - this will automatically take you to the "Configure triggers" page.
6. Click the dotted box and select "Alexa Skills Kit" (NOTE - if you do not see Alexa Skill Kit as an option then you are in the wrong AWS region).
7. Click Next 
8. Name the Lambda Function : exple‘conversation’
9. Select the runtime as "Python3.7".
10. paste the code conversation.py in function code environment .
### Alexa Skill Setup
1. In a new browser tab/window go to the Alexa Console https://developer.amazon.com/alexa/console/ask create a new skill named conversation application 
 2.Go to JSON EDITOR and paste the following code : 
{
    "interactionModel": {
        "languageModel": {
            "invocationName": "conversation application",
            "intents": [
                {
                    "name": "AMAZON.FallbackIntent",
                    "samples": []
                },
                {
                    "name": "AMAZON.CancelIntent",
                    "samples": []
                },
                {
                    "name": "AMAZON.HelpIntent",
                    "samples": [
                        "i need help",
                        "please help me ",
                        "i don't know how to use this app"
                    ]
                },
                {
                    "name": "AMAZON.StopIntent",
                    "samples": []
                },
                {
                    "name": "AMAZON.NavigateHomeIntent",
                    "samples": []
                },
                {
                    "name": "test",
                    "slots": [],
                    "samples": [
                        "i want to test my application",
                        "can you send the sample response",
                        "test test test test",
                        "run the test intent "
                    ]
                },
                {
                    "name": "compliment",
                    "slots": [],
                    "samples": [
                        "i would like for you to compliment me",
                        "can you say something nice about me",
                        "i need a pick me up",
                        "give me a compliment"
                    ]
                }
            ],
            "types": []
        }
    }
}

3. go to Endpoint select AWS Lambda ARN :
	Copy the skill id and paste it in the trigger alexa skills kit (in the aws account)
	Then , copy the ARN code of the function conversation found in the AWS account (arn:aws:lambda:eu-west-1:973484888424:function:conversation) and paste it in the blank Default Region

4.build the skill 
5.test the skill :
Alexa run conversation application 
Alexa give me a compliment please 
Alexa give me another compliment 
….

2-GOOGLE MAPS SKILL :
### Step 1: Get a Google Maps API key

**Server key**.

To get an API key:

 1. Visit https://developers.google.com/console and log in with
    a Google Account.
 2. Select one of your existing projects, or create a new project.
 3. Enable the API(s) you want to use. The Python Client for Google Maps Services
    accesses the following APIs:
    * Directions API
    * Distance Matrix API
    * Elevation API
    * Geocoding API
    * Geolocation API
    * Places API
    * Roads API
    * Time Zone API
 4. Create a new **Server key**.

For guided help, follow the instructions for the [Directions API][directions-key].
You only need one API key, but remember to enable all the APIs you need.
For even more information, see the guide to [API keys][apikey].

**Important:** This key should be kept secret.


### AWS Lambda Setup

1. Go to http://aws.amazon.com/. You will need to set-up an AWS account (the basic one will do fine) if you don't have one already. Make sure you use the same Amazon account that your Echo device is registered to. **Note - you will need a credit or debit card to set up an AWS account - there is no way around this. Please see the AWS Charges section above**
2. Select Lambda from the AWS Services menu at the top left
3. Click on the "Create a Lambda Function" or "Get Started Now" button.
4. Select "Blank Function" - this will automatically take you to the "Configure triggers" page.
5. Click the dotted box and select "Alexa Skills Kit" (NOTE - if you do not see Alexa Skill Kit as an option then you are in the wrong AWS region).
6. Click Next 
7. Name the Lambda Function : exple‘conversation’
8. Select the runtime as " Python 2.7".
9. Select Code entry type as "Upload a .ZIP file".
10. Click on the "Upload" button. Go to the folder where you unzipped the files you downloaded and select the nihedmaps.zip file

### Alexa Skill Setup
1. In a new browser tab/window go to the Alexa Console https://developer.amazon.com/alexa/console/ask create a new skill named conversation application 
 2.Go to JSON EDITOR and paste the following code : 
{
    "interactionModel": {
        "languageModel": {
            "invocationName": "google maps",
            "intents": [
                {
                    "name": "AMAZON.CancelIntent",
                    "samples": []
                },
                {
                    "name": "AMAZON.HelpIntent",
                    "samples": []
                },
                {
                    "name": "AMAZON.StopIntent",
                    "samples": []
                },
                {
                    "name": "GetCommuteToWork",
                    "slots": [],
                    "samples": [
                        "How is my commute",
                        "How is my commute to work",
                        "How is the traffic to work",
                        "How is the drive to work",
                        "My travel time to work"
                    ]
                },
                {
                    "name": "GetCommuteFromWork",
                    "slots": [],
                    "samples": [
                        "How is my commute home",
                        "How is my commute home from work",
                        "How is the traffic home",
                        "How is the drive home",
                        "My travel time home from work"
                    ]
                },
                {
                    "name": "GetDirectionsTo",
                    "slots": [
                        {
                            "name": "tocity",
                            "type": "AMAZON.City"
                        }
                    ],
                    "samples": [
                        "Get directions to {tocity}",
                        "How long does it take to get to {tocity}",
                        "How far is {tocity}",
                        "How far away is {tocity}",
                        "How far to {tocity}",
                        "How long to {tocity}",
                        "Give me directions to {tocity}",
                        "For directions to {tocity}"
                    ]
                },
                {
                    "name": "GetDirectionsFromTo",
                    "slots": [
                        {
                            "name": "fromcity",
                            "type": "AMAZON.City"
                        },
                        {
                            "name": "tocity",
                            "type": "AMAZON.City"
                        }
                    ],
                    "samples": [
                        "Get directions from {fromcity} to {tocity}",
                        "How long does it take to get from {fromcity} to {tocity}",
                        "How far is it from {fromcity} to {tocity}",
                        "How far from {fromcity} to {tocity}",
                        "How long from {fromcity} to {tocity}",
                        "Give me directions from {fromcity} to {tocity}",
                        "For directions from {fromcity} to {tocity}"
                    ]
                },
                {
                    "name": "AMAZON.NavigateHomeIntent",
                    "samples": []
                }
            ],
            "types": []
        }
    }
}

3. go to Endpoint select AWS Lambda ARN :
    Copy the skill id and paste it in the trigger alexa skills kit (in the aws account)
    Then , copy the ARN code of the function conversation found in the AWS account (arn:aws:lambda:eu-west-1:973484888424:function:conversation) and paste it in the blank Default Region

4.build the skill 
5.test the skill :
alexa run google maps 
 How far is it from tunis to london
 the weather in tunis 
 aryanah .....
Remember me where is my car
"# assisstant-vocal-" 

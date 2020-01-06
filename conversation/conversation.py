"""
This is a Python template for Alexa to get you building skills (conversations) quickly.
"""

from __future__ import print_function
import random


# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }

def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------
def get_test_response():
    """ An example of a custom intent. Same structure as welcome message, just make sure to add this intent
    in your alexa skill in order for it to work.
    """
    session_attributes = {}
    card_title = "Test"
    speech_output = "This is a test message"
    reprompt_text = "You never responded to the first test message. Sending another one."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
def get_compliment_response():
    """ An example of a custom intent. Same structure as welcome message, just make sure to add this intent
    in your alexa skill in order for it to work.
    """
    session_attributes = {}
    card_title = "compliment"
    compliments=["You're an awesome friend.",
"You're a gift to those around you.",
"You're a smart cookie.",
"You are awesome!",
"You have impeccable manners.",
"I like your style.",
"You have the best laugh.",
"I appreciate you.",
"You are the most perfect you there is.",
"You are enough.",
"You're strong.",
"Your perspective is refreshing.",
"I'm grateful to know you.",
"You light up the room.",
"You deserve a hug right now.",
"You should be proud of yourself.",
"You're more helpful than you realize.",
"You have a great sense of humor.",
"You've got an awesome sense of humor!",
"You are really courageous.",
"Your kindness is a balm to all who encounter it.",
"You're all that and a super-size bag of chips.",
"On a scale from 1 to 10, you're an 11.",
"You are strong.",
"You're even more beautiful on the inside than you are on the outside.",
"You have the courage of your convictions.",
"I'm inspired by you.",
"You're like a ray of sunshine on a really dreary day.",
"You are making a difference.",
"Thank you for being there for me.",
"You bring out the best in other people.",
"Your ability to recall random factoids at just the right time is impressive.",
"You're a great listener.",
"How is it that you always look great, even in sweatpants?",
"Everything would be better if more people were like you!",
"I bet you sweat glitter.",
"You were cool way before hipsters were cool.",
"That color is perfect on you.",
"Hanging out with you is always a blast.",
"You always know -- and say -- exactly what I need to hear when I need to hear it.",
"You help me feel more joy in life.",
"You may dance like no one's watching, but everyone's watching because you're an amazing dancer!",
"Being around you makes everything better!",
"When you say, 'I meant to do that,' I totally believe you.",
"When you're not afraid to be yourself is when you're most incredible.",
"Colors seem brighter when you're around.",
"You're more fun than a ball pit filled with candy. (And seriously, what could be more fun than that?)",
"That thing you don't like about yourself is what makes you so interesting.",
"You're wonderful.",
"You have cute elbows. For reals! ",
"Jokes are funnier when you tell them.",
"You're better than a triple-scoop ice cream cone. With sprinkles.",
"When I'm down you always say something encouraging to help me feel better.",
"You are really kind to people around you.",
"You're one of a kind!",
"You help me be the best version of myself.",
"If you were a box of crayons, you'd be the giant name-brand one with the built-in sharpener.",
"You should be thanked more often. So thank you!!",
"Our community is better because you're in it.",
"Someone is getting through something hard right now because you've got their back. ",
"You have the best ideas.",
"You always find something special in the most ordinary things.",
"Everyone gets knocked down sometimes, but you always get back up and keep going.",
"You're a candle in the darkness.",
"You're a great example to others.",
"Being around you is like being on a happy little vacation.",
"You always know just what to say.",
"You're always learning new things and trying to better yourself, which is awesome.",
"If someone based an Internet meme on you, it would have impeccable grammar.",
"You could survive a Zombie apocalypse.",
"You're more fun than bubble wrap.",
"When you make a mistake, you try to fix it.",
"Who raised you? They deserve a medal for a job well done.",
"You're great at figuring stuff out.",
"Your voice is magnificent.",
"The people you love are lucky to have you in their lives.",
"You're like a breath of fresh air.",
"You make my insides jump around in the best way.",
"You're so thoughtful.",
"Your creative potential seems limitless.",
"Your name suits you to a T.",
"Your quirks are so you -- and I love that.",
"When you say you will do something, I trust you.",
"Somehow you make time stop and fly at the same time.",
"When you make up your mind about something, nothing stands in your way.",
"You seem to really know who you are.",
"Any team would be lucky to have you on it.",
"In high school I bet you were voted 'most likely to keep being awesome.'",
"I bet you do the crossword puzzle in ink.",
"Babies and small animals probably love you.",
"If you were a scented candle they'd call it Perfectly Imperfect (and it would smell like summer).",
"There's ordinary, and then there's you.",
"You're someone's reason to smile.",
"You're even better than a unicorn, because you're real.",
"How do you keep being so funny and making everyone laugh?",
"You have a good head on your shoulders.",
"Has anyone ever told you that you have great posture?",
"The way you treasure your loved ones is incredible.",
"You're really something special.",
"Thank you for being you."]
    speech_output = compliments[random.randint(0,len(compliments)-1)]
    reprompt_text = "You never sss"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """
    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to Smart Car !"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "I don't know if you heard me, welcome to your custom alexa application!"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for trying the Alexa Skills Kit sample. " \
                    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts.
        One possible use of this function is to initialize specific 
        variables from a previous state stored in an external database
    """
    # Add additional code here as needed
    pass

    

def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """
    # Dispatch to your skill's launch message
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "test":
        return get_test_response()
    elif intent_name == "compliment":
        return get_compliment_response()
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.
    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("Incoming request...")

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
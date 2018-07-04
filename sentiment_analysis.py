import requests
import json


def analyze_tone(text):
    username = ''   # enter username according to your credentials
    password = ''   # enter password according to your credentials
    watsonUrl = 'https://gateway.watsonplatform.net/tone-analyzer/api/v3/tone?version=2016-05-18'
    headers = {"content-type": "text/plain"}
    data = text
    try:
        r = requests.post(watsonUrl, auth=(username, password), headers=headers,
                          data=data)
        return r.text
    except:
        return False


def welcome():
    message = "Welcome to the IBM Watson Tone Analyzer\n"
    print(message + "-" * len(message) + "\n")
    message = "How it works"
    print(message)
    message = "Perhaps a bit too aggressive in your emails? Are your blog posts a little too friendly? Tone Analyzer might be able to help. The service uses linguistic analysis to detect and interpret emotional, social, and writing cues found in text."
    print(message)
    print()
    print("Have fun!\n")

happy_score_list = []
sad_score_list = []

def display_results(data):
    data = json.loads(str(data))
    print(data)
    #for i in data['document_tone']['tone_categories']:
        #print(i['category_name'])
        #print("-" * len(i['category_name']))
    print(data['document_tone']['tone_categories'][0]['tones'][3]['score'])  ### happy score
    print(data['document_tone']['tone_categories'][0]['tones'][4]['score'])  ### sad score
    happy_score = data['document_tone']['tone_categories'][0]['tones'][3]['score']
    sad_score = data['document_tone']['tone_categories'][0]['tones'][4]['score']
    happy_score_list.append(happy_score)
    sad_score_list.append(sad_score)
    print("happy score list!"+ str(happy_score_list))


def analyze(tweets):
    welcome()

    #data = input("Enter some text to be analyzed for tone analysis by IBM Watson (Q to quit):\n")
    print("all tweets"+ str(tweets))
    count = 0
    for single_tweet in tweets:
        if count > 20:
            break
        if len(tweets) >= 1:
            if single_tweet == 'q'.lower():
                exit
            results = analyze_tone(single_tweet)
            if results != False:
                display_results(results)
            else:
                print("Something went wrong")
        count += 1 
    return sad_score_list

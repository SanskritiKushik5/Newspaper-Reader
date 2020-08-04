# Newspaper Reader
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    import requests
    import json
    url = ('https://newsapi.org/v2/top-headlines?''sources=the-times-of-india&''apiKey=deb63e7937dd416a83fc89be046cee73')
    req = requests.get(url)
    sk = req.text
    parsed = json.loads(sk)
    for i in range(0,11):
        speak(parsed['articles'][i]['title'])
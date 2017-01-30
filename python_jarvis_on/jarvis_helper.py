# Raspberry pi 3 model b
# USB камера logitech
# pip3 install SpeechRecognition
# pip3 install pocketsphinx
# sudo nano /usr/local/lib/python3.4/dist-packages/speech_recognition/pocketsphinx-data/en-US
# /pronounciation-dictionary.dict
# jarvis JH AA R V AH S
# https://github.com/ubaransel/lgcommander
# sudo apt-get install mpg123
#! /usr/bin/env python
# -*-coding:utf-8-*-
import os
import speech_recognition as sr
from xml.dom import minidom
import sys
import random

r = sr.Recognizer()

# https://tech.yandex.ru/speechkit/
ya_uuid = ''
ya_api_key = ''

# os.system('echo "Ассист+ент зап+ущен" |festival --tts --language russian')

def convert_ya_asr_to_key():
    xmldoc = minidom.parse('./asr_answer.xml')
    itemlist = xmldoc.getElementsByTagName('variant')
    if len(itemlist) > 0:
        return itemlist[0].firstChild.nodeValue
    else:
        return False

def jarvis_on():
    with sr.WavFile("send.wav") as source:
        audio = r.record(source)

    try:
        t = r.recognize_sphinx(audio)
        print(t)
    except LookupError:
        print("Could not understand audio")

    return t == ("jarvis")

def jarvis_say(phrase):
    os.system(
        'curl "https://tts.voicetech.yandex.net/generate?format=wav&lang=ru-RU&speaker=zahar&emotion=good&key='+ya_api_key+'" -G --data-urlencode "text=' + phrase + '" > jarvis_speech.wav')
    os.system('aplay jarvis_speech.wav')

def jarvis_sya_good():
    phrases = ["Готово", "Сделано", "Слушаюсь", "Есть", "Что-то еще?", ]
    randitem = random.choice(phrases)
    jarvis_say(randitem)

try:
    while True:
        os.system('arecord -B --buffer-time=1000000 -f dat -r 16000 -d 3 -D plughw:1,0 send.wav')
        if jarvis_on():
            os.system('aplay jarvis_on.wav')
            os.system('arecord -B --buffer-time=1000000 -f dat -r 16000 -d 3 -D plughw:1,0 send.wav')
            os.system(
                'curl -X POST -H "Content-Type: audio/x-wav" --data-binary "@send.wav" "https://asr.yandex.net/asr_xml?uuid='+ya_uuid+'&key='+ya_api_key+'&topic=queries" > asr_answer.xml')
            command_key = convert_ya_asr_to_key()
            if (command_key):
                if (command_key in ['key_word', 'key_word1', 'key_word2']):
                    os.system('')
                    jarvis_sya_good()
                    continue
                if (command_key in ['включи свет', 'включить свет', 'свет']):
                    os.system('python3 /home/pi/smarthome/hue/hue.py a1167aa91-on-0')
                    jarvis_sya_good()
                    continue
                if (command_key in ['приглуши свет', 'приглушить свет']):
                    os.system('python3 /home/pi/smarthome/hue/hue.py ac637e2f0-on-0')
                    jarvis_sya_good()
                    continue
                if (command_key in ['выключи свет', 'выключить свет']):
                    os.system('python3 /home/pi/smarthome/hue/hue.py  "off"')
                    jarvis_sya_good()
                    continue
                #1 - POWER
                #24 - VOLUNE_UP
                #25 - VOLUME_DOWN
                #400 - 3D_VIDEO
                if (command_key in ['выключи телевизор', 'выключить телевизор']):
                    os.system('python3 /home/pi/smarthome/TV/tv2.py 1')
                    jarvis_sya_good()
                    continue
                if (command_key in ['прибавь громкость', 'громче']):
                    os.system('python3 /home/pi/smarthome/TV/tv2.py 24')
                    jarvis_sya_good()
                    continue
                if (command_key in ['новости', 'выключи новости','что происходит']):
                    os.system('mpg123 URL')
                    continue

except Exception:
jarvis_say('Что-то пошло не так')
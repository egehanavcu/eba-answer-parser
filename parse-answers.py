# -*- coding: UTF-8 -*-

from PIL import Image, ImageDraw, ImageFont
from colorama import Fore, Back, Style, init
import sys
import time
import json
import requests
import configparser

init()

class EBA_Answer:
    def __init__(self, id, applicationid):
        self.url = 'https://ades-sinavsistemi.eba.gov.tr/adestek/ExamSystem/home/exam/performance/viewperformance.json'
        self.text = ""
        self.id = str(id)
        self.data = {
            'applicationid': applicationid,
            'examid' : examid
        }

        self.headers = {
            'Cookie': cookie
        }

        self.answersDict = {"0" : "A", "1" : "B", "2" : "C", "3" : "D", "4" : "E"}
        self.parse_answer()

    def parse_answer(self):
        r = requests.post(self.url, data=self.data, headers=self.headers)
        try:
            response = r.json()
            print(Fore.GREEN + " \"" + response["application"]["title"] + "\"" + Style.RESET_ALL + " cevapları çekildi.")
            for id, answer in enumerate(response["application"]["applicationUsers"][0]["answers"]):
                self.text += str(id+1) + "- " + self.answersDict[answer["correctAnswer"]] + "\n"
            self.text = response["application"]["title"] + "\n" + self.text
            self.draw_answers(25)
            self.draw_id(100)
            print(" " + Fore.YELLOW + str(len(response["application"]["applicationUsers"][0]["answers"])) + Style.RESET_ALL + " sorunun cevapları kaydedildi.\n")
        except json.decoder.JSONDecodeError:
            print(Fore.RED +" Update your cookie.")
            time.sleep(10)
            sys.exit()

    def draw_answers(self, font_size):
        fnt = ImageFont.truetype("arial.ttf", font_size)
        image = Image.new(mode = "RGB", size = (int(font_size/2)*max([len(i) for i in self.text.split("\n")]) + 50,(font_size+3)*self.text.count("\n")), color = "#555555")
        draw = ImageDraw.Draw(image)
        draw.text((10,10), self.text, font=fnt, fill=(158,158,158))
        image.save("./answers/" + self.data["applicationid"] + ".png")

    def draw_id(self, font_size):
        img = Image.open("./answers/" + self.data["applicationid"] + ".png")
        width, height = img.size
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", 100)
        draw.text((width/2-45, height/2-45), self.id, (255, 255, 255), font=font)
        img.save("./answers/" + self.data["applicationid"] + ".png")

config = configparser.ConfigParser()
config.read("./config")
cookie = config.get("Eba", "cookie")
examid = config.get("Eba", "examid")
applicationids = list(filter(None, json.loads(config.get("Eba", "applicationids"))))

print(Fore.RED + """
  _____ ____    _    
 | ____| __ )  / \   
 |  _| |  _ \ / _ \  
 | |___| |_) / ___ \ 
 |_____|____/_/   \_\\

""")
for id, applicationid in enumerate(applicationids):
    EBA_Answer(id+1, applicationid)
print(Fore.YELLOW + " Tüm cevaplar kaydedildi. 10 saniye sonra program kapanacak.")
time.sleep(10)

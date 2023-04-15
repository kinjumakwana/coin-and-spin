from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from django.db import IntegrityError
import schedule
import time
import demoji
import emoji
import re 
# from models import Post
import requests
# firebased 
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
# from django.conf import settings

# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "coinspinapp.settings")

# Setup
cred = credentials.Certificate("servicekey.json")
firebase_admin.initialize_app(cred)
db=firestore.client()
# db.collection('Post').add({'Title':'', 'Details':'aasdasd', 'Link': "https://Coin-Master.me/CqcECW"})

s = Service(r"D:\Kinjal\chromedriver_win32\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(service=s, options=options)

class Facebookboat:
    def __init__(self):
        self.driver = webdriver.Chrome(service=s, options=options)
        sleep(5)
        # self.driver = webdriver.Chrome(chrome_driver_path)

    def login(self):
        post_data = {}
        try:
            self.driver.get("https://www.facebook.com/coinmaster/")
            sleep(10)
            data = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[4]/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div")
            print(data)
            
            encode_text = data.text.encode('utf8')
            print('encode_text',encode_text)
            text = data.text
            # Extract URL 
            url_pattern = r'https?://\S+'
            matches = re.findall(url_pattern, text)

            if len(matches) > 0:
                link = matches[0]
                print('URL:', link)
                text = text.replace(link, '') # remove URL from text
                # Check if URL already exists in database
                query = db.collection('Post').where('Link', '==', link)
                existing_posts = query.get()

                dataget = db.collection('Post')
                print("get",dataget.get())
                
                for doc in dataget.stream():
                    print(f'{doc.id}')
                    # print(doc.to_dict())
                    # post = Post(id=doc.id, **doc.to_dict())
                    # data.append(post)
            
                if len(existing_posts) > 0:
                    print('URL already exists in database')
                else:
                    post_data['Detail'] = text
                    post_data['Link'] = link
                    post_data['Title'] = ''
                    db.collection('Post').add(post_data)
                    # addpost = Coinmaster.objects.create(title="",detial=text,link=url)
                    # addpost.save()
                    
                    try:
                        url = 'http://localhost:8000/add_post/'
                        data = {'detail': text, 'link': link, 'title':''}
                        response = requests.post(url, data=data)
                        print(response.content)
                    except IntegrityError:
                        print('URL already exists in Django database')
            else:
                post_data['Detail'] = 'No Data found'
                post_data['Link'] = 'No URL found'
                post_data['Title'] = ''
                db.collection('Post').add(post_data)
                print('No URL found.')
            
            # # get URL text like <a> hello </a> hello fetch
            # anchor_element = data.find_element(By.CSS_SELECTOR, 'a[role="link"]')
            # print(anchor_element.text)
            # # Get the href attribute
            # href_attribute = anchor_element.get_attribute('href')
            # print("href_attribute",href_attribute)
            # post_data = {'Title':'','Detail':data.text ,'Link':anchor_element.text}   
            # db.collection('Post').add(post_data)
            
            # Schedule the login function to run every 10 minutes
            # schedule.every(10).minutes.do(Fabboat.login())

            # Schedule the login function to run every day at 8:00 AM
            # schedule.every().day.at("08:00").do(Fabboat.login())

            # Run the scheduled tasks
            # while True:
            #     schedule.run_pending()
            #     time.sleep(1)
             
        except Exception as e:
            print(e)
            sleep(10)

Fabboat = Facebookboat()
Fabboat.login()

from selenium import webdriver  
import pyautogui
from selenium.webdriver.common.keys import Keys 
import time
import os

class InstaBot:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.bot=webdriver.Firefox() 
    

    def login(self):  
        bot=self.bot
        bot.get('https://www.instagram.com/accounts/login/')
        
        time.sleep(1)
        email=bot.find_element_by_name('username')
        password=bot.find_element_by_name('password')
        
        email.clear()
        password.clear()
        time.sleep(0.2)
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)
        
    def like_post(self,hashtag):
        count=0
        bot = self.bot
        bot.get('https://www.instagram.com/explore/tags/'+hashtag+'/')
        time.sleep(2)

        for i in range(1,500+1):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            posts = bot.find_elements_by_class_name('v1Nh3')
            links = [elem.find_element_by_css_selector('a').get_attribute('href') for elem in posts]
           
            for link in links:

                if(count<500+1):
                    bot.get(link)

                    try:
                        print("Click Action:")
                        #pyautogui.moveTo(615, 610, duration=0.1)
                        time.sleep(0.3)
                        for i in range(0, 2+1):
                            pyautogui.click(315, 480, button='left')
                            time.sleep(0.1)
                        print("Action: Liked! -> ", end=" ")
                        print(count)
                        print("-"*60)
                        count=count+1
                        time.sleep(0.2)

                    except Exception as ex:
                        time.sleep(5)

                else:
                    bot.close()

    def follow(self, amount): #function for following
    	bot = self.bot
    	bot.get("https://www.instagram.com/")
    	time.sleep(1)

    	pyautogui.click(954, 720, button='left')
    	print("Denied pop-up")
    	time.sleep(0.5)
    	bot.get("https://www.instagram.com/explore/people/suggested/")
    	print("page found!")
    	count=0
    		
    	for x in range(0, amount+1):
    		next_coor = 268
    		time.sleep(1)
    		for i in range(0, 13+1):
    			count += 1
    			pyautogui.click(1205, next_coor, button='left')
    			print("Action: Followed! -> ", end=" ")
    			print(count)
    			next_coor += 61 #parameter for the next follow button
    			time.sleep(0.5)

    		time.sleep(0.5)
    		bot.get("https://www.instagram.com/explore/people/suggested/")

''' pyautogui for bypassing code filters and safer exploiting: use the driver at your left side pannel 
    of your monitor! (or change the coordinates!) FULLSCREEN FOR FOLLOW '''

if __name__ == '__main__':
    os.system("cls") # can get changed to os.system("clear") at unix[...]
    obj = InstaBot('username','password') #username and passwd of your account
    obj.login()
    #obj.like_post('try') #the hastag
    obj.follow(100)
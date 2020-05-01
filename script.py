
import sys
import os.path
from os import path
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import jokes

# READ INSTRUCTIONS.TXT

file = path.exists("credentials.txt")

if file:
    f = open("credentials.txt", "r")
    f = f.read()
    f = f.splitlines()
    user = f[0]
    passwd = f[1]
    victim_username = f[2]
    print()
    print(" ay! session restored for user:", "@",user)
    print(" continue to spam @",victim_username,"? (y/n)")
    newvictim = input(" ")

    if newvictim == 'y':
        victim_username = f[2]
    else:
        newvictim = input(" Enter new victim's username: ")
        victim_username =  newvictim

    username = user
    password = passwd
    
else:
    print()
    username = input(" Enter your Instagram Username: ")
    password = input(" Password: ")
    victim_username = input("\n Victim's Username: ")
    f = open("credentials.txt", "a" )
    f.write(username)
    f.write("\n")
    f.write(password)
    f.write("\n")
    f.write(victim_username)
    f.close()
    checkprompt = input(" \nmake sure it's all correct, continue? (y/n): ")
    if checkprompt == 'y':
        pass
    else:
        os.remove("credentials.txt")
        sys.exit(" \nokay, run the script again to start over!")
    

number = 0

print("\n > What do you wanna spam?\n")
print(" 1. Lame jokes")
print(" 2. WHOLE BEE MOVIE SCRIPT!")
print("\n Press 1 or 2:")
choice = int(input(" "))
if choice == 2:
    spamChoice = 2
else:
    number = int(input("\n Enter amount of messages to send (integer): "))
    spamChoice = 1

print("\n Opening browser...")
print(" Use CTRL + C to stop the script")


class DMspam:
    def __init__(self, username, password, victim_username, number):
        self.username = username
        self.password = password
        self.victim_username = victim_username
        self.number = number
        self.browser = webdriver.Firefox()

    def login(self):
        browser = self.browser
        browser.implicitly_wait(5)
        browser.set_window_size(800, 800)
        browser.set_window_position(0, 0)
        browser.get('https://www.instagram.com/')
        browser.find_element_by_xpath("//input[@name='username']").send_keys(self.username)
        browser.find_element_by_xpath("//input[@name='password']").send_keys(self.password)
        browser.find_element_by_xpath("//button[@type='submit']").click()

    def victim_profile(self):
        browser = self.browser
        browser.implicitly_wait(5)
        sleep(5)
        not_now_button = browser.find_element_by_xpath("//button[text()='Not Now']")
        sleep(2)
        not_now_button.click()
        browser.find_element_by_xpath("//span[text()='Search']").click()
        browser.find_element_by_xpath("//input[@placeholder='Search']").send_keys(self.victim_username)
        sleep(1)
        browser.find_element_by_xpath("//span[text()='"+self.victim_username+"']").click()
        sleep(2)

    def spamming(self):
        spamChoice = choice 
        browser = self.browser
        browser.implicitly_wait(5)
        browser.find_element_by_xpath("//button[@type='button']").click()
        message_area = browser.find_element_by_xpath("//textarea[@placeholder='Message...']")
        message_area.click()

        if spamChoice == 2:
            f = open("BeeMovieScript.txt", "r")
            f = f.read()
            lst = f.split()
            for x in lst:
                message_area = browser.find_element_by_xpath("//textarea[@placeholder='Message...']")
                message_area.click()
                message_area.send_keys(x, Keys.ENTER)
                browser.implicitly_wait(.5)
        else:
            for i in range(0, self.number):
                message_area = browser.find_element_by_xpath("//textarea[@placeholder='Message...']")
                message_area.click()
                message_area.send_keys(jokes.get_msg(), Keys.ENTER)

        
if __name__ == '__main__':
        spam = DMspam(username, password, victim_username, number)
        spam.login()
        spam.victim_profile()
        spam.spamming()

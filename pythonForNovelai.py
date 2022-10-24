import requests
import json
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import base64
import os
mail = "286studio@gmail.com"
pw = "boston2022"
numOfImage = input("how much image?")
prompt = input("prompt?")
driver = webdriver.Safari()
def get_file_content(driver, uri):
  result = driver.execute_async_script("""
    var uri = arguments[0];
    var callback = arguments[1];
    var toBase64 = function(buffer){for(var r,n=new Uint8Array(buffer),t=n.length,a=new Uint8Array(4*Math.ceil(t/3)),i=new Uint8Array(64),o=0,c=0;64>c;++c)i[c]="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/".charCodeAt(c);for(c=0;t-t%3>c;c+=3,o+=4)r=n[c]<<16|n[c+1]<<8|n[c+2],a[o]=i[r>>18],a[o+1]=i[r>>12&63],a[o+2]=i[r>>6&63],a[o+3]=i[63&r];return t%3===1?(r=n[t-1],a[o]=i[r>>2],a[o+1]=i[r<<4&63],a[o+2]=61,a[o+3]=61):t%3===2&&(r=(n[t-2]<<8)+n[t-1],a[o]=i[r>>10],a[o+1]=i[r>>4&63],a[o+2]=i[r<<2&63],a[o+3]=61),new TextDecoder("ascii").decode(a)};
    var xhr = new XMLHttpRequest();
    xhr.responseType = 'arraybuffer';
    xhr.onload = function(){ callback(toBase64(xhr.response)) };
    xhr.onerror = function(){ callback(xhr.status) };
    xhr.open('GET', uri);
    xhr.send();
    """, uri)
  if type(result) == int :
    raise Exception("Request failed with status %s" % result)
  
  return result


def loginAndDownload(email, password):
    driver.get('https://novelai.net/login')
    username = driver.find_element("id","username")
    username.send_keys(email)
    PW = driver.find_element("id","password")
    PW.send_keys(password)
    PW.send_keys(Keys.RETURN)
    time.sleep(6)
    
    driver.find_element(By.XPATH,"/html/body/div[4]/div/div[1]/div/button").click()
    time.sleep(1)
    imagePage = driver.find_element(By.XPATH,"//*[@id=\"app\"]/div[3]/div[3]/div[1]/div/div/div[3]/a")
    action = ActionChains(driver)

    action.double_click(imagePage).perform()
    i = 0
    time.sleep(6)
    enterPrompt = driver.find_element("id","prompt-input-0")
    enterPrompt.send_keys(prompt)
    
    
    os.mkdir(prompt)
    while (i< int(numOfImage)):
        
        
        time.sleep(6)
        gen = driver.find_element(By.XPATH,"//*[@id=\"__next\"]/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[3]/button")
        gen.send_keys(Keys.RETURN)
        i += 1
        time.sleep(6)
        element = driver.find_element(By.TAG_NAME, "img")
        html = element.get_attribute('src')
        
        bytes = get_file_content(driver, html)
        filename = prompt+'/'+str(i)+'.jpg'  
        with open(filename, 'wb') as f:
            f.write(base64.b64decode(bytes))
        
        
        

loginAndDownload(mail,pw)



    
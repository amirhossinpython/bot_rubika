import os
import datetime
import time
import shutil
import random
from random import randint
from io import BytesIO 
import base64
import threading
import socket
import re
try:
    from deep_translator import GoogleTranslator

except ImportError:
    os.system("pip install deep_translator ")    
from requests import post

try:
    import pyowm
except ImportError:
    os.system("pip install pyowm")  
      
try:
    import sqlite3

except ImportError :
    os.system("pip install sqlite3")    

try:
    from pyrubi import Client

except ImportError:
    os.system("pip install pyrubi==3.3.1 ")

try:
    from requests import get,post
            
    import requests
except ImportError:
    
    
    os.system("pip install  requests")  
try:     
    import khayyam
except ImportError:
    os.system("pip install khayyam")  


def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True
def get_bmi_category(bmi):
    if bmi < 18.5:
        return "کمبود وزن"
    elif 18.5 <= bmi < 25:
        return "طبیعی"
    elif 25 <= bmi < 30:
        return "اضافه وزن"
    else:
        return "چاقی"

  



 
def get_crypto_price(coin_id, currencies=['usd', 'eur', 'gbp']):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies={",".join(currencies)}'
    response = requests.get(url)
    data = response.json()
    if coin_id in data:
        return {currency: data[coin_id][currency] for currency in currencies}
    else:
        return None

def main():
    coin_id = 'bitcoin'
    currencies = ['usd', 'eur', 'gbp']
    prices = get_crypto_price(coin_id, currencies)
    if prices:
        for currency, price in prices.items():
            return f"قیمت فعلی {coin_id.capitalize()} برابر است با {price} {currency.upper()}"
            
    else:
        return "Couldn't retrieve the price."
client = Client(session="MirBit")



list_command =(
            "سلام ربات هوش مصنوعی فعال شد وکار های که میتونه انجام بده به شرح زیر است:\n"
            "command:برای چت با هوش مصنوعی از این علامت استفاده کنید(*)\n"
            "command: برای تبدیل متن به ویس از این علامت استفاده کنید(voice)\n"
            "command:برای ارسال تصویر از هوش مصنوعی از این علامت استفاده کنید(تصویر)\n"
            "command:فال\n"
            "command:fal\n"
            "command:دانستنی\n"
            "command:/help\n"
            "command:/start\n"
            "command:دستورات\n"
            "command :راهنما\n"
            "command :time\n"
            "command :name,نام\n"
            "command :سلام\n"
            "command :prof\n"
            "command :بیوگرافی,بیو\n"
            "command :تایم\n"
            "command :زمان\n"
            "command :برای استفاده از بخش دوم هوش مصوعی  از ای علامت استفاده کید:/\n"
            "command :بات,ربات\n"
            "command :jok,جوک\n"
            "command:چت با چت جی پی تی  نسخه4 از علامت تعجب قبل از سوال خود بزارید\n"
            "command :fact,فکت\n"
            "command :برای اینکه لگو بده اول logo بعد متن خود\n"
            "command :برای چت با هوش مصنوعی بی رحم قبل هر متنی اینو qبزارید\n"
            "command :برای به دست اوردن  اینکه چقدر وزن ایده ال دارید اینطوری استفاده کنید به شرح زیر\n"
            "bmi:w190,h80\n"
            "command :برای اینکه عدد اول مشخص بشه اینطوری استفاده کنید به شرح زیر است:\n"
            "num:2\n"
            "command:faz,فاز\n"
            "command:انگیزشی\n"
            "command:دقت\n"
            "command:کتاب\n"
            "command :قیمت ارز,ارز\n"
            "command :برای ارسال عکس از هوش مصنوعی نسخه جدید قبل هر سوالی این را بنویسیدimage\n")


            
       
def get_images(text):
    response = requests.get(f'https://pyrubi.b80.xyz/img.php?text={text}&v=3.5')
    if response.status_code == 200:
        data = response.json()
        return data.get('result', [])
    else:
        return []                                   
                                    
for message in client.on_message():
    
  
            
               

    
    
    
    
   
        
        
        
    guid = message.object_guid
    msg = message.reply_message_id
    message_id=message.message_id
    
    if message.text =="دستورات":
        
        client.send_text(guid,"منتظربمانید",message_id=message_id)
        
        
       
       
       
          
        
          
          
        client.send_text(guid,list_command,message_id=message_id)

    elif message.text =="راهنما":
        
        client.send_text(guid,"منتظربمانید",message_id=message_id)
        client.send_text(guid,list_command)
    elif message.text =="/help":
        client.send_text(guid,"منتظربمایند",message_id=message_id)
        
        client.send_text(guid,list_command,message_id=message_id)
        
    elif message.text =="/start":
        
        client.send_text(guid,"منتظربمانید",message_id=message_id)
        
        client.send_text(guid,list_command,message_id=message_id)
    
    elif message.text =="تاریخ":
        
        client.send_text(guid,"منتظربمانید",message_id=message_id)
        tariq =khayyam.JalaliDatetime.today().strftime("%A %D %B %Y")
        client.send_text(guid,f"**{tariq }**",message_id=message_id)
    
    elif message.text =="کمک":
        client.send_text(guid,"منتظربمانید",message_id=message_id)
        client.send_text(guid,list_command,message_id=message_id)
    
    
    elif  message.text=="time":
        client.send_text(guid,"منتظربمانید",message_id=message_id)
        current_time = time.strftime("%H:%M:%S")
        client.send_text(guid,f"**{current_time }**",message_id=message_id)
    
    elif message.text.startswith("تصویر"):
        
        client.send_text(guid,"منتظربمانید در حال ساخت تصویر هستم",message_id=message_id)
        
        time.sleep(4)
        try:
            image =message.text.replace("تصویر","")
            
            client.send_text(guid,"صبرکنید",message_id=message_id)
            response =requests.get(f"https://pyrubi.b80.xyz/image-creator.php?text={image}")
            response.raise_for_status()
            
            data = response.json()
            result = data["result"]
            first_link = result[0]
            
            response = requests.get(first_link, stream=True)
            response.raise_for_status()
            with open("downloaded_image.jpg", "wb") as out_file:
                client.send_text(guid,"بازم انتظار",message_id=message_id)
                shutil.copyfileobj(response.raw, out_file)
                client.send_image(object_guid=guid,file='downloaded_image.jpg',text="عکس شما اماده شد",message_id=message_id)
                
        except Exception as p:
            print(p)
    
    elif message.text.startswith("prof"):
        prof =message.text.replace("prof","")
        
        response =requests.get('https://pyrubi.b80.xyz/prof.php')
        response.raise_for_status()
        data = response.json()
        image_url = data["result"][0]
        response = requests.get(image_url, stream=True)
        response.raise_for_status() 
        try:
            client.send_text(guid,"صبرکنید",message_id=message_id)
            with open("prof.jpg", "wb") as out_file:
                
                shutil.copyfileobj(response.raw, out_file)
                client.send_image(object_guid=guid,file='prof.jpg',text="پروفایل شما اماده شد")
                
                time.sleep(3)
               
        except Exception as p:
            
            print(p) 
    
    elif message.text =="بیوگرافی" or message.text=="bio" or message.text=="بیو":
        client.send_text(guid,"صبر کن عزیزم",message_id=message_id)
        bio =requests.get("https://pyrubi.b80.xyz/bio.php").json()["result"]
        client.send_text(guid,bio,message_id=message_id)
    
    
    
        
    elif message.text =="fal" or message.text=="فال":
        client.send_text(guid,"منظربمانید",message_id=message_id)
        try:
            
            response = requests.get("https://pyrubi.b80.xyz/fal").json()
            link = response["result"]

            
            img_response = requests.get(link, stream=True)
            if img_response.status_code == 200:
                
                with open('image2.jpg', 'wb') as f:
                    
        
                    img_response.raw.decode_content = True
                    shutil.copyfileobj(img_response.raw, f)
                    client.send_image(object_guid=guid,file='image2.jpg',text="فال شما اماده شد")
                    
                time.sleep(3)
                
        except Exception as f:
            
            print(f)        
                
        
    elif message.text =="نام"  or message.text =="name":
        
        client.send_text(guid,"منظربمانید",message_id=message_id)
        
        
        name =requests.get("https://pyrubi.b80.xyz/name.php").json()["result"]
        client.send_text(guid,name,message_id=message_id) 
        

    
    
    elif message.text.startswith("voice"):
        voice =message.text.replace("voice","")
        time.sleep(4)
       
        client.send_text(guid,"**صبرکنید تا ویس بدم**",message_id=message_id)
        r=requests.get(f"https://pyrubi.b80.xyz/voice.php?text={voice}&mod=FaridNeural").json()["result"]
        try:
            time.sleep(4)
            with open('voice_bot.mp3',"wb") as f:
                client.send_text(guid,"**صبرکنید خداباصابران است**",message_id=message_id)
                f.write(base64.b64decode(r))
                threading.Thread(target=r, args=(client.send_voice(object_guid=guid,file='voice_bot.mp3',text="ویس شما اماده شد \n @python_code_1384",message_id=message_id)))
                 
                
                
        except Exception as pt:
            print(pt)
    
    elif message.text =="دانستنی":
        link_dns =requests.get("http://Pyrubi.b80.xyz/danes.php")  
        client.send_text(guid,"منتظربمانید",message_id=message_id)
        try:
            
            client.send_text(guid,link_dns.text,message_id=message_id)
        
        except Exception as dns:
            print(dns)
    
    
            
    elif message.text.startswith("-"):
        text_s=message.text.replace("-","")
        
        g =GoogleTranslator("fa","en").translate(text_s)
        
        client.send_text(guid,f"ترجمه شده به انگلیسی:{g}",message_id=message_id)
        
    
    
    elif message.text.startswith('*'):
        text_gpt =message.text.replace("*","")
        time.sleep(4)
        
        client.send_text(guid,"**منتظرپاسخ بمانید**",message_id=message_id)
        gpt3=get(f"https://pyrubi.b80.xyz/chat.php?text={text_gpt}").json()["result"]
        
        
        
       
        
        try:
            client.send_text(guid,f"**{gpt3} **",message_id=message_id)
        except Exception as g:
            
            client.send_text(guid,f"erorr:{g}",message_id=message_id)   
             
      
    
    elif message.text =="سلام"   : 
         
          client.send_text(guid,"منتظرپاسخ بمانید",message_id=message_id)
          client.send_text(guid,"علیک سلام من میربات هستم چطور میتونم به شما کمک کنم؟",message_id=message_id)
    
    elif message.text =="انگیزشی":
        client.send_text(guid,"منتظرپاسخ بمانید",message_id=message_id)
        try:
            angiz=requests.get("http://ehsancoder.b80.xyz/angizeshi").json()["text"]
            
            client.send_text(guid,angiz,message_id=message_id)
        except Exception as a:
            client.send_text(guid,f"erorr:{a}",message_id=message_id)
            
            
 
     
    
    
    elif message.text =="ربات" or message.text =="بات":
        
        list_bo =["سلام","جان چیکار داری","اماده دستور هستم","چی میخوای عشقم"]
        r=random.choice(list_bo)
        client.send_text(guid,r,message_id=message_id) 
        

    elif message.text =="jok" or message.text =="جوک":
        client.send_text(guid,"منتظرپاسخ بمانید",message_id=message_id)
        j=requests.get('http://ehsancoder.b80.xyz/JoK.php')
        try:
            client.send_text(guid,j.text,message_id=message_id)
        except Exception as jo:
            
            print(jo)
    
                
    elif message.text =="fact" or message.text =="فکت":
        client.send_text(guid,"منتظرپاسخ بمانید",message_id=message_id)
        fact =requests.get('http://ehsancoder.b80.xyz/facet.php')  
        try:  
            client.send_text(guid,fact.text,message_id=message_id)
        except Exception as jo:
            
            print(jo)  
    
    
        
               
        client.send_text(guid,"ok send")
    
    elif message.text=="جرعت وحقیقت"or message.text =="جرعت_حقیقت":  
        time.sleep(4)
        client.send_text(guid,"**منتظربمانید برای بازی**",message_id=message_id)
        j=requests.get('https://pyrubi.b80.xyz/GH.php').json()["result"]
        try: 
            time.sleep(2)
            client.send_text(guid,j,message_id=message_id)
            
        except Exception as j:
            print(j)
    
    elif message.text.startswith("logo"):
        user =message.text.replace("logo", "")
        response = requests.get(f"https://api3.haji-api.ir/majid/ai/ephoto/random?text={user}").json()
        client.send_text(guid,"منتظربمانید الان لگورا میسازم",message_id=message_id)
        if response.get("success", False):
            
            
            image_url = response["result"]
            
    
            image_response = requests.get(image_url)
            
            if image_response.status_code == 200:
                
                client.send_text(guid,"منتظربمانید الان  میدم",message_id=message_id)
                try:
                
                    with open("logo_bot.jpg", "wb") as lo:
                        client.send_text(guid,"خداوندباصابرا است",message_id=message_id)
                        lo.write(image_response.content)
                        client.send_image(guid,"logo_bot.jpg",message_id=message_id,text="لگوی شما اماده شد")
                except requests.exceptions.RequestException as e:
                    client.send_text(guid,f"An error occurred: {str(e)}",message_id=message_id)
    elif message.text.startswith("/"):
        
        inp=message.text.replace("/","")
        client.send_text(guid,"**منتظربمانید**",message_id=message_id)
        
        
        time.sleep(4)
        
        chat=requests.get(f"http://www.mahrez.iapp.ir/Gpt/?text={inp}").json()["message"]
        
        try:
            client.send_text(guid,chat,message_id=message_id)
        except Exception as l:
            client.send_text(guid,f"اشکال در سرور :{l}",message_id=message_id)  
    
    
    elif message.text =="bg" or message.text =="بگراند" :
       
        response =requests.get("https://pyrubi.b80.xyz/background.php")
        response.raise_for_status()
        data = response.json()
        result = data["result"]
        first_link = result[0]
        response = requests.get(first_link, stream=True)
        response.raise_for_status()
        client.send_text(guid,"متظربمانید لطفا",message_id=message_id)
        try:
            with open("bg.jpg", "wb") as out_file:
                client.send_text(guid,"**منتظربمانید دارم بگراند زیبا میسازم**",message_id=message_id)
                shutil.copyfileobj(response.raw, out_file)
                client.send_image(guid,"bg.jpg",message_id=message_id,text="بگراند شما")
        except Exception as gb:
                client.send_text(guid,f"erorr**{gb}*",message_id=message_id)
    
    elif message.text.startswith("عکس"):
        
        ack = message.text.replace("عکس", "")
        client.send_text(guid, "متظربمانید لطفا", message_id=message_id)
        ac = requests.get(f"http://mahrez.iapp.ir/santcoin/image_creator.php?text={ack}")
        ac.raise_for_status()
        data_ = ac.json()
        result_ = data_[0]["image"]
        first_link_ = result_
        ac_image = requests.get(first_link_, stream=True)
        ac_image.raise_for_status()
    
        try:
            with open("downloaded_image_aret.jpg", "wb") as ut_file:
                client.send_text(guid, "الان ارسال میشه", message_id=message_id)
                shutil.copyfileobj(ac_image.raw, ut_file)
                client.send_image(guid, "downloaded_image_aret.jpg", message_id=message_id, text="بفرما عکس")
        except Exception as acc:
            client.send_text(guid, f"error {acc}", message_id=message_id)

   

    
    
    
    elif message.text.startswith("bmi:") and ',h' in message.text:
        text =message.text.replace("bmi:","")
        client.send_text(guid,"متظربمانید",message_id=message_id)
        if ',h' in text:
            try:
                weight, height = list(map(float, text.split('w')[1].split(',h')[0])), float(text.split(',h')[1])
                weight = weight[0]  # چون map به لیست تبدیل شده است، باید مقدار مورد نیاز را استخراج کنیم
                bmi = weight / ((height / 100) ** 2)
                bmi_category = get_bmi_category(bmi)
                client.send_text(guid, f"BMI شما: {bmi:.2f}\nدر دسته‌بندی BMI: {bmi_category}",message_id=message_id)
            except Exception as b:
                client.send_text(guid, f"erorr {b}",message_id=message_id)
    
    
    elif message.text.startswith("num:"):
        number_str = message.text.replace('num:', '')  
        try:
            number = int(number_str)   
            if is_prime(number):
                client.send_text(guid,f"عدد {number} یک عدد اول است.",message_id=message_id)
                client.reaction_message(guid,message_id,2)
            else:
                client.reaction_message(guid,message_id,3)
                client.send_text(guid,f"عدد {number} یک عدد اول نیست.",message_id=message_id)
            
        except ValueError:
            client.send_text(guid,"ورودی نامعتبر است. لطفاً یک عدد صحیح وارد کنید.",message_id=message_id)
  
    
    
    
    elif message.text.startswith("سوال"):
        sa=message.text.replace("سوال","")
        time.sleep(3)
        
        client.send_text(guid,"**منتظربمانید**",message_id)
        gpt_4 =requests.get(f"https://chat-gpt.chbk.run/gpt-3.5?text=hi{sa}").json()["result"]
        
        try:
            client.reaction_message(guid,message_id=message_id,reaction=1)
            
            client.send_text(guid,gpt_4,message_id)
        except Exception as gpt_44:
            client.send_text(guid,f"erorr {gpt_44}",message_id)
    
    
    
    elif message.text=="فاز" or message.text=="faz":
        client.send_text(guid,"**منتظربمانید**",message_id)
        faz =requests.get("http://ehsancoder.b80.xyz/faz.php") 
        try:
            client.send_text(guid,faz.text,message_id=message_id)
        except Exception as faz:
            
             client.send_text(guid,f"erorr{faz}",message_id=message_id)
    
    
    elif message.text =="deqat" or message.text =="دقت":
        client.send_text(guid,"**منتظربمانید**",message_id)
        deq=requests.get("http://ehsancoder.b80.xyz/degat.php") 
        try:
            client.send_text(guid,deq.text,message_id=message_id)   
        except Exception as deq:
            client.send_text(guid,deq.text,message_id=message_id) 
            
    elif message.text.startswith("بازی"):
        client.send_text(guid,"**منتظربمانید**",message_id)
        g =message.text.replace("بازی","")
        game =requests.get(f"http://ehsancoder.b80.xyz/game.php/?game={g}")   
        try:
            client.send_text(guid,game.text,message_id=message_id) 
        except Exception as game:
            client.send_text(guid,f"eror :{game}",message_id=message_id) 
    
    elif message.text =="کتاب":
        client.send_text(guid,"**منتظربمانید**",message_id)
        ket =get("http://ehsancoder.b80.xyz/ketab.php")
        try:
            client.send_text(guid,ket.text,message_id=message_id) 
        except Exception as k:
            client.send_text(guid,f"erorr{k}",message_id=message_id)   
    elif message.text.startswith("نگا"):
        gpt3=message.text.replace("نگا","")
        client.send_text(guid,"**منتظربمانید**",message_id)
        
        gpe3=get(f"http://ehsancoder.b80.xyz/chatGpt.php/?text={gpt3}").json()["message"]
        try:
            client.send_text(guid,f"**{gpe3}**",message_id)
        except Exception as g:
            client.send_text(guid,f"**erorr:{g}**",message_id)
   
    elif message.text=="ارز" or message.text=="قیمت ارز":
        client.send_text(guid,"**منتظربمانید**",message_id)
        m=main()
        client.send_text(guid,f"**{m}**",message_id)
     
    
   
    
    elif message.text.startswith("ip:"):
        url=message.text.replace("ip:","")
        get_ip=socket.gethostbyname(url)
        
        try:
            client.send_text(guid,f"**{get_ip}**",message_id)
        except Exception as ip:
            client.send_text(guid,f"**erorr :{ip}**",message_id) 
    
    elif message.text.startswith("image"):
        
        i = message.text.replace("image", "")
        client.send_text(guid, "**منتظر بمانید الان لینک عکس ارسال میشه**", message_id)
        images = get_images(i)
        

        if images:
            
            
            
        # انتخاب یک لینک به صورت تصادفی
            selected_image = random.choice(images)
            client.send_text(guid, f"بفرماید اینم از لینک عکس شما که ساخته شد برید نگاکنید\n {selected_image}" , message_id)
        else:
            client.send_text(guid, "پیدانشد ", message_id)
                
       
    
        
        client.send_text(guid,f"**ارسال لینک ممنوع است**", message_id)
    
    elif message.text=="شعر" or message.text=="شاعر":
        client.send_text(guid,f"**ای کاربر عزیر منتظربمان**", message_id)
        
        sh=get("http://ehsancoder.b80.xyz/shear").json()["text"]
        
        try:
            
            client.send_text(guid,f"**{sh}**", message_id)
        except Exception as s:
            
             
            client.send_text(guid,f"**{s}**", message_id)
    
    elif message.text.startswith("موزیک"):
        m= message.text.replace("موزیک","")
        client.send_text(guid,f"**الان لینک دانلود را میدم**", message_id)
        response = requests.get(f'http://song-search.chbk.run/song-title?song={m}').json()
        
        client.send_text(guid,f"{response['url']}", message_id)
                   
    elif message.text.startswith("لغت"):
        lo=message.text.replace("لغت","")
        client.send_text(guid,"منتظربمانید", message_id)
        
        l=get(f"http://ehsancoder.b80.xyz/word.php/?text={lo}").json()["Results"] 
        client.send_text(guid,f"{l}", message_id)  
    
    
  
    
    
      

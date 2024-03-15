#کتاب خانه های نیاز برای اجرا:rubpy,requests,aiortc

from os import system
import time
import base64
import random
import shutil
import asyncio
from re import search
import datetime
from random import randint
from urllib.parse import quote
import threading
from datetime import datetime
import urllib.request

try :
    from deep_translator import GoogleTranslator
except ImportError :
    system("pip install deep_translator")    
    
try:
    from rubpy import Client, filters, utils,enums,exceptions
    from rubpy.types import Updates
except ImportError :
    system("pip install rubpy ")

try:      
    import requests
except ImportError :
    system("pip install requests ")
try:
    import khayyam       
except ImportError:
    system("pip install khayyam")    
s =requests.Session()
# https://api-free.ir/api/voice.php?text=%D8%B3%D9%84%D8%A7%D9%85&mod=DilaraNeural
bot = Client(name='bot',display_welcome=False,parse_mode=enums.ParseMode.MARKDOWN)

def gpt_4(text):
    chat=s.get(f"http://www.mahrez.iapp.ir/Gpt/?text={text}").json()["message"]
    return f"پاسخ شما :\n{chat}"

def gpt3_(text):
    gpt =requests.get(f"https://api4.haji-api.ir/api/ai/ChatGPT/3/?text={text}").json()["result"]
    return f"پاسخ :\n{gpt}"

def get_images(text):
    response = requests.get(f'http://api-free.ir/api/img.php?text={text}&v=3.5')
    if response.status_code == 200:
        data = response.json()
        return data.get('result', [])
    else:
        return []   
        

def handle_text(l):
    
    response = requests.get(f'https://api-free.ir/api/Logo-top.php?text={l}&page=12')
    
    # بررسی موفقیت دریافت درخواست
    if response.status_code == 200:
        result = response.json()["result"]
        random_link = random.choice(result)
        return random_link
       
        # چاپ لینک‌های تصاویر
def get_joke(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None        
           
def get_random_music_link():
    api_url = "https://api-free.ir/api/music/"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        if data.get("ok") and data.get("result") and data["result"].get("song"):
            return data["result"]["song"]
    return None

def download_and_save_music(file_path, music_link):
    response = requests.get(music_link)
    if response.status_code == 200:
        with open(file_path, "wb") as file:
            file.write(response.content)
       
def show_time():
    # گرفتن تایم فعلی
    current_time = datetime.now().strftime("%H:%M:%S")
    # نمایش تایم به کاربر
    bot.send_message(f"Current Time: {current_time}")
    # ایجاد یک تایمر برای اجرای متد show_time هر یک ثانیه
    threading.Timer(1, show_time).start()

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

  







# مثال استفاده:

def send_current_date():
    tariq = khayyam.JalaliDatetime.today().strftime("%A %D %B %Y")
    return f"تاریخ فعلی: {tariq}"
def gpt_3_4(text):
    url = f'http://mahrez.iapp.ir/gpt3-4.php?text={text}'
    r = requests.get(url)
    response = r.json()

    # جواب‌های مختلف GPT ها را در یک لیست ذخیره می‌کنیم
    answers = [response["gpt3"], response["gpt4"]]

    # یکی از جواب‌ها را به صورت تصادفی انتخاب می‌کنیم
    selected_answer = random.choice(answers)
    return f"جواب شما :\n{selected_answer}"
  
#     filters.is_private  filters.is_group
@bot.on_message_updates()
async def updates(update: Updates):
    guid = update.object_guid
    msg = update.reply_message_id
    message_id=update.message_id
    
   


# تعریف وظیفه برای ارسال تاریخ فعلی یکبار در روز ساعت 6 صبح
  
    
    
    
#   "user_guid"
    text =update.text
    if text =="/start" or text =="/help" or text =="دستورات":
        await update.reply("**منتظرپاسخ بمانید**")
        list_command = (
            "📜لیست دستورات :\n"
            "command 1: /start\n"
            "command 2: /help\n"
            "command 3: /time\n"
            "command 4: برای چت با چت جی بی تی چهار قبل هر متن + بزارید\n"
            "command 5: برای چت با بخش چت جی بی تی 3.5 قبل هر متنی * بزارید\n"
            "command 6: برای بخش تصویر هوش مصنوعی قبل هر متنی image بنویسید\n"
            "command 7: تاریخ\n"
            "command 8: برای ویس دادن ربات قبل هر متن ویس بنویسید\n"
            "command 9: اگر میخواید ربات درویسکال ویس بده قبل هر متن شروع بنویسید\n"
            "command 10: برای پخش موزیک درویسکال قبل هر متنی موزیک بنویسید\n"
            "command 11: جوک\n"
            "command 12: jok\n"
            "command 13: fact\n"
            "command 14: فکت\n"
            "command 16: برای پخش رندوم آهنگ درویسکال بنویسید اهنگ\n"
            "command 17: bio\n"
            "command 18: بیو\n"
            "command 19: برای ویس دادن مرد قبل هر متنی voice بنویسید\n"
            "command 20: برای چت با بخش هوش مصنوعی لاما از این / قبل هر متن استفاده کید\n"
            "command 21: برای ارسال عکس به صورت فایلی قبل هر متنی بنویسید عکس\n"
            "command 22:برای ارسال نام راندم بنویسید نام\n"
            "command 23:برای تشخیص توده بدنی اینگونه برای ربات بنویسید\n"
            "bmi:w60,h185\n"
            "command 24:شعر\n"
            "command 25:برای فونت انگلیسی قبل هرمتنی کلمه fontبنویسید\n"
            "command 26: :برای ارسال پیام از اکانت ربات به مالک که یک نوع پیام ناشناس هم حساب میشه میتونید قبل هر پیام خود اینوگونه بنویسید\n"
         
            
            
            
    )

    
        await update.reply(list_command)
        
        
                           
        
        
        
        
        
    
    elif text.startswith("+"):
        try:
            await update.reply("**منتظرپاسخ بمانید**")
            gpt4=update.text.replace("+","")
            try:
                g=gpt_4(gpt4)
                await update.reply(g)
            except Exception as g:
                await update.reply(f"erorr:\n{g}")
        except exceptions.InvalidMethod as me:
            await update.reply(f"erorr :\n{me}")
    elif text.startswith("*"):
        await update.reply("**منتظرپاسخ بمانید**")
        gpt3=update.text.replace("*","")
        try:
            g=gpt3_(gpt3)
            
            await update.reply(g)
            
            
        except Exception as gb:
            await update.reply(f"erorr:\n{gb}")

   
    elif text.startswith("ویس"):
        
        await update.reply("**منتظر پاسخ بمانید**")
        voice = update.text.replace("ویس", "")
        
    
        try:
            
            response = requests.get(f"https://api-free.ir/api/voice.php?text={voice}&mod=DilaraNeural")
            response.raise_for_status()  # بررسی موفقیت درخواست
            
            result_url = response.json()["result"]
            
            await asyncio.sleep(3)
            await update.reply("الان میدم خدمت شما")
            
            voice_response = requests.get(result_url)
            
            voice_response.raise_for_status()
            # بررسی موفقیت درخواست
            
            with open('voice_bot.mp3', "wb") as f:
                
                f.write(voice_response.content)
                
                
                await bot.send_voice(guid, 'voice_bot.mp3', caption="ویس شما آماده است", reply_to_message_id=message_id)
        except Exception as v:
            await update.reply(f"خطا:\n{v}")

    elif text.startswith("image"):
        i = update.text.replace("image", "")
        await update.reply("منتظرلینک عکس باشید")
        images = get_images(i)
        if images:
            selected_image = random.choice(images)
            await update.reply(f"لینک عکس شما اماده شدمیتونید واردلینک وعکس خودراببینید\n{selected_image}")

    elif text.startswith("شروع"):
        await update.reply("**منتظرپاسخ بمانید**")
        
        v_c=update.text.replace("شروع","")
        time.sleep(2)
        
        try:
            response = requests.get(f"https://api-free.ir/api/voice.php?text={v_c}&mod=DilaraNeural")
            response.raise_for_status() 
            result_url = response.json()["result"]
            await asyncio.sleep(3)
            await update.reply("الان درویسکال جواب میدم")
            voice_response = requests.get(result_url)
            
            voice_response.raise_for_status()
            with open('voice_bot.mp3', "wb") as f:
                
                
                f.write(voice_response.content)
                await bot.voice_chat_player(guid,'voice_bot.mp3')
                
            
            
        except Exception as vc:
                await update.reply(f"erorr:\n{vc}")
   

    elif text.startswith("موزیک"):
        m=update.text.replace('موزیک',"")
        await update.reply("**منظربمانید وبه زودی اهنگ درویسکال اجرامیشه**")
        url = f"https://api-free.ir/api/sr-music/?text={m}"
        response = requests.get(url)  
        if response.status_code == 200:
            
            data = response.json()
            song_url = data["result"]["song"]
            
            # دانلود فایل صوتی
            urllib.request.urlretrieve(song_url, "music_plyar.mp3")
            with open("music_plyar.mp3","rb") as m:
                
                await bot.voice_chat_player(guid,"music_plyar.mp3")
                m.close()
            
            
         
       
        
    elif text =="time":
        await update.reply("time......")
        current_time = time.strftime("%H:%M:%S")
        now = datetime.now()
        a=now.strftime("%H:%M:%S")
        m=now.strftime("%Y-%m-%d")
        await update.reply(f"زمان:\n{a} \n تاریخ:\n{m} \n فعلی:\n {current_time}")
    elif text =="تاریخ" or text =="data":
        await update.reply("منتظربمانید")
        tariq =khayyam.JalaliDatetime.today().strftime("%A %D %B %Y")
        await update.reply(tariq)
    elif text =="انگیزشی":
        await update.reply("منتظربمانید")
        angiz=requests.get("http://ehsancoder.b80.xyz/angizeshi").json()["text"]
        try:
            await update.reply(angiz)
        except Exception as an:
            await update.reply(f"erorr\n {an}")
    elif text =="jok" or text =="جوک":
        await update.reply("منتظربمانید")
        links = requests.get("https://api-free.ir/api/jok.php").json()["result"]
        
        
        
        try:
            await update.reply(links)
            
        except Exception as jo:
            await update.reply(f"erorr\n {jo}")
    elif text =="fact" or text == "فکت":
        fact =requests.get('http://ehsancoder.b80.xyz/facet.php')  
        try:
            await update.reply(fact.text)
        except Exception as f:
                await update.reply(f"erorr\n {f}")

    elif text =="bot" or text =="ربات" or text =="بات" or text =="میربات":
        list_bot =[
            "جان ربات",
            "بله بفرماید",
            "اماده دستورم",
            "اماده برای فرمان شما",
            "hello👋", 
            "چی میخای ",
            "بنال",
            "جون توفقط  دستور بده"
            
        ]
        r=random.choice(list_bot)
        await update.reply(r)
    elif text =="اهنگ" or text=="music":
        await update.reply("منتظردانلوداهنگ وپخش درویسکال باشید")
        random_music_link = get_random_music_link()
        try:
            if random_music_link:
            
                await update.reply(f"لینک دانلود موزیک تصادفی: \n{random_music_link}")
                music_file_name = "random_music.mp3"
                download_and_save_music(music_file_name, random_music_link)
                with open(music_file_name, 'rb') as music_file:
                    await bot.voice_chat_player(guid,'random_music.mp3')
        except Exception as h:
              await update.reply(f"erorr\n{h}")
              
    elif text =="bio" or text =="بیو" :
        await update.reply("منتظربمانید")
        bi=s.get("http://ehsancoder.b80.xyz/bio.php")
        try:
            await update.reply(bi.text)
              
        except Exception as b:
            
            await update.reply(f"erorr :\n{b}")
    
    elif text.startswith("voice"):
        await update.reply("**منتظر پاسخ بمانید**")
        voice = update.text.replace("voice", "")
        try:
            response = requests.get(f"https://api-free.ir/api/voice.php?text={voice}&mod=FaridNeural")
            response.raise_for_status() 
            result_url = response.json()["result"]
            await asyncio.sleep(3)
            await update.reply("الان میدم خدمت شما")
            voice_response = requests.get(result_url)
            voice_response.raise_for_status()
            with open('voice_bot_man.ogg', "wb") as f:
                f.write(voice_response.content)
                await bot.send_voice(guid, 'voice_bot_man.ogg', caption="ویس شما آماده است", reply_to_message_id=message_id)
        except Exception as vm:
            await update.reply(f"erorr :\n {vm}")
    elif text.startswith("مرد"):
        await update.reply("**منتظر پاسخ بمانید**")
        mard =update.text.replace("مرد", "")
        response = requests.get(f"https://api-free.ir/api/voice.php?text={mard}&mod=FaridNeural")
        response.raise_for_status() 
        result_url = response.json()["result"]
        await asyncio.sleep(3)
        await update.reply("الان میدم خدمت شما")
        voice_response = requests.get(result_url)
        voice_response.raise_for_status()
        try:
            with open('voice_bot_man.mp3', "wb") as f:
                f.write(voice_response.content)
                await bot.voice_chat_player(guid,'voice_bot_man.mp3')
        except Exception as m:
         
            await update.reply(f"erorr :\n {m}")

    elif text.startswith('/'):
        
        
        s=requests.session()
        
        await update.reply("**منتظر پاسخ بمانید**")
        t=update.text.replace('/','')
        
        l=s.get(f"http://api-free.ir/api/llama.php?text={t}").json()["result"]  
        english_text =l
        persian_text = GoogleTranslator(source='auto', target='fa').translate(english_text)
        
        try:
            
            
           await update.reply(f"پاسخ :\n{persian_text}")
        except Exception as lam:
            
            await update.reply(f"erorr::\n{lam}")
   
    elif text.startswith("عکس"):
        await update.reply("loading......")
        
        image = update.text.replace("عکس","")
        response = requests.get(f"http://api-free.ir/api/img.php?text={image}&v=3.5")
        response.raise_for_status()
            
        data = response.json()
        result = data["result"]
        
        # انتخاب یک عنصر تصادفی از لیست result
        random_link = random.choice(result)
        
        response = requests.get(random_link, stream=True)
        response.raise_for_status()
        try:
            with open("downloaded_image.jpg", "wb") as out_file:
                
                await update.reply("درحال ارسال")
                shutil.copyfileobj(response.raw, out_file)
                await update.reply_photo("downloaded_image.jpg",caption='عکس شما آماده شد')
        except Exception as ph:
            await update.reply(f"erorr\n{ph}")
    
    elif text =="شعر" or text =="شاعرانه":
        sh =requests.get("http://ehsancoder.b80.xyz/shear").json()["text"]
        try:
            await update.reply(sh)
        except Exception as s:
                await update.reply(f"erorr\n{s}")
    elif text.startswith("font"):
        await update.reply("درحال ساخت فونت")  
        a =update.text.replace("font","")
        fonts = requests.get(f'http://api-free.ir/api/font.php?en={a}').json()["result"]
        formatted_fonts = "\n".join([f"{index + 1}. {font}" for index, font in enumerate(fonts)])
        await update.reply(f"فونت‌های شما:\n{formatted_fonts}")
    
    elif  text =="name" or text =="نام":
        name =requests.get('https://api-free.ir/api/name.php').json()["result"]
        try:
            await update.reply(name)
        except Exception as n:
            await update.reply(f"erorr \n{n}")
  
    
   
    elif text =="❤️":
        await update.reply("چه قلب زیبایی همین تقدیم شما ❤️")   
    elif text.startswith("bmi:") and ',h' in text:  
        t=update.text.replace("bmi:","")
        await update.reply("درحال محاسبه")
        if ',h' in t:
            try:
                weight, height = list(map(float, text.split('w')[1].split(',h')[0])), float(text.split(',h')[1])
                weight = weight[0]  # چون map به لیست تبدیل شده است، باید مقدار مورد نیاز را استخراج کنیم
                bmi = weight / ((height / 100) ** 2)
                bmi_category = get_bmi_category(bmi)
                await update.reply(f"BMI شما: {bmi:.2f}\nدر دسته‌بندی BMI: {bmi_category}")
            except ValueError:
                await update.reply("مقادیر رادرست وارد کنید")
    elif text.startswith("رباتی"):
        g3g4 =update.text.replace("رباتی","")
        await update.reply("❤️منتظربمانید❤️")
        
        try:
            await  update.reply(gpt_3_4(g3g4))
        except Exception as g3g:
            
            await update.reply(f"erorr\n{g3g}")
       
            
bot.run()

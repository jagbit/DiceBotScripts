"""
    Ultimate.py
"""

# Imports
from browser import document, window
import math, random, sys, time

# Init Globals
bal = float(balance)
chance = 32
basebet = bal * 1000e-8
nextbet = basebet
losecount = 0
i = bal * 0.99
k = 0.0005
roll = 0
targetprofit = bal * 1.10
a = 0
bethigh = True
#resetseed() # Live play only

# Sleep function
def sleeper(n=0.2):
    max = n
    start = time.process_time()
    sentry = True
    while (sentry == True):
        remaining = max + start - time.process_time()
       # print("%s seconds remaining" % int(remaining))

        if remaining <= 0:
            break
            
def dobet(event):
  	# Init Globals
    # Game variables must always be called as global
    # any user variables initialized outside of 
    # dobet() must be declared global
    global chance,multiplier,bethigh,nextbet
    global previousbet,bets,wins,losses,profit,currentprofit,currentstreak,currentroll,balance,win
    global currency,currencies,lastBet
    global basebet,losecount,i,k,roll,a,resetseed,bal,targetprofit
    
    roll += 1
    
    if bal > targetprofit:
            stop()
            
    if a == 16:
        if bethigh == true:
            bethigh = False
        elif bethigh == false:
            bethigh = True
        a = 0
        
    if win == True:
        a += 1
        nextbet = basebet
        chance = 20
        losecount = 0
    elif win == False:
        nextbet = previousbet * 1.33
        losecount += 1
        
    if (losecount>=6):
        nextbet = previousbet*1.33
        chance = 6
        
    if (losecount>=10):
        nextbet = previousbet*1.33
        chance = 20
    
    if (losecount>=12):
        nextbet = previousbet*1.33
        chance = 15
    
    if (losecount>=16):
        nextbet = previousbet*1.55
        chance = 28
    
    if (losecount>14):
        nextbet = previousbet*1.88
        chance = 20
    
    if (losecount>17):
        nextbet = previousbet*2.075
        chance = 48
        
    if (losecount>18):
        nextbet = previousbet*2
    
    if (losecount>19):
        nextbet = previousbet*1.95
    
    sleeper()
    
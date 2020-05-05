import tweepy
import time


def getLastSeenId(fileName):
    f_r = open(fileName, 'r')
    lsID = int(f_r.read().strip())
    f_r.close()
    return lsID

def setLastSeenId(id, fileName):
    f_w = open(fileName, 'w')
    f_w.write(str(id))
    f_w.close()
    return


CONSUMER_KEY = 'UqfYkk074wKd9DSEFDA0JeBwZ'
CONSUMER_SECRET = 'WfMtfFD2VXaI8XDaRgSNYHUDh4V4MJ0KGTMb1TM7b6RpYXrTFm'
ACCESS_KEY = '1256980054141284356-KOHIO95m9HSszgum6GsOWlYpaxRdO3'
ACCESS_SECRET = 'eflMco61feb46oh4bHC78AfXzwaMSSkMTfN2gBGv3SVjh'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#lastSeenId = 1257300822095990786

FILENAME_lsID = 'last_seen_id.txt'
SCREEN_NAME = '@CaroKann20'


run = True


#home = api.home_timeline()

"""
if str(m.text).__contains__('?'):
    print(str(m.id) + ': ' + m.text)
   # api.update_status("Listen up @%s" % m.author.screen_name, m.id)
if m.text.__contains__('hello bot'):
    print(str(m.id) + ': ' + m.text)
    #api.update_status("sup @%s" % m.author.screen_name, m.id)
"""

"""
print("home")
for m in home:
    print(str(m.id) + ': ' + m.text)"""
i = 0
while run:
    lastSeenId = getLastSeenId(FILENAME_lsID)
    mentions = api.mentions_timeline(lastSeenId)
    if len(mentions) > 0:
        setLastSeenId(mentions[0].id,FILENAME_lsID)
        for m in mentions:
            print('iteration ' + str(i) + ' - ' + str(m.id) + ': ' + m.text)
            api.update_status("wdym " + "%s @%s" % (m.text.replace(SCREEN_NAME, ''), m.author.screen_name), m.id)
    f_cont = open('controller.txt', 'r')
    content = f_cont.read()
    if 'running' not in content:
        run = False
    f_cont.close()
    time.sleep(5)
    i += 1

print("program finished, last seen: " + str(getLastSeenId(FILENAME_lsID)))





















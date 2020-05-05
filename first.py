import tweepy
import time
CONSUMER_KEY = 'UqfYkk074wKd9DSEFDA0JeBwZ'
CONSUMER_SECRET = 'WfMtfFD2VXaI8XDaRgSNYHUDh4V4MJ0KGTMb1TM7b6RpYXrTFm'
ACCESS_KEY = '1256980054141284356-KOHIO95m9HSszgum6GsOWlYpaxRdO3'
ACCESS_SECRET = 'eflMco61feb46oh4bHC78AfXzwaMSSkMTfN2gBGv3SVjh'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

lastSeenId = 1257300822095990786



run  = True
f = open('controller.txt', 'r')

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
    mentions = api.mentions_timeline(lastSeenId)
    if len(mentions) > 0:
        lastSeenId = mentions[0].id
    for m in mentions:
        print('iteration ' + str(i) + ' - ' + str(m.id) + ': ' + m.text)
        api.update_status("wdym " + "%s  @%s" % (m.text, m.author.screen_name), m.id)
    if f.mode == 'r':
        content = f.read()
        if not content.__contains__('running'):
            run = False
    i += 1
    time.sleep(5)

print("program finished, last seen: " + str(lastSeenId))

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time


ckey = 'HsB6ogDWH9crNKB5XQmxsQ'
csecret = 'Jxky6riYtjxeZDMR2MTu4Lc2X1GOSuNpnJu71IPHs8'
atoken = '75264459-YHx2kl72929vNWQ9RqhPpRGC7v6KoUwTmvQi4RK4x'
asecret = 'Seq18PwFsdijpbkYEAsC1smzyszLAie8mHCxih04W2FmR'

class listener(StreamListener):

    def on_data(self, data):
        try:
            #print data

            
            saveFile = open('OscarTrial327.json', 'a') 
            saveFile.write(data)
            #saveFile.write('\n')
            saveFile.close()
            return True
        except BaseException, e:
            print 'failed ondata,',str(e)
            time.sleep(5)

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["#oscarpistorius","#oscartrial","pistorius","steenkamp","reeva"])


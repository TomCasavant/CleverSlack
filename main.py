from slackclient import SlackClient
from cleverwrap import CleverWrap
import os
import time
from ConfigParser import SafeConfigParser



def main():
	if sc.rtm_connect():
		#sc.rtm_send_message("clever", "Bot starting up...")
		while True:
			for slack_message in sc.rtm_read():
				message = slack_message.get("text")
				user = slack_message.get("user")
				if not message or not user or user == "cleverbot":
					continue
				#print "Got message! %s" %(message)
				sc.rtm_send_message("#clever", "{text}".format(text=cleverbot(message)))

			time.sleep(1)

		else:
			print "Connection failed"

def cleverbot(text):
	response = cw.say(text)
	return response

if __name__ == "__main__":
	parser = SafeConfigParser()
	parser.read("config.ini")
	SLACK_API_TOKEN = parser.get("slack", "API_TOKEN")
	CLEVERBOT_API_TOKEN = parser.get("cleverbot","API_TOKEN")
	sc = SlackClient(SLACK_API_TOKEN)
	cw = CleverWrap(CLEVERBOT_API_TOKEN)
	main()

import fbchat
import random
import time
# import credentials


client = fbchat.Client("USER NAME", "PASSWORD")
greetings = ["Hey", "Hey how's it goin", "Sup", "yo"]
#names = ["Will", "Mr. Hodges", "Willy", "buddy", "man"]
names = ["Todd", "Mr. Schmid", "Ted", "buddy", "man"]

replies = ["I understand", "Hmmm interesting",  "Tell me more", "You're right.", "I see", "Wow that's great"]
questionReplies = ["Hmmm... What do you think", "I don't know", "Probably"]
lolReplies = ["lol", "haha", "oh wow lol"]
Friends = client.getUsers("Poe Phox")

def isLink(str):
    return "http" in str

def isQuestion(str):
    return "?" in str

def isBotCatch(str):
    return "bot" in str

def isJoke(str):
    return (("haha" in str) or ("lol" in str))

# print(Friends)
Friend = Friends[0]
greeting = random.choice(greetings)
name = random.choice(names)
# print (greeting)


sent = client.send(Friend.uid, greeting + " " + name)
if sent:
    print("Sent: ", greeting + " " + name)

time.sleep(2)

last_messages = client.getThreadInfo(Friend.uid,0)  
while True:
    if(last_messages[0].author != ("fbid:" + str(client.uid))):
        name = random.choice(names)  
        response = last_messages[0].body
        print("Got: ", response)
        if isLink(response):
            reply = "let me check that out..."
            sent = client.send(Friend.uid, reply)        
            if sent:
                print("Sent: ", reply)
            time.sleep(random.randint(10,30))
            reply = "Wow interesting!" + "Thanks " + name +"!"
        elif isQuestion(response):
            reply = random.choice(questionReplies)
        elif isJoke(response):
            reply = random.choice(lolReplies)
        elif isBotCatch(response):     
            reply = "Sorry I need to go now."
            sent = client.send(Friend.uid, reply)        
            exit()
        else:      
            reply = random.choice(replies)    
            time.sleep(random.randint(3,10))

        time.sleep(random.randint(3,10))
        sent = client.send(Friend.uid, reply)

        if sent:
            print("Sent: ", reply)
        
    time.sleep(1)
    last_messages = client.getThreadInfo(Friend.uid,0)    
    
# for message in last_messages:
#     print(message.body)

# sent = client.send(Friend.uid, greeting)
# if sent:
#     print("Message sent successfully!")

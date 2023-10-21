# Asymetric encryption with python
# - public key encrypts the message
# - private key decrypts the message

import rsa
from dataclasses import dataclass
import datetime
import time

@dataclass
class EncyptionKeys:
  publicKey:bytes
  privateKey:bytes

publicKey,privateKey = rsa.newkeys(512)
message = "vwalaaa"

keys = {
  "publicKey":publicKey,
  "privateKey":privateKey
}
parsedKeys = EncyptionKeys(**keys)


def EncryptData(message:str):
  return rsa.encrypt(message.encode(),parsedKeys.publicKey)

def DecryptData(message:str):
  return rsa.decrypt(message,privateKey).decode()

class Message:
  def __init__(self,sender,recepient,content=""):
    self.sender = sender
    self.recepient = recepient
    self.is_read = False 
    self.sent_at = datetime.datetime.now()
    self.recieved()
    self.content(content=content)
  
  def content(self,content):
    self.__message = EncryptData(content)

  def recieved(self):
    self.recieved_at = datetime.datetime.now()
    self.is_read = True

  @property
  def read(self):
    return DecryptData(self.__message)
    
  def __str__(self):
    return f"This is a message from {self.sender} to {self.recepient}"

    
class User:
  def __init__(self,username,contact,inbox=[]):
    self.username = username
    self.contact = contact
    self.Inbox(inbox=inbox)

  def Inbox(self,inbox):
    self.__inbox = inbox
  
  def AddMessage(self,message):
    return self.__inbox.append(message)
  
  def CheckInbox(self):
    return self.__inbox
  
  def ViewMessage(self,sender):
    for message in self.__inbox:
      if message.sender == sender:
        message.recieved()
        time.sleep(60)
        print(message.read,f"@{message.sent_at}") 
      else:
        print("no messages from",sender)


print("You are logged in as leaky")
sender = "leaky"
content = str(input("Enter message: "))
user = User("kefason","0793031904")
recipient = input("Send to: ")
incommingMessage = Message(sender,recepient=recipient,content=content)
if(user.username == incommingMessage.recepient):
  user.AddMessage(incommingMessage)

messages = user.CheckInbox()
total_messages = 0
user.ViewMessage("leaky")
for message in messages:
  if message.is_read:
    continue
  total_messages+=1


print("Total messages",total_messages)
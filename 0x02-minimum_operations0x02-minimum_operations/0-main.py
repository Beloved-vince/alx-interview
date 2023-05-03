# #!/usr/bin/python3
# """
# Main file for testing
# """

# minOperations = __import__('0-minoperations').minOperations

# n = 4
# print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

# n = 12
# print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))


from gtts import gTTS
  
# This module is imported so that we can 
# play the converted audio
import os
  
# The text that you want to convert to audio
mytext = 'Welcome to geeksforgeeks!'
  
# Language in which you want to convert
language = 'en'
  
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("welcome.mp3")
  
# Playing the converted file
os.system("mpg321welcome.mp3")
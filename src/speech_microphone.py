#!/usr/bin/env python
import rospy
import speech_recognition as sr
import subprocess, time 	

r = sr.Recognizer()
r.energy_threshold = 4000

class speech_microphone(object):
	def __init__(self):
		self.speech()
		
	def speech(self):	
	
		while not rospy.is_shutdown():

			with sr.Microphone() as source:
				print("Say something!")
				audio = r.listen(source)
				#r.adjust_for_ambient_noise(source, duration=2)
				print("Got it! Now to recognize it...")
				try:
				# for testing purposes, we're just using the default API key
				# to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
				# instead of `r.recognize_google(audio)`
					print(r.recognize_google(audio,language='zh-tw'))
				
				
				except sr.UnknownValueError:
					print("Google Speech Recognition could not understand audio")
				except sr.RequestError as e:
					print("Could not request results from Google Speech Recognition service; {0}".format(e))
			
			
if __name__ == "__main__":
	rospy.init_node("speech_microphone",anonymous=False)
	speech_microphone = Speech_microphone()
	rospy.spin()
	
'''
import speech_recognition as sr
import subprocess, time

r = sr.Recognizer()
m = sr.Microphone()

def say(text):
    return subprocess.call("espeak -s 155 -a 200 '" + text + "'", shell=True)

try:
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        print("Say something!")
        with m as source: audio = r.listen(source)
        print("Got it! Now to recognize it...")
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)

            # we need some special handling here to correctly print unicode characters to standard output
            if str is bytes: # this version of Python uses bytes for strings (Python 2)
                say(u"You said {}".format(value).encode("utf-8"))
            else: # this version of Python uses unicode for strings (Python 3+)
                say("You said {}".format(value))
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
        time.sleep(0.5) # sleep for a little bit
except KeyboardInterrupt:
    pass		
'''
		
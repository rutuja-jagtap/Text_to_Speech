import os
import time
import flask
import playsound
import speech_recognition as sr
from gtts import gTTS
# from flask import request 
from flask import Flask , render_template , request

#from datetime import datetime

app = Flask("Text to speech")
@app.route('/')
def home():
	return render_template('index.html')

#for speaking
@app.route("/process" , methods = ["POST"] )
def speak():
		text = request.form["z1"] 
		tts=gTTS(text=text) 		#transform into audio file
		filename="voice.mp3" 		#saves text in voice.mp3
		tts.save(filename)			#save file which contains text in this folder
		playsound.playsound(filename) 
		os.remove("voice.mp3")
		return render_template('index.html')
		
#speak("hello RJ")
# speak("Peter Piper picked a peck of pickled peppers; A peck of pickled peppers Peter Piper picked;If Peter Piper picked a peck of pickled peppers,Where’s the peck of pickled peppers Peter Piper picked")
app.run("localhost" , port=5000 )
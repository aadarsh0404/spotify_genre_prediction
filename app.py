from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        
        danceability = float(request.form['danceability'])
        if danceability<0.161:
            danceability=0.161
        elif danceability>1.13:
                danceability=1.13
                
        energy = float(request.form['energy'])
        if energy<0.1955:
            energy=0.1955
        elif energy>1.36:
                energy=1.36
                
        key = int(request.form['key'])
        if(key==0):
            key=3470
        elif(key==1):
            key=7537
        elif(key==2):
            key=3047
        elif(key==3):
            key=900
        elif(key==4):
            key=2368
        elif(key==5):
            key=2994
        elif(key==6):
            key=3417
        elif(key==7):
            key=4275
        elif(key==8):
            key=3345
        elif(key==9):
            key=3254
        elif(key==10):
            key=3251
        elif(key==11):
            key=4150
            
        loudness = float(request.form['loudness'])
        if loudness<-13.63:
            loudness=-13.63
        elif loudness>0.96:
            loudness=0.96
            
        speechiness = float(request.form['speechiness'])
        if speechiness<-0.167:
            speechiness=-0.167
        elif speechiness>0.41:
            speechiness=0.41
            
        acousticness= float(request.form['acousticness'])
        if acousticness<-0.15:
            acousticness=-0.15
        elif acousticness>0.265:
            acousticness=0.265
            
        instrumentalness = float(request.form['instrumentalness'])
        if instrumentalness<-1.1:
            instrumentalness=-1.1
        elif instrumentalness>1.805:
            instrumentalness=1.805
            
        liveness = float(request.form['liveness'])
        if liveness<-0.192:
            liveness=-0.192
        elif liveness>0.5855:
            liveness-0.5855
            
        valance = float(request.form['valance'])
        if valance<-0.38:
            valance=-0.38
        elif valance>1.063:
            valance=1.063
            
        tempo = float(request.form['tempo'])
        if tempo<82.63:
            tempo=82.63
        elif tempo>208.7:
            tempo=208.7
            
        duration_ms = int(request.form['duration_ms'])
        if duration_ms>483072:
            duration_ms=483072
            
        mode = int(request.form['mode'])
        time_signature = float(request.form['time_signature'])
        t3 = 0
        t4 = 0
        t5 = 0
        if time_signature==3:
            t3 = 1
        elif time_signature==4:
            t4 = 1
        elif time_signature==5:
            t5 = 1
        
        pred = model.predict([[danceability,energy,key,loudness,mode,speechiness,acousticness,instrumentalness,valance,tempo,duration_ms,mode,t3, t4, t5]])
        if pred==0:
            return render_template('index.html',prediction_texts="Dark Trap")
        elif pred==1:
            return render_template('index.html',prediction_texts="Underground Rap")
        elif pred==2:
            return render_template('index.html',prediction_texts="Trap Metal")
        elif pred==3:
            return render_template('index.html',prediction_texts="Emo")
        elif pred==4:
            return render_template('index.html',prediction_texts="Rap")
        elif pred==5:
            return render_template('index.html',prediction_texts="RnB")
        elif pred==6:
            return render_template('index.html',prediction_texts="Pop")
        elif pred==7:
            return render_template('index.html',prediction_texts="Hip Hop")
        elif pred==8:
            return render_template('index.html',prediction_texts="Technohouse")
        elif pred==9:
            return render_template('index.html',prediction_texts="Techno")
        elif pred==10:
            return render_template('index.html',prediction_texts="Tance")
        elif pred==11:
            return render_template('index.html',prediction_texts="Psytrance")
        elif pred==12:
            return render_template('index.html',prediction_texts="Trap")
        elif pred==13:
            return render_template('index.html',prediction_texts="DnB")
        elif pred==14:
            return render_template('index.html',prediction_texts="Hardstyle")
    else:
        return render_template('index.html')
    
if __name__=="__main__":
    app.run()
    
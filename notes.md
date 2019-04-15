### notes 

#### 2019-04-15 
* plan to talk with Dr. Lam 

#### 2019-04-12 
* coding the syn function

#### 2019-04-11 
* fix the file upload issue 
  - 
  
* [check Heroku App with Flask](http://clouddatafacts.com/heroku/heroku-flask/heroku_flask_getting_started.html)


#### 2019-04-09 
* 'Acoustic Phonetics' part on slp2 
* TODO 
  - fix the interface issues soon 

#### 2019-04-04 
* check the problems to deploy on heroku
  - [weblink](https://ispeech.herokuapp.com/ | https://git.heroku.com/ispeech.git)

#### 2019-04-03 
* try to use Heroku TO deploy the HTTPS 

#### 2019-04-02 
* check the code HTTPS connection 
* read a doc on phonetics from a computational perspective referenced on slp2 


#### 2019-03-27 
* todo
  - the principle of voice 

#### 2019-03-26

* present a simplified web demo 

* TODO 
  - HTTPS connection
    + [HTTPS and trust chain in Flask](https://carolinafernandez.github.io/development/2017/09/13/HTTPS-and-trust-chain-in-Flask)
  - socket issue 
    + flask socketio bp 
  - the realted resource  
    + check the realted principle and module 


#### 2019-03-24 
* progresss
  - capture audio using Recorderjs 
  

* TODO
  - use websocket for connection 
  - deploying a web app using Heroku and Flask 
  - <del>deploying a mobile app </del>

* reference
  - [Deploying Deep Learning Models On Web And Mobile](https://reshamas.github.io/deploying-deep-learning-models-on-web-and-mobile/)

#### 2019-03-21 
* work 
  - uses Recorderjs for audio capture 
  - a **WebSocket** connection to the Kaldi GStreamer server for speech recognition 

#### 2019-03-20 
* ASR 
  - A Speech-to-Text API synchronous recognition request
  - Streaming Recognition (gRPC only) using google cloud

#### 2019-03-19 
* ASR in ELT 
  - pronunciation 
    + compare student voice recordings 
    + work on phonology and accent 
  - Interactive practice  
    + short interactions to speak with a virtual character 
    + highlight words which are spoken incorrectly 

  - speech-to-speech translation 
  - automated marking 

* [IBM Reading Companion](http://www-07.ibm.com/ibm/hk/community/readingcompanion.html)


#### 2019-03-13 
* The application Factory 
    - 

* the layout 
    - speech/, a Python package containing application code and files 
    - tests/, a directory containing test modules 
    - venv/ 

* Start
  on powershell
  >  $env:FLASK_APP="ispeech.py"  
  >  $env:FLASK_ENV = "development" 
  > 
  on Windows  
  > set FLASK_APP="ispeech.py"  
  > set FLASK_ENV=development 
  > flask run 

* freeze 
  > pip3 freeze > requirements.txt
  > pip3 install -r requirements.txt

#### 2019-03-04 
* TODO 
  - a web-based system to improve English (word) pronouncation, and give a marker 
  - flask 

#### Customized speech recognition - A Technical Report

#### 2017-02-27 

#### 2019-01-24 
* In CMUSphinx phoneme recognition 

#### 2019-01-07 
* use keras 

* Dataset 
   - [GMU](https://www.kaggle.com/rtatman/speech-accent-archive#recordings.zip) 
     + variety of accents 
     + module to generalize the rules <- the differences 

   - CMU pronouncing dictionary

* Module
   - create phonological generalizations 


#### radio

#### reference 
* [2019 KDD Workshop on Deep Learning for Education (DL4Ed)](http://ml4ed.cc/2019-kdd-workshop/)
* [宝宝玩英语](http://www.babyfs.cn/about.html)
* [CS224S / LINGUIST285 - Spoken Language Processing](http://web.stanford.edu/class/cs224s/syllabus.html)
* [2017 KDD workshop - Advancing Education with Data](http://ml4ed.cc/2017-kdd-workshop/)
* [2016 NIPS Workshop - Machine Learning for Education](http://ml4ed.cc/2016-nips-workshop/)
* [Musicianship](https://www.coursera.org/learn/develop-your-musicianship/home/welcome)
* [writing](https://www.coursera.org/learn/introduction-to-research-for-essay-writing)
* [CRIS - (Custom Recognition Intelligent Service)](https://westus.cris.ai/Home/CustomSpeech)
* [Audio Signal Processing and Recognition](http://mirlab.org/jang/books/audioSignalProcessing/)
* Conferences: ICASSP, ICSLP, EuroSpeech
* [speech recognition](https://cmusphinx.github.io/wiki/tutorial/)
* [Musicianship](https://www.coursera.org/learn/develop-your-musicianship/home/welcome)
* [Links for English Pronunciation](https://www.ilc.cuhk.edu.hk/EN/ENResources/Speaking_Pronun.aspx)

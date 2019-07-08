### notes 



#### 2019-07-05
  * redo the frontend using tornado framework 
    - tornado is fast 

  * todo 
    - adjust the code on Chinese one 
    - train module based on english dataset

  * notes
    - there are errors to use jinja2 templates 

#### 2019-07-04 
  * 
  * set up the connect between local and server 
    - build opus dll on win
    - use tornado as server 
      + brautopy lib to upload audio to server 


#### 2019-07-03
  * check Vue.js + Flask 
    - drop 

#### 2019-07-02 
  * request ShefCE data 
  * check heroku

#### 2019-06-28 
  * opuslib 
  *  
  * about vue.js  
    > npm install -g @vue/cli 
    > 
    > vue create app  
    > s

#### 2019-06-27 
  * TODO - frontend
  * 
  * resource 
    - [ShefCE: A Cantonese-English bilingual speech corpus
](https://figshare.shef.ac.uk/articles/ShefCE_A_Cantonese-English_bilingual_speech_corpus_--_speech_recognition_model_sets_and_recording_transcripts/4522925)
    - [Corpus Linguistics in EdUHK](http://corpus.eduhk.hk/) 
    - [TIMIT](https://github.com/philipperemy/timit)
    - [emoji translation](https://meowni.ca/emoji-translate/)
   

#### 2019-06-25
  * about python 

#### 2019-06-24 
  * 
  * notes on the server 
    - the server: 10.237.4.253 raymond/raymond 
    - source /usr/local/tensorflow/bin/activate 
    - GPU: export CUDA_VISIBLE_DEVICES=0 
    - check gpu process : nvidiva-smi 


#### 2019-06-21 
  * ideas 
    - tts 
    - chatting 


#### 2019-06-20
  * python doc 

#### 2019-06-19 
  * give a presentation
  * todo 
    - more robust tests on current module 
    - give an introduction on deep learning 
    - module on English 

#### 2019-06-18
  * two issues
    - Extended pronunciation network ?



#### 2019-06-17 
  * rebuild web frontend using vue.js 
  * 

#### 2019-06-15 
  *  speaking corpus 
    - 
    - [cantonese corpus (HKCanCor)](http://compling.hss.ntu.edu.sg/hkcancor/)
  * notes on errors 
    > flask run --no-reload


#### 2019-06-14 
  * train a Module based on thchs30 Mandarin speech corpus 


#### 2019-06-13 
  * data format 
  * spoken database  
    - TIMIT database 
    - the WSJ database 
    - the Switchboard database 
    - the RAS 863 corpus (for Chinese) 
    
    - [Z. Z. Dong Wang, Xuewei Zhang, "THCHS-30: A free Mandarin speech corpus," 2015](https://arxiv.org/abs/1512.01882) 

  * add the recording audio function  
  * notes 
    - dataset 
      + [International Corpora](http://corpus.eduhk.hk/phonetics/Resources.aspx)
    - Kaldi Speech Recognition Toolkit 
    - fix the pocketsphinx  error 
     > pip install C:\pocketsphinx-0.1.15-cp37-cp37m-win_amd64.whl


#### 2019-06-12
  * training a module 
    - errors 
  * talk with Dr. Lam 

#### 2019-06-11 
  * setup the training env 

  * notes on errors in virtual env: 
    - create a virtual env 
     > pip install virtualenvwrapper-win 

    - activate the env in powershell 
     > C:\Users\raymondzhao\envs\speechenv\Scripts\activate.ps1

#### 2019-06-10 
  * TODO 
    - try to train an acoustic module 
    - check whether the dataset is fine 
    - combine with web 

  * fix the coding errors 
    - use python3.6 not python3.7 to support tensorflow 

  * speech model -> audio to phone-level transcription
    - acoustic module 
      + Hiden Markov Model (HMM) + GMM 
      + HMM + deeplearning -> CNN + LSTM/GRU  -> latest

    - CTC decode alg 
      +  

    - metrics 
      + accuracy: Word error rate (WER) 
      + 

    - dataset 
      + [Spoken Corpora by eduhk](http://corpus.eduhk.hk/English_Pronunciation/?page_id=2149)

#### 2019-06-06 
  * Speech Model 
    - acoustic module 
      + all of basic sounds of language given their context 
      + the likelihood p(o|w) 

    - pronunciation dictionary - lexicon 
      + how all the words get pronounced 

  * Language Model  (needn't) 
    - phonetic to word  

#### 2019-06-05 
  * it is slow/effectual to output the result 
    - the raw audio is too large (64M), and the audio quality isn't good 
    - the target is for a given utterance like a sentence 
    - thus, it's fine now

#### 2019-06-03 
  * build a web-based prototype   
    - Flask + React   
    - data-driven approaches 
    - demo 
      + Input: speak a given utterance - sentence
      + output: phone-level transcriptions 

  * Phoneme Recognition <- high errors now 
    - sound to phoneme  
    - phonemes itself are pretty loosely defined 
      + 17.7% on the TIMIT
phoneme recognition benchmark by Alex Graves - 2013 
    - the phone recognition error rate is typically much higher than word error rate even for native speakers, which makes it difficult to distinguish between pronunciation errors and recognition errors. 
    - 


  * ASR -> p(w|o) ~ p(o|w) * p(w)
    - acoustic module 
      + all of basic sounds of language given their context 
      + HMM - statistical representations for each phoneme in a language 

      + the likelihood p(o|w) 

    - pronunciation dictionary - lexicon 
      + how all the words get pronounced 
      + bulit by stringing together acoustic models 

    - language model - match a word or phrase 
      + p(w)
      + model of word sequences 

  * reference
    - [Emojist](http://emojist.com/)

#### 2019-05-31 
  * fix web uploading function 
    - change real-time function into uploading file -> too slow 

#### 2019-05-30 
  * task -> English phonetic erros firstly 
    - approach 
      + Free Speech Corpora ?  
      + acoustic models 
      + language models 
      + [openSLR](http://www.openslr.org/12/) 
    
    - metrics 

    - baseline  
    
    - demo  

  * gap 

#### 2019-05-29 
  * the doc 

#### 2019-05-28 
  * about python

#### 2019-05-23 
  * The **principle**  
  * a basic 

  * gap 
    - phonetic erros -> focus
    - prosodic  -> key of intelligibility 

#### 2019-05-22 
  * doc on python

#### 2019-05-20 
  * ispeaking: a web-based Pronunciation System for Cantonese Speakers English L2 Learners
   - do a basic recognition and checking 

  * how 
    - principle 
    - dataset 
      + ShefCE dataset ?
    - module  

#### 2019-05-20 
  * project on Enlgish mispronunciation detection 

  * support iCon project  
    -> A new idea/min-project about GAN/NLU by myself  ?  

  * join the project on 靈實 
    -> not in engineering and business view if possible ? 

  * fake news 

#### 2019-05-16 
  * mispronunciation detection 
  * another project -> NLP ?

#### 2019-05-15 
  * mispronunciation detection  <- hard 
    - phoneme-based recognition and then identify pronunciation errors in the learners’ speech 
    =>  pronunciation errors and recognition errors

    - the acoustic models and an extended pronunciation dictionary with possible erroneous pronunciation variations are used to recognize the most likely phone sequences 
    =>  reduce recognition errors 

  * reference 
    - [Computer Aided Pronounciation Training in CUHK](http://www1.se.cuhk.edu.hk/~hccl/languagelearning/index_publications.htm)

  * fake news 
    - using Sentiment Analysis 


#### 2019-05-14 
  * proposal - how to pursue it 
    - English (word) Pronunciation (coach) 
      + checking and feedback - 
        - recognizing word and compared with standarded one 

      + assessment - 

    - fake news <- using Sentiment Analysis  

  * dev <- Heroku  


#### 2019-05-10 
  * mini-proposal 
    - pronunciation 
      + checking and feedback 
      + assessment

    - fake news  
    Detecting Fake Reviews through Sentiment Analysis Using Machine Learning Techniques 


#### 2019-05-08 
  * fake news 
  * GAN - generative adversarial networks 

  * ideas in ASR + education
    - customer **pronunciation dictionary** using deeplearning 
      + grapheme-to-phoneme conversion 

    - a British/American English pronunciation dictionary 
      + maps English words to their pronunciations as per the International Phonetic Alphabet. 
      + [Dictionary](https://github.com/JoseLlarena/britfoner)
   
    - product 
      + [ELSA](https://www.forbes.com/sites/chynes/2016/08/30/the-app-using-artificial-intelligence-to-improve-english-speaking-skills/#447723c31c82) 

  * reference 
    - [Automatic Pronunciation Intelligibility Assessment](https://medium.com/viithiisys/automatic-pronunciation-intelligibility-assessment-de5a6b8c990c)


#### 2019-05-06 
  * ideas in ASR + education 
   - computer-aided language learning (CALL) <- ASR 
     + on vocabulary, grammar, semantics checking 
     + based on a comparison with models trained on data from native speakers as well as the lab’s state-of-the art text-to-speech synthesis technology. 
     + Instant and precise feedbacks on every sound 
     + you make Free interactive pronunciation dictionary

     + -> Spoken Language Understanding - English - NLU 

   - computer-aided pronunciation training (CAPT) 
     + pronunciation assessment 

     + Automatic scoring 

     + Automatic scoring of non-native speech in tests of spoken English 
     + A evaluating model of english pronunciation for Chinese students 


#### 2019-04-24 
* doc on deep learning    

#### 2019-04-16 
* exercise on python programming 
  - generator

#### 2019-04-15 
* - survey 

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
* [ELSA](https://elsaspeak.com/home)
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

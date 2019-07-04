<template>
  <div class="row">
    <div class="toggle" @click="toggle">TOGGLE</div>

    <audio-recorder v-if="showRecorder"
      upload-url="http://localhost:5000/record"
      filename="ninja"
      format="wav"
      :attempts="3"
      :time="2"
      :headers="headers"
      :before-recording="callback"
      :pause-recording="callback"
      :after-recording="callback"
      :select-record="callback"
      :before-upload="callback"
      :successful-upload="callback"
      :failed-upload="callback"
      :bit-rate="192"/>

    <audio-player :src="mp3" v-if="!showRecorder"/>
  </div>
</template>


<script>

export default {
    name: 'record',
    data() {
        return {
            mp3: 'C:\Users\raymondzhao\myproject\dev.speech\ispeaking\data\english81.wav',
            showRecorder: true,
            headers: {
                'X-Custom-Header': 'some data'
            },
        }
    },

    methods: {
       callback (msg) {
        console.debug('Event: ', msg)
      },
       toggle () {
        this.showRecorder = !this.showRecorder
      },
    },

};
</script>

<style lang="scss">
  .toggle {
    cursor: pointer;
    margin: 20px;
  }
</style>

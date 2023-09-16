<script setup>
import axios from 'axios'
import {ref} from 'vue'
const inputVal = ref('')
const imgSrc = ref('')
const callAPI = () =>{
  console.log(inputVal.value)
  let body = {}
  body.id = inputVal.value
  console.log(body)
  axios.post("http://localhost:8000/product", body)
  .then((res) =>{
    console.log("Call result", res)
    imgSrc.value = res.data.img_path
  })
} 

</script>

<template>
  <div>
    <img v-bind:src="imgSrc"/>
  </div>  
  <div>
    <input v-model="inputVal"/>
  </div>
  <div>
    <button @click="callAPI">Test</button>
  </div>  
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>

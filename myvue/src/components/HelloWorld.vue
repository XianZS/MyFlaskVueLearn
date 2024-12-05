<script setup lang="ts">
import axios from 'axios';
import {reactive} from "vue";


function show() {
    axios.get("http://172.24.105.186:5000/login/login").then((response) => {
        user.some = response.data;
        console.log(response.data);
    })
}

let user = reactive({some: null})
</script>

<template>
    <button @click="show">点击</button>
    {{ user.some }}
</template>

<script lang="ts">
  import { defineComponent, ref } from 'vue';
  import axios from 'axios';
  import { Data , Story } from '../types'
  
  export default defineComponent({
    props: {
      apiUrl: {
        type: String,
        required: true,
      },
    },
    emits : ['fetchArgument'],
    setup(props, {emit}) {
      // const apiUrl = ref('http://127.0.0.1:8000/latest-stories/')
      const currentPage = ref(0);
      const totalPages = ref();
      const next = ref<string>();
      const current = ref<string>(props.apiUrl);
      const previous = ref<string | null>();
      const results = ref<Story[]>(); 

      const triggeredFetch = (url: string) => {
        emit('fetchArgument', url)
      }
  
      // Function to fetch data for a specific page
      const fetchStories = async () => {
        try {
          const response = await axios.get<Data>(current.value)
          const data = response.data;
  
          totalPages.value = data.count;
          next.value = data.next;
          previous.value = data.previous;

          triggeredFetch(data.next)

        } catch (error) {
          console.error('Error fetching stories:', error);
        }
      };
  
      // Function to navigate to the next page
      const nextPage = () => {
        if (next.value != null) {
          currentPage.value++;
          current.value = next.value;
          fetchStories();
        }
      };
  
      // Function to navigate to the previous page
      const prevPage = () => {
        if (previous.value != null) {
          currentPage.value--;
          current.value = previous.value;
          fetchStories();

        }
      };

      fetchStories()
  
      return {
        currentPage,
        totalPages,
        next,
        previous,
        results,
        nextPage,
        prevPage,
        
      };
    },
  });
  </script>

<template>
    <div class="wrapper">
      <div class="align">
        <div class="search-box">
          <button @click="prevPage" :disabled="!currentPage">Previous</button>
          <span>{{ currentPage }} / {{ totalPages }}</span>
          <button @click="nextPage" :disabled="!next">Next</button>
        </div>
      </div>
    </div>
  </template>
  
  <style scoped>
.wrapper {
  background: #f8f5f5;
}
.align {
  padding-top: 10px;
  margin: auto;
  max-width: 740px;
  background-color: #fff;
}
.search-box {
  width: fit-content;
  margin: auto;
}
span {
  margin-right: 3px;
  margin-left: 3px;
}
  </style>
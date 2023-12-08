<script lang="ts">
  import { defineComponent, ref, onMounted } from 'vue';
  import axios from 'axios';
  import { Data , Story } from '../types'
  
  export default defineComponent({
    props: {
      apiUrl: {
        type: String as () => string,
        required: true,
      },
    },
    setup(props, {emit}) {
      const currentPage = ref(1);
      const totalPages = ref(1);
      const next = ref('');
      const previous = ref<string | null>(null);
      const results = ref<Story[]>([]); 
  
      // Function to fetch data for a specific page
      const fetchStories = async (page: number) => {
        try {
          const response = await axios.get<Data>(`${props.apiUrl}?page=${page}`);
          const data = response.data;
  
          results.value = data.results;
          currentPage.value = page;
          totalPages.value = data.count;
          next.value = data.next;
          previous.value = data.previous;
            
          emit('fetchStories', `${props.apiUrl}?page=${page}`);
        } catch (error) {
          console.error('Error fetching stories:', error);
        }
      };
  
      // Function to navigate to the next page
      const nextPage = () => {
        if (next.value) {
          currentPage.value++;
          fetchStories(currentPage.value);
        }
      };
  
      // Function to navigate to the previous page
      const prevPage = () => {
        if (previous.value) {
          currentPage.value--;
          fetchStories(currentPage.value);
        }
      };
  
    //   // Watch changes in apiUrl prop and fetch stories when it changes
    //     watch(() => props.apiUrl, () => {
    //     fetchStories(currentPage.value);
    //     });
  
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
    <div>
      <!-- Pagination buttons -->
      <div>
        <button @click="prevPage" :disabled="!previous">Previous</button>
        <span>{{ currentPage }} / {{ totalPages }}</span>
        <button @click="nextPage" :disabled="!next">Next</button>
      </div>
    </div>
  </template>
  
  <style scoped>
  /* Styles for pagination buttons */
  /* ... */
  </style>
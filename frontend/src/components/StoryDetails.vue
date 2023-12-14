<template>
    <div>
      <!-- <h2>{{ story.title }}</h2> -->
      <!-- Display story details and comments here -->
      <button @click="goBack">Back</button>
      <button @click="deleteStory">Delete</button>
      <button @click="updateStory">Update</button>
      <!-- Add comment creation functionality here -->
    </div>
  </template>
  
  <script lang="ts">
  import { defineComponent, ref , onMounted } from 'vue';
  // import { Data, Story } from '../types';
  import { useRouter } from 'vue-router';
  // import axios from 'axios';
  
  export default defineComponent({
    setup() {
      const router = useRouter();
      const storyId = ref();
      // const story = ref<Story[]>([]);

      onMounted(() => {
      // Access the ID from the route parameters
      const id = router.currentRoute.value.params.id;
      storyId.value = id;
      // Fetch story details based on the ID
      // Use the storyId.value to fetch the corresponding story details
    });

      const goBack = () => {
        router.push({ name: 'StoryPage' });
      };

      const deleteStory = () => {
          // Implement delete story functionality using the API endpoint
      };
    
      const updateStory = () => {
          // Implement update story functionality using the API endpoint
      }; 
    
      return {
        goBack,
        deleteStory,
        updateStory,
      };
    },
  });
  </script>

<script lang="ts">
import { defineComponent, ref, watch } from 'vue';
import { Story, Data } from '../types'; 
import axios from 'axios'

export default defineComponent({
  components: {
  },
  setup() {
    const stories = ref<Story[]>([]); // Fetch stories from API and store in this variable
    const URL = ref<string>('http://127.0.0.1:8000/latest-stories/');
    const searchText = ref<string>('');
    const totalPage = ref(100);


    // Function to fetch stories
    const fetchStories = async () => {
      try {
        const response = await axios.get<Data>(`${URL.value}?page=${store.currentPage}${filter}`);
        const data: Data = response.data;
        stories.value = data.results
        totalPage.value = data.count
      } catch (error) {
        console.error('Error fetching stories:', error);
      }
    };

    // Function to fetch stories based on the search text
    const searchStories = async () => {
      try {
        const response = await axios.get<Data>(
          `http://127.0.0.1:8000/story-search/?search=${searchText.value}&?page=${store.currentPage}`
        );
        const data: Data = response.data;
        stories.value = data.results;
      } catch (error) {
        console.error('Error searching stories:', error);
      }
    };

    const newsClicked = () => {
      URL.value = 'http://127.0.0.1:8000/filter-by-score/'
      store['currentPage'] = 1
      fetchStories()
    }
    const newestClicked = () => {
      URL.value = 'http://127.0.0.1:8000/latest-stories/'
      store['currentPage'] = 1
      fetchStories()
    }
    const askClicked = () => {
      URL.value = 'http://127.0.0.1:8000/filtered-stories/'
      store['currentPage'] = 1
      fetchStories('&filter=ask') 
    }
    const showClicked = () => {
      URL.value = 'http://127.0.0.1:8000/filtered-stories/'
      store['currentPage'] = 1
      fetchStories('&filter=show')
    }
    const jobClicked = () => {
      URL.value = 'http://127.0.0.1:8000/filtered-stories/'
      store['currentPage'] = 1
      fetchStories('&filter=job')
    }


    
    fetchStories(); // Fetch stories when component is mounted
    watch(
      () => store.currentPage,
      () => {
        fetchStories();
      }
    );

    return {
      stories,
      newsClicked,
      newestClicked,
      askClicked,
      showClicked,
      jobClicked,
      searchText,
      searchStories,
      totalPage,
      fetchStories,
      URL,
    };
  },
});
</script>

<template>
  <h1>Detail Page</h1>
</template>

<style scoped>

</style>
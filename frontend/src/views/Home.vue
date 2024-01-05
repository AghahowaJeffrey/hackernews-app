<script lang="ts">
import { defineComponent, ref, watch } from 'vue';
import StoryList from '../components/StoryList.vue';
import StoryDetail from '../components/StoryDetails.vue';
import PageNavigation from '../components/PageNavigation.vue'
import { Story, Data } from '../types'; 
import { store } from '../store'
import axios from 'axios'

export default defineComponent({
  components: {
    StoryList,
    StoryDetail,
    PageNavigation,
  },
  setup() {
    const stories = ref<Story[]>([]); // Fetch stories from API and store in this variable
    const URL = ref<string>('http://127.0.0.1:8000/latest-stories/');
    const searchText = ref<string>('');
    const totalPage = ref(100);


    // Function to fetch stories
    const fetchStories = async (filter: string = '') => {
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
  <div class="main-container">
    <div>
      <header>
        <div class="align">
          <div class="nav-container">
            <h1 class="logo">HACKERNEWS</h1>
            <nav class="navigation">
              <ul>
                <li @click="newsClicked">News</li>
                <li @click="newestClicked">Newest</li>
                <li @click="askClicked">Ask</li>
                <li @click="showClicked">Show</li>
                <li @click="jobClicked">Job</li>
                <router-link :to="{name: 'CreatePost'}"><li>Submit</li></router-link>
              </ul>
            </nav>
            
          </div>
          <div class="searchbox">
            <input v-model="searchText">
            <button @click="searchStories">Search</button>
          </div>
        </div> 
      </header>
      <PageNavigation :totalPage="totalPage" />
      <StoryList :stories="stories"  />
    </div>
  </div>
</template>

<style scoped>
* { 
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
}
header {
  background: #211f1f;
  color: #ffffff;
  padding-block-start: 10px;
  padding-block-end: 10px;
  padding-left: 10px;
  padding-right: 10px;
  width: 100%;
  margin: auto;
}
.align {
  margin: auto;
  max-width: 740px;
}
.nav-container {
  display: flex;
  align-items: center;
}
.logo {
  font-size: 15px;
  color: #00dc82
}
.navigation ul{
  list-style: none;
  display: flex;
}
.navigation li {
  padding-right: 20px;
  font-weight: normal;
  font-size: 15px;
  cursor: pointer
}
.navigation li:hover {
  color: #00dc82
}
.searchbox input{
  outline: none;
  width: 200px;
  height: 30px;
  border: 0
}
.searchbox button {
  height: 30px;
  color: #ffffff;
  background-color: #03b269;
  border: 0;
}

a {
    text-decoration: none;
    color: #ffffff
}

</style>
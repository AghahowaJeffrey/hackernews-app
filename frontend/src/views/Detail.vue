<script lang="ts">
  import { defineComponent, ref } from 'vue';
  import { useRoute } from 'vue-router'
  import { Story } from '../types'; 
  import axios from 'axios';
  import { timeAgo } from '../utils';


  export default defineComponent({
    setup() {
      const route = useRoute()
      const storyData = ref<Story | undefined>()
      // const { convert } = require('html-to-text');

      const fetchUser = async (ID: String | String[]) => {
        try {
          const response = await axios.get<Story>(`http://127.0.0.1:8000/stories/${ID}`);
          console.log(`http://127.0.0.1:8000/stories/${ID}`)
          const data: Story = response.data;
          console.log(data)
          if (data) {
            storyData.value = data
          }
          
        } catch (error) {
          console.error('Error fetching stories:', error);
        }
      }

      // fetch the user information when params change
      
      fetchUser(route.params.id)
      return {
        storyData,
        timeAgo,
      };
    },
  });
</script>

<template>
  <div class="main-container">
    <div class="align">
      <div class="title-container">
        <h1>{{ storyData?.title }}</h1>
        <h2 class="time">{{ timeAgo(storyData?.time) }}</h2>
      </div>
      <p class="text">{{ storyData?.text }}</p>
      <a class=" story-url" :href="storyData?.url" target="_blank">LINK</a>
      <div class="main-body">
        <p class="comment-count">{{ storyData?.descendants }} Comments</p>
        <div class="comment-container" v-for="comment in storyData?.comments">
          <p class="by">{{ comment.by }} <span class="comment-time">{{ timeAgo(comment.time) }}</span></p>
          <p class="comment">{{ comment.text }}</p>
          
        </div>
      </div>
    </div>  
  </div>


</template>

<style scoped>

* { 
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
}

.main-container {
  background-color: #f8f5f5;
}

.align {
  margin: auto;
  max-width: 740px;
  background-color: #ffffff;
}

.title-container {
  background-color: #211f1f;
  color: #ffffff;
  padding: 10px
}

.title h1 {
  font-size: 23px;
}

.time {
  color: #00dc82;
  font-size: 16px;
  border-top: 1px solid #00dc82;
}

.comment-time {
  color: #00dc82;
  font-size: 12px;
}
.main-body {
  padding: 10px
}

.text {
  background-color: #f4f1f1;
  padding: 10px;
}

.story-url {
  text-decoration: none;
  font-size: 16px;
  display: block;
  max-width: fit-content;
  /* border-radius: 20px; */
  margin: 5px 0 20px 10px ;
  padding: 4px 10px 4px 10px;
  background-color: #00dc82;
  color: #000000;
}
.comment-count {
  border: 1px solid #211f1f;
  margin-bottom: 15px;
  padding: 5px;
  background-color: #00dc82;
}

.by {
  font-size: 20px;
  color: #211f1f;
  padding: 3px;
  font-weight: 600;
}
.comment-container {
  padding: 0px 10px 0 20px;
}
.comment {
  word-wrap: break-word;
  margin-bottom: 20px;
  border-bottom: 1px solid #00dc82;

}
</style>
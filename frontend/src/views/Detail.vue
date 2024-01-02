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
      console.log(route.params.id)
      console.log(storyData.value)
      return {
        storyData,
        timeAgo
      };
    },
  });
</script>

<template>
  <div class="main-container">
    <div class="align">
      <h1>{{storyData?.title}}</h1>
      <h2>{{timeAgo(storyData?.time)}}</h2>
      <p>{{storyData?.text}}</p>
      <p>{{ storyData?.descendants }} Comments</p>
        <ul>
          <li class="comment" v-for="comment in storyData?.comments">
            {{ comment.text }}
          </li>
        </ul>
    </div>  
  </div>


</template>

<style scoped>

.main-container {
  background-color: #f8f5f5;
}

.align {
  margin: auto;
  padding: 10px;
  max-width: 740px;
  background-color: #ffffff;
}

.comment {
  margin-left: 50px;
  margin-bottom: 30px;
  border-bottom: 1px solid green;
}
</style>
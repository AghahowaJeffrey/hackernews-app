<script lang="ts">
import { defineComponent, PropType } from 'vue';
import { Story } from '../types';
import { timeAgo } from '../utils';
// import { useRouter } from 'vue-router';


export default defineComponent({
  props: {
    stories: {
      type: Array as PropType<Story[]>,
      required: true,
    },
  },
  setup(props) {

    return {
      timeAgo
    };
  },
});
</script>

<template>
  <div class="container">
    <div class="align">
      <div class="story-box">
        <div class="stories" v-for="story in stories" :key="story.id">
          <p class="score">{{ story.score }}</p>
          <router-link :to="{name: 'DetailPage', params: {id: story.id}}">
          <div class="story-info">
              <h1 class="title">{{ story.title }}</h1>
              <p >by <span class="author">{{ story.by }} </span><span class="time">{{ timeAgo(story.time) }}</span> | 
                <span class="comment">{{ story.descendants }} comments</span></p>
          </div>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
a {
  text-decoration: none;
  color: inherit;
}
.container {
  background: #f8f5f5;
}
.align {
  background: #ffffff;
  margin: auto;
  max-width: 740px;
  
}
.story-box {
  padding: 10px;
}
.stories {
  display: flex;
  align-items: center;
  gap: 20px;
  justify-content: left;
  border-bottom:1px solid #00dc82;
}
.score {
  width:60px;
  padding: 30px;
  font-size: 20px;
}
.story-info {
  line-height: 1;
  padding-block: 10px;
}
.title {
  font-size: 16px;
  font-weight: 400px;
  margin-bottom: 8px;
}
.author {
  text-decoration: underline;
  margin-right: 10px;
}
.author:hover {
  color: #00dc82
}
.comment {
  text-decoration: underline;
}
.comment:hover {
  color: #00dc82;
}
</style>
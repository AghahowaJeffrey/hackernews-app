<template>
  <div id="app">
    <StoryList />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import StoryList from './components/StoryList.vue';

export default  defineComponent({
  name: 'App',
  components: {
    
  },
  setup() {
    return {};
  },
});
</script>

<style>
/* Add your styles here */
</style>
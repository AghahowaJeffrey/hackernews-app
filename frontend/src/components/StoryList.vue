<template>
    <div>
      <h2>Latest Stories</h2>
      <ul>
        <li v-for="story in stories" :key="story.id">
          <h3>{{ story.title }}</h3>
          <p>{{ story.text }}</p>
          <ul>
            <li v-for="comment in story.comments" :key="comment.id">
              <p>{{ comment.text }}</p>
              <!-- Display other comment details as needed -->
            </li>
          </ul>
          <hr>
        </li>
      </ul>
    </div>
  </template>
  
  <script lang="ts">
  
  </script>
  
  <style>
  /* Add your styles here */
  </style>
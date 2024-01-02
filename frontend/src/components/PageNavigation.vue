<script lang="ts">
  import { defineComponent} from 'vue';
  import { store } from '../store'

  
  export default defineComponent({
    props: {
      totalPage: {
        type: Number,
        required: true,
      },
    },
    setup(props) {

      // Function to navigate to the next page
      const nextPage = () => {
        if (store.currentPage != props.totalPage) {
          store.currentPage++;
        }
      };
  
      // Function to navigate to the previous page
      const prevPage = () => {
        if (store.currentPage != 0) {
          store.currentPage--;
        }
      };

      const checkNextPage = () => {
        if (store.currentPage == props.totalPage) {
          return true
        } else {
          return false
        }
      }

      const checkPrevPage = () => {
        if (store.currentPage > 1) {
          return false
        } else {
          return true
        }
      }

      const totalPageRounder  = () => {
        if (props.totalPage <= 10) {
          return 1
        } else {
          return Math.round(props.totalPage / 10)
        }
      }
      console.log(props.totalPage)

      return {
        store,
        totalPageRounder,
        nextPage,
        prevPage,
        checkNextPage,
        checkPrevPage,
        
      };
    },
  });
  </script>

<template>
    <div class="wrapper">
      <div class="align">
        <div class="search-box">
          <button @click="prevPage" :disabled="checkPrevPage()">Previous</button>
          <span>{{ store.currentPage }} / {{ totalPageRounder() }}</span>
          <button @click="nextPage" :disabled="checkNextPage()">Next</button>
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
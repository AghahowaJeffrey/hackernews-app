import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';

// Import your components for main and detailed pages
import StoryDetails from '../App.vue'
import StoryList from '../components/StoryList.vue';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'StoryPage',
    component: StoryList,
  },
  {
    path: '/story/:id',
    name: 'DetailPage',
    component: StoryDetails,
    props: true, // Pass route params as props to the component
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
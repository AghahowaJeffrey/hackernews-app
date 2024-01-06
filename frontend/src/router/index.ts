import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';

// Import your components for main and detailed pages
import Home from '../views/Home.vue';
import Post from '../views/Post.vue';
import Detail from '../views/Detail.vue';
import Edit from '../views/Edit.vue';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'HomePage',
    component: Home,
  },
  {
    path: '/post',
    name: 'CreatePost',
    component: Post,
  },
  {
    path: '/story/:id',
    name: 'DetailPage',
    component: Detail,
    // props: true,

  },
  {
    path: '/edit/:id',
    name: 'EditPage',
    component: Edit,
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
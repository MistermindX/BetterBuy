import VueRouter from 'vue-router'
import Home from './pages/Home'
import CategorySearch from './pages/CategorySearch'
const routes = [
  { path: '/', component: Home, name: 'Home' },
  {
    path: '/categories/:category_id',
    component: CategorySearch,
    name: 'CategorySearch'
  }
]

export default new VueRouter({ routes, mode: 'history' })

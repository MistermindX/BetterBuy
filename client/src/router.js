import VueRouter from 'vue-router'
import Home from './pages/Home'
import CategorySearch from './pages/CategorySearch'
import SignIn from './pages/SignIn'

const routes = [
  { path: '/', component: Home, name: 'Home' },
  {
    path: '/categories/:category_id',
    component: CategorySearch,
    name: 'CategorySearch'
  },
  { path: '/signin', component: SignIn, name: 'SignIn' }
]

export default new VueRouter({ routes, mode: 'history' })

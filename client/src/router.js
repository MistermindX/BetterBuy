import VueRouter from 'vue-router'
import Home from './pages/Home'
import CategorySearch from './pages/CategorySearch'
import SignIn from './pages/SignIn'
import ItemDetail from './pages/ItemDetail'

const routes = [
  { path: '/', component: Home, name: 'Home' },
  {
    path: '/categories/:category_id',
    component: CategorySearch,
    name: 'CategorySearch'
  },
  { path: '/signin', component: SignIn, name: 'SignIn' },
  { path: '/items/:item_id', component: ItemDetail, name: 'ItemDetail' }
]

export default new VueRouter({ routes, mode: 'history' })

<template>
  <div id="app">
    <Nav />
    <main>
      <!-- Routes Go Here -->
      <router-view></router-view>
    </main>
  </div>
</template>

<script>
import Nav from './components/Nav.vue'
export default {
  name: 'App',
  components: {
    Nav
  }
}
</script>


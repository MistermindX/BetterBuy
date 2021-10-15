<template>
  <div class="flex-content">
    <CategoryCard
      v-for="category in categories"
      :key="category.id"
      :name="category.name"
      :image="category.image"
    />
  </div>
</template>

<script>
import axios from 'axios'
import CategoryCard from '../components/CategoryCard.vue'
export default {
  name: 'Home',
  components: { CategoryCard },
  data: () => ({
    categories: [],
    searchQuery: '',
    searchResults: [],
    searched: false
  }),
  mounted() {
    this.getCategories()
  },
  methods: {
    async getCategories() {
      const res = await axios.get(`http://localhost:5000/categories`)
      this.categories = res.data
    }
  }
}
</script>

<style scoped>
</style>
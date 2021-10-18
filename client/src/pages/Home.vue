<template>
  <div class="content">
    <CategoryCard
      v-for="category in categories"
      :key="category.id"
      :name="category.name"
      :image="category.image"
      :id="category.id"
      @navigateCategory="navigateCategory"
    />
  </div>
</template>

<script>
import axios from 'axios'
import CategoryCard from '../components/CategoryCard.vue'
import { BASE_URL } from '../globals'
export default {
  name: 'Home',
  components: { CategoryCard },
  data: () => ({
    categories: []
  }),
  mounted() {
    this.getCategories()
  },
  methods: {
    async getCategories() {
      const res = await axios.get(`${BASE_URL}/categories`)
      this.categories = res.data
      console.log(localStorage.getItem('token'))
    },
    navigateCategory(id) {
      this.$router.push(`/categories/${id}`)
    }
  }
}
</script>
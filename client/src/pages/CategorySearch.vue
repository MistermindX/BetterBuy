<template>
  <div>{{ category.name }}</div>
</template>

<script>
import { categories } from './Home.vue'
export default {
  name: 'CategorySearch',
  data: () => ({
    category: null
  }),
  mounted: function () {
    this.category = categories.find(
      (category) => category.id === parseInt(this.$route.params.category_id)
    )
  }
}
</script>
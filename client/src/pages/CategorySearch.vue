<template>
  <div class="flex-content">
    <ItemCard
      v-for="item in items"
      :key="item.id"
      :name="item.name"
      :image="item.image"
      :id="item.id"
      :price="item.price"
      :description="item.description"
      @navigateItem="navigateItem"
    />
  </div>
</template>

<script>
import axios from 'axios'
import ItemCard from '../components/ItemCard.vue'
import { BASE_URL } from '../globals'
export default {
  name: 'CategorySearch',
  components: { ItemCard },
  data: () => ({
    items: []
  }),
  mounted() {
    this.getItems()
  },
  methods: {
    async getItems() {
      const res = await axios.get(
        `${BASE_URL}/categories/items/${this.$route.params.category_id}`
      )
      this.items = res.data.items
    },
    navigateItem(id) {
      this.$router.push(`/items/${id}`)
    }
  }
}
</script>
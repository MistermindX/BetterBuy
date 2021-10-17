<template>
  <div class="item-page">
    <button @click="goBackToItemList()">{{ category.name }}</button>
    <div class="item">
      <div class="item-words">
        <h2>{{ item.name }}</h2>
        <p class="description">{{ item.description }}</p>
      </div>
      <div><img :src="item.image" /></div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { BASE_URL } from '../globals'
export default {
  name: 'ItemDetail',
  data: () => ({
    item: {},
    category: {}
  }),
  async mounted() {
    await this.getItemDetails(), this.getCategoryDetails()
  },
  methods: {
    async getItemDetails() {
      const res = await axios.get(
        `${BASE_URL}/items/id/${this.$route.params.item_id}`
      )
      this.item = res.data
    },
    async getCategoryDetails() {
      const res = await axios.get(
        `${BASE_URL}/categories/${this.item.category_id}`
      )
      this.category = res.data
    },
    goBackToItemList() {
      this.$router.push(`/categories/${this.item.category_id}`)
    }
  }
}
</script>
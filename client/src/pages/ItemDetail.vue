<template>
  <div class="item">
    <p>{{ item.name }}</p>
    <p>{{ item.description }}</p>
    <img :src="item.image" />
  </div>
</template>

<script>
import axios from 'axios'
import { BASE_URL } from '../globals'
export default {
  name: 'ItemDetail',
  data: () => ({
    item: {}
  }),
  mounted() {
    this.getItemDetails()
  },
  methods: {
    async getItemDetails() {
      const res = await axios.get(
        `${BASE_URL}/items/id/${this.$route.params.item_id}`
      )
      this.item = res.data
    }
  }
}
</script>
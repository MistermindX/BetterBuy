<template>
  <div class="store-list">
    <StoreCard
      v-for="store in stores"
      :key="store.id"
      :address="store.address"
      :id="store.id"
    />
  </div>
</template>

<script>
import axios from 'axios'
import StoreCard from '../components/StoreCard.vue'
import { BASE_URL } from '../globals'
export default {
  name: 'StoreList',
  components: { StoreCard },
  data: () => ({
    stores: []
  }),
  mounted() {
    this.getStores()
  },
  methods: {
    async getStores() {
      const res = await axios.get(`${BASE_URL}/stores`)
      this.stores = res.data
    }
  }
}
</script>
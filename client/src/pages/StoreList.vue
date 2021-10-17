<template>
  <div class="flex-content"></div>
</template>

<script>
import axios from 'axios'
import { BASE_URL } from '../globals'
export default {
  name: 'StoreList',
  components: {},
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
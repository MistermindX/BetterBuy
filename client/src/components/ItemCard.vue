<template>
  <div class="card" @click="navigateItem(id)">
    <div class="image-wrapper">
      <img :src="image" />
    </div>
    <div class="info-wrapper flex-col">
      <h3>{{ name }}</h3>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ItemCard',
  props: ['name', 'image', 'id'],
  methods: {
    navigateItem(id) {
      this.$emit('navigateItem', id)
    }
  }
}
</script>
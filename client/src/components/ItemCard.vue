<template>
  <div class="card" @click="navigateItem(id)">
    <div class="image-wrapper">
      <img :src="image" />
    </div>
    <div class="info-wrapper flex-col">
      <h3>{{ name }}</h3>
      <h5>{{ description }}</h5>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ItemCard',
  props: ['name', 'image', 'id', 'description'],
  methods: {
    navigateItem(id) {
      this.$emit('navigateItem', id)
    }
  }
}
</script>
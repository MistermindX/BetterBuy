<template>
  <div class="card" @click="navigateItem(id)">
    <div class="image-wrapper">
      <img :src="image" :alt="name" />
    </div>
    <div class="info-wrapper">
      <h3>{{ name }}</h3>
      <h5>${{ price }}</h5>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ItemCard',
  props: ['name', 'image', 'id', 'description', 'price'],
  methods: {
    navigateItem(id) {
      this.$emit('navigateItem', id)
    }
  }
}
</script>
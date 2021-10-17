<template>
  <div class="card" @click="navigateCategory(id)">
    <div class="image-wrapper">
      <img :src="image" :alt="name" />
    </div>
    <div class="info-wrapper flex-col">
      <h3>{{ name }}</h3>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CategoryCard',
  props: ['name', 'image', 'id'],
  methods: {
    navigateCategory(id) {
      this.$emit('navigateCategory', id)
    }
  }
}
</script>
<template>
  <div>{{ category.name }}</div>
</template>

<script>
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
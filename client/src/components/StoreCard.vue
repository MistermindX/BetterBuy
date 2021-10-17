<template>
  <div class="store-card">
    <h2>Store Number: {{ id }}</h2>
    <h2>{{ address }}</h2>
  </div>
</template>

<script>
export default {
  name: 'StoreCard',
  props: ['address', 'id']
}
</script>
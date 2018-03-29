<template>
  <div class="casecell">
    <h3 :id="title" class="cell-classify">{{title}}</h3>
    <ul class="cell-list">
      <li class="cell-list m-button" v-for="(item, index) in data" :key="index" @click="$router.push(`/case/${item}`)">{{item}}</li>
    </ul>
  </div>
</template>
<script>
export default {
  components: {},
  props: ['title', 'data'],
  data () {
    return {
    }
  },
  computed: {},
  mounted () {},
  methods: {}
}
</script>
<style lang="scss">
.casecell {
  margin-top: 40px;
  .cell {
    &-classify {
      margin-bottom: 20px;
    }
    &-list {
      display: flex;
      flex-wrap: wrap;
    }
  }
}
</style>
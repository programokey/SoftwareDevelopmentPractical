<template>
  <ul class="classification">
    <slot></slot>
    <li v-for="(item,index) in list" :key="index">{{item}}</li>
  </ul>
</template>
<script>
export default {
  components: {},
  props: {},
  data () {
    return {
      list: ['分类1', '分类2', '分类3', '分类4', '分类5', '分类6', '分类7', '分类8']
    }
  },
  computed: {},
  mounted () {},
  methods: {}
}
</script>
<style lang="scss">

</style>
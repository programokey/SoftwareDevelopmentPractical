<template>
  <ul class="classification">
    <li v-for="(item,index) in classifyList" :key="index">{{item}}</li>
  </ul>
</template>
<script>
export default {
  components: {},
  props: ['classifyList'],
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
.classification {
  padding-top: 30px;
  // height: 100%;
  height: 100%;
  overflow-y: scroll !important;

  li {
    margin: 0 10px 30px;
    // margin-bottom: 30px;
    font-size: 20px;
    color: $green;
    line-height: 30px;
    cursor: pointer;
  }
}
</style>
<template>
  <div class="classification">
    <a v-for="(item,index) in classifyList" :key="index" :href="`#${item}`">{{item}}</a>
  </div>
</template>
<script>
export default {
  components: {},
  props: ['classifyList'],
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
.classification {
  padding-top: 30px;
  // height: 100%;
  height: 100%;
  overflow-y: scroll !important;

  a {
    display: block;
    margin: 0 10px 30px;
    // margin-bottom: 30px;
    font-size: 20px;
    color: #fff;
    line-height: 30px;
    cursor: pointer;
  }
}
</style>
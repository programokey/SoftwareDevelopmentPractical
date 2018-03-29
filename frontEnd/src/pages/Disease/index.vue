<template>
  <div>
    <el-breadcrumb class="breadcrumb" separator="/">
      <el-breadcrumb-item :to="{ path: '/learn' }">病例学习</el-breadcrumb-item>
      <el-breadcrumb-item>{{$route.params.caseName}}</el-breadcrumb-item>
    </el-breadcrumb>
    <div>病例列表</div>
  </div>
</template>
<script>
export default {
  components: {},
  props: {},
  data () {
    return {}
  },
  computed: {},
  mounted () {},
  methods: {}
}
</script>
<style lang="scss">

</style>
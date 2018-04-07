<template>
  <div class="disease">
    <el-breadcrumb class="breadcrumb" separator="/">
      <el-breadcrumb-item :to="{ path: '/learn' }">病例学习</el-breadcrumb-item>
      <el-breadcrumb-item>{{$route.params.caseName}}</el-breadcrumb-item>
    </el-breadcrumb>
    <div class="disease-cases">

    </div>
  </div>
</template>
<script>
import MCard from '@/components/mCard'
export default {
  components: {
    MCard
  },
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
.disease {
  &-cases {
  }
}
</style>
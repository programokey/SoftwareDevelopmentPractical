<template>
  <div class="Role">
    <el-breadcrumb class="breadcrumb" separator="/">
      <el-breadcrumb-item :to="{ path: '/roleplay' }">角色扮演</el-breadcrumb-item>
      <el-breadcrumb-item>{{name}}</el-breadcrumb-item>
    </el-breadcrumb>

    <div class="head"><h5>{{name}}</h5></div>
    <ul class="workType">
      <li v-for="(item,index) in data.workType" :key="index" @click="$router.push(`/roleplay/${name}/${item}`)">{{item}}</li>
    </ul>
  </div>
</template>
<script>
export default {
  components: {},
  props: {},
  data () {
    return {
      data: {
        // name: '前台',
        workType: ['接待挂号', '病例档案的合理保存']
      }
    }
  },
  computed: {
    name () {
      return this.$route.params.name
    }
  },
  mounted () {
  },
  methods: {}
}
</script>
<style lang="scss">

</style>
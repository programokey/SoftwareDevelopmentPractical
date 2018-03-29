<template>
  <div class="Role">
    <el-breadcrumb class="breadcrumb" separator="/">
      <el-breadcrumb-item :to="{ path: '/roleplay' }">角色扮演</el-breadcrumb-item>

      <el-breadcrumb-item :to="{ path: `/roleplay/${name}`}">{{name}}</el-breadcrumb-item>
      <el-breadcrumb-item>{{workType}}</el-breadcrumb-item>
    </el-breadcrumb>

    <div class="head"><h5>{{workType}}</h5></div>
    <ul class="workTypeDescription">
      <li>描述：{{data.description}}</li>
      <li>注意事项：{{data.dosAndDonots}}</li>
      <li v-if="data.jobflow" @click="$router.push(`/`)">职能流程体验 </li>
      
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
        description: '工作类别详细描述',
        dosAndDonots: '工作类别注意事项',
        jobflow: '1'
      }
    }
  },
  computed: {
    name () {
      return this.$route.params.name
    },
    workType () {
      return this.$route.params.workType
    }

  },
  mounted () {
  },
  methods: {}
}
</script>
<style lang="scss">

</style>
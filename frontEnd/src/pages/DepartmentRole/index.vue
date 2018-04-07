<template>
  <div class="departmentRole">
    <el-breadcrumb class="breadcrumb" separator="/">
      <el-breadcrumb-item :to="{ path: '/' }">导览</el-breadcrumb-item>
      <el-breadcrumb-item :to="{path:`/department/${frontUrl}`}">{{frontUrl}}</el-breadcrumb-item>
      <el-breadcrumb-item>{{currentUrl}}</el-breadcrumb-item>
    </el-breadcrumb>
    <!-- <div class="descrip">{{data.description}}</div> -->
    <ul class="jobs">
      <li v-for="(item,index) in data.jobs" :key="index">{{item}}</li>
    </ul>

  </div>
</template>
<script>
import MCard from '@/components/MCard'
export default {
  components: {
    MCard
  },
  props: {},
  data () {
    return {
      data: {
        // description: 'xxxxxxxxxxxxxxxxxxxxxxxx',
        jobs: ['a', 'b']
      }
    }
  },
  computed: {
    frontUrl () {
      return decodeURI(this.$route.params.departmentName)
    },
    currentUrl () {
      return decodeURI(this.$route.params.roleName)
    }
  },
  mounted () {
  },
  methods: {}
}
</script>
<style lang="scss">

</style>
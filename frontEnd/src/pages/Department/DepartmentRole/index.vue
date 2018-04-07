<template>
  <div class="departmentRole">
    <el-breadcrumb class="breadcrumb" separator="/">
      <el-breadcrumb-item :to="{ path: '/' }">导览</el-breadcrumb-item>
      <el-breadcrumb-item :to="{path:`/department/${frontUrl}`}">{{frontUrl}}</el-breadcrumb-item>
      <el-breadcrumb-item>{{currentUrl}}</el-breadcrumb-item>
    </el-breadcrumb>
    <!-- <div class="descrip">{{data.description}}</div> -->
    <div class="jobs card-container">
      <m-card v-for="(item,index) in data.jobs" :key="index" :job="item"></m-card>
    </div>

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
        jobs: ['a', 'b', 'c', 'd', 'e']
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
.jobs {
  margin-top: 30px;
}
</style>
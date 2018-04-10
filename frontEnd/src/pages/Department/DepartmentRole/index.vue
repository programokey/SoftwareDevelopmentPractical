<template>
  <div class="departmentRole">
    <el-breadcrumb class="breadcrumb" separator="/">
      <el-breadcrumb-item :to="{ path: '/' }">导览</el-breadcrumb-item>
      <el-breadcrumb-item :to="{path:`/department/${frontUrl}`}">{{frontUrl}}</el-breadcrumb-item>
      <el-breadcrumb-item>{{currentUrl}}</el-breadcrumb-item>
    </el-breadcrumb>
    <!-- <div class="descrip">{{data.description}}</div> -->
    <div class="jobs card-container">
      <m-card v-for="(item,index) in jobs" :key="index" :job="item" @clickMethod="gojob" />
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
        // description: 'xxxxxxxxxxxxxxxxxxxxxxxx',
      jobs: []
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
    this.$api.getDepartmentRoleJob(this.frontUrl, this.currentUrl).then(res => {
      this.jobs = res.data
    })
  },
  methods: {
    gojob (val) {
      this.$router.push(`/roleplay/${this.currentUrl}/${val.job}`)
    }
  }
}
</script>
<style lang="scss">
.jobs {
  margin-top: 30px;
}
</style>
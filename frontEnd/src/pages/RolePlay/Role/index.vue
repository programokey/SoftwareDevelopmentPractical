<template>
  <div class="Role">
    <el-breadcrumb class="breadcrumb" separator="/">
      <el-breadcrumb-item :to="{ path: '/roleplay' }">角色扮演</el-breadcrumb-item>
      <el-breadcrumb-item>{{name}}</el-breadcrumb-item>
    </el-breadcrumb>
    <div class="role-content">
      <h1>{{name}}</h1>
      <!-- <p>{{info.description}}</p> -->
      <ul class="workType">
        <h4>角色工作</h4>
        <li class="job" v-for="(item,index) in jobs" :key="index" @click="$router.push(`/roleplay/${name}/${item}`)">{{item}}</li>
      </ul>
    </div>
  </div>
</template>
<script>
export default {
  components: {},
  props: {},
  data () {
    return {
      jobs: []
    }
  },
  computed: {
    name () {
      return this.$route.params.name
    }
  },
  mounted () {
    this.$api.getRoleJobList(this.name).then(res => {
      console.log(res)
      this.jobs = res.data
    })
  },
  methods: {}
}
</script>
<style lang="scss">
.role {
  &-content {
    border: 1px solid $green;
    border-radius: 30px;
    padding: 20px 40px;
    margin: 20px;
    h1 {
      color: $green;
    }
    & > * {
      margin-bottom: 20px;
    }
  }
}
.job {
  height: 40px;
  line-height: 30px;
  background: $green;
  color: #fff;
  padding: 5px;
  font-size: 13px;
  margin-right: 20px;
  cursor: pointer;
}
.workType {
  h4 {
    color: #999;
    margin-bottom: 10px;
  }
}
</style>
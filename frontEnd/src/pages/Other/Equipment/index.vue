<template>
  <div class="equipment">
    <el-breadcrumb class="breadcrumb" separator="/">
      <el-breadcrumb-item :to="{ path: '/' }">导览</el-breadcrumb-item>
      <el-breadcrumb-item>设备</el-breadcrumb-item>
    </el-breadcrumb>
    <div>
      <div class="name">{{data.name}}</div>
      <div class="descrip">{{data.description}}</div>
      <div class="operate">{{data.operateMethod}}</div>
      <div class="location">{{data.location}}</div>
      <div class="flow">{{data.flow}}</div>
    </div>
  </div>
</template>
<script>
export default {
  components: {},
  props: {},
  data () {
    return {
      data: {
        name: 'a',
        description: 'xx',
        operateMethod: 'xx',
        location: 'xx',
        flow: 1
      }
    }
  },
  computed: {
    currentUrl () {

    }
  },
  mounted () {
    this.$api.getEquipment(this.$route.params.id).then(res => {
      this.data = res.data
    })
  },
  methods: {}
}
</script>
<style lang="scss" scoped>

</style>
<template>
  <div class="department">
    <el-breadcrumb class="breadcrumb" separator="/">
      <el-breadcrumb-item :to="{ path: '/' }">导览</el-breadcrumb-item>
      <el-breadcrumb-item>{{$route.params.name}}</el-breadcrumb-item>
    </el-breadcrumb>
    <div class="content">
      <div class="name">科室名：{{info.name}}</div>
      <div class="structure">基础设施：{{info.basicStructure}}</div>
      <div class="function">职能：{{info.function}}</div>
      <ul class="roles">角色：
        <li class="role" v-for="(role,index) in info.roles" :key="index" @click="$router.push(`/department/${info.name}/role/${role}`)">{{role}}</li>
      </ul>
      <ul class="equipments">设备：
        <li class="equipment" v-for="(equipment,index) in info.equipments" :key="index" @click="$router.push(`/equipment/${index}`)">{{equipment}}</li>
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
      info: {
        name: '前台',
        basicStructure: '爱丽丝电话立刻返回开始的风格的快速改变的疯狂v不',
        function: '接待客人啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊',
        roles: ['前台1'],
        equipments: {'1': '桌子', '2': '椅子'}
      }
    }
  },
  computed: {},
  mounted () {},
  methods: {}
}
</script>

<style lang="scss" scoped>

</style>
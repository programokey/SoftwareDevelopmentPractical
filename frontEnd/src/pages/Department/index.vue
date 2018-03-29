<template>
  <div class="department">
    <el-breadcrumb class="breadcrumb" separator="/">
      <el-breadcrumb-item :to="{ path: '/' }">导览</el-breadcrumb-item>
      <el-breadcrumb-item>{{$route.params.name}}</el-breadcrumb-item>
    </el-breadcrumb>
    <div class="content">
      <div class="name">
        <h2 class="label">科室名：</h2>
        <p class="info">{{info.name}}</p>
      </div>
      <div class="structure">
        <h2 class="label">基础设施：</h2>
        <p class="info">{{info.basicStructure}}</p>
      </div>
      <div class="function">
        <h2 class="label">职能：</h2>
        <p class="info">{{info.function}}</p>
      </div>
      <ul class="roles">
        <h2 class="label">角色：</h2>
        <li class="role info" v-for="(role,index) in info.roles" :key="index" @click="$router.push(`/department/${info.name}/role/${role}`)">{{role}}</li>
      </ul>
      <ul class="equipments">
        <h2 class="label">设备：</h2>
        <li class="equipment info" v-for="(equipment,index) in info.equipments" :key="index" @click="$router.push(`/equipment/${index}`)">{{equipment}}</li>
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
  mounted () {

  },
  methods: {}
}
</script>

<style lang="scss" scoped>
.content {
  margin: 50px 0 0 150px;
  .label {
    color: $green;
    // margin-bottom: 10px;
  }
  & > div {
    display: flex;
    align-items: flex-end;
    margin-top: 20px;
  }
  & > ul {
    margin-top: 20px;
    .label {
      margin-bottom: 10px;
    }
    li {
      margin-left: 15px;
      cursor: pointer;
    }
  }
  .name {
    .info {
      font-size: 30px;
    }
  }
}
// .inActive {
//   cursor: pointer;
// }
</style>
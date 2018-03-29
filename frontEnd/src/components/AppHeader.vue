<template>
  <header class="header" v-if="$route.path!=='/login'">
    <p class="header-title">模拟宠物医院</p>
    <!-- @click="$router.push('/')" -->
    <el-menu :default-active="active" class="header-menu" mode="horizontal" @select="handleSelect">
      <!-- background-color="#97BDF1" text-color="#fff" active-text-color="#F3DB28" -->
      <el-menu-item index="/">个人信息</el-menu-item>

      <el-menu-item index="/test">在线测试</el-menu-item>
      <!-- <el-submenu index="2">
        <template slot="title">角色扮演</template>
        <el-menu-item index="roleplay">前台</el-menu-item>
        <el-menu-item index="roleplay">医助</el-menu-item>
        <el-menu-item index="roleplay">医师</el-menu-item>
      </el-submenu> -->
      <el-menu-item index="/learn">病例学习</el-menu-item>
      <el-menu-item index="/roleplay">角色扮演</el-menu-item>
      <el-menu-item index="/">医院导览</el-menu-item>

    </el-menu>
  </header>
</template>

<script>
export default{
  name: '',
  components: {},
  mixins: {},
  props: {
  },
  data () {
    return {
    }
  },
  computed: {
    active () {
      let path = this.$route.path
      return path
      // if (path === '/') {
      //   return path
      // } else {
      // }
    }
  },
  watch: {},
  created () {},
  mounted () {
  },
  methods: {
    handleSelect (key, keyPath) {
      this.$router.push(keyPath[0])
    }
  }
}
</script>

<style lang='scss' scoped>
.header {
  // position: relative;
  z-index: 1000;
  min-width: 1024px;
  &-menu {
    width: 100%;
  }
  &-title {
    position: absolute;
    margin-left: 20px;
    color: $green;
    font-size: 26px;
    line-height: 60px;
    z-index: 10;
    // cursor: pointer;
  }
  .el-menu--horizontal > .el-menu-item {
    float: right;
  }
}
</style>

<template>
  <div class="login">
    <h1 class="login-title">模拟宠物医院</h1>
    <div class="login-wrap">
      <p class="login-tip">请输入账号密码登陆我们的系统</p>
      <div class="login-form">
        <el-input class="login-input" v-model="account" placeholder="请输入账号"></el-input>
        <el-input type="password" class="login-input" v-model="password" placeholder="请输入密码"></el-input>
        <el-button class="login-button">登陆</el-button>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  components: {},
  props: {},
  data () {
    return {
      account: '',
      password: ''
    }
  },
  computed: {},
  mounted () {},
  methods: {}
}
</script>
<style lang="scss" scoped>
.login {
  position: relative;
  height: 100%;
  background-image: url("./../../../static/login-bg.jpg");
  background-size: cover;
  &-title {
    position: absolute;
    top: 70px;
    left: 70px;
    font-size: 80px;
    color: #fff;
  }
  &-wrap {
    position: absolute;
    right: 10%;
    top: 45%;
    box-sizing: border-box;
    width: 350px;
    padding: 20px 30px;
    border-radius: 30px;
    background: #fff;
    transform: translateY(-50%);
  }
  &-tip {
    text-align: left;
    color: #606266;
  }
  &-form {
    width: 100%;
    margin-top: 20px;
  }
  &-input {
    margin-bottom: 10px;
  }
  &-button {
    width: 100%;
    margin-bottom: 20px;
  }
}
</style>
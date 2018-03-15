<template>
  <div id="app">
    <app-header class="app-header" />
    <!-- v-show="$route.name!=='Login'"  -->
    <router-view class="app-content" />
  </div>
</template>

<script>
import AppHeader from '@/components/AppHeader'
export default {
  name: 'app',
  components: {
    AppHeader
  }
}
</script>

<style lang="scss">
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  height: 100%;
  min-width: 1024px;

  border: 1px solid #fff;
  position: relative;
  z-index: 2;
}
.app {
  &-header {
    position: fixed;
    width: 100%;
  }
  &-content {
    padding-top: 61px;
    // position: absolute;
    // top: 0;
    width: 100%;
    height: 100%;
    margin: 0 auto;
    overflow-y: auto;
    // z-index: 1;
  }
}
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
html,
body {
  width: 100%;
  height: 100%;
}
p,
h1,
h2,
h3,
span {
  font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB",
    "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
  color: #606266;
}
/* 滚动条整体部分 */

::-webkit-scrollbar {
  width: 5px;
  height: 5px;
  /* scroll轨道背景 */
  &-track {
    border-radius: 8px;
    background-color: #d8d8d8;
  }
  /* 滚动条中能上下移动的小块 */
  &-thumb {
    border-radius: 8px;
    background-color: #999;
  }
}
ul {
  list-style: none;
}
</style>

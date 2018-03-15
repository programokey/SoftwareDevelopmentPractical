<template>
  <div class="guide">
    <div class="guide-wrap">
      <div class="guide-list">
        <p class="guide-title">医院导览</p>
        <ul class="depart">
          <li class="depart-item" :class="[+isHover===1?'ishover':'']" @mouseenter="mouseen(1)" @mouseleave="mousele()">科室1</li>
          <li class="depart-item" :class="[+isHover===2?'ishover':'']" @mouseenter="mouseen(2)" @mouseleave="mousele()">科室2</li>
          <li class="depart-item" :class="[+isHover===3?'ishover':'']" @mouseenter="mouseen(3)" @mouseleave="mousele()">科室3</li>
          <li class="depart-item">科室4</li>
          <li class="depart-item">科室5</li>
          <li class="depart-item">科室6</li>
          <li class="depart-item">科室7</li>
          <li class="depart-item">科室8</li>
          <li class="depart-item">科室1</li>
          <li class="depart-item">科室2</li>
          <li class="depart-item">科室3</li>
          <li class="depart-item">科室4</li>
          <li class="depart-item">科室5</li>
          <li class="depart-item">科室6</li>
          <li class="depart-item">科室7</li>
          <li class="depart-item">科室8</li>
          <li class="depart-item">科室1</li>
          <li class="depart-item">科室2</li>
          <li class="depart-item">科室3</li>
          <li class="depart-item">科室4</li>
          <li class="depart-item">科室5</li>
          <li class="depart-item">科室6</li>
          <li class="depart-item">科室7</li>
          <li class="depart-item">科室8</li>
          <li class="depart-item">科室4</li>
          <li class="depart-item">科室5</li>
          <li class="depart-item">科室6</li>
          <li class="depart-item">科室7</li>
          <li class="depart-item">科室8</li>

        </ul>
      </div>
      <div class="guide-plan">
        <!-- <i class="el-icon-location hotspot"></i> -->
        <Hotspot :activeId="isHover" :coor="'121,121'" :uid="1" @mouseenter.native="mouseen(1)" @mouseleave.native="mousele()" />
        <Hotspot :activeId="isHover" :coor="'222,222'" :uid="2" @mouseenter.native="mouseen(2)" @mouseleave.native="mousele()" />
        <Hotspot :activeId="isHover" :coor="'333,333'" :uid="3" @mouseenter.native="mouseen(3)" @mouseleave.native="mousele()" />
        <img src="./../../../static/plan.png">
      </div>
    </div>
  </div>
</template>

<script>
import Hotspot from '@/components/Hotspot'
export default{
  name: '',
  components: {
    Hotspot
  },
  mixins: {},
  props: {},
  data () {
    return {
      isHover: -1
    }
  },
  computed: {},
  watch: {},
  created () {},
  mounted () {},
  methods: {
    mouseen (val) {
      this.isHover = val
    },
    mousele () {
      this.isHover = -1
    },
    hoverActive (val) {

    }
  }
}
</script>

<style lang='scss' scoped>
.guide {
  width: 1024px;

  &-wrap {
    display: flex;
    justify-content: space-between;
    padding-top: 30px;
    height: 100%;
  }
  &-list {
    width: 250px;
    height: 100%;
    display: flex;
    flex-direction: column;
  }
  &-title {
    font-size: 28px;
    margin: 0px 0 40px 40px;
  }
  .depart {
    // flex: 1;
    display: flex;
    flex-wrap: wrap;
    // max-height: 340px;
    overflow-y: auto;
    margin-bottom: 10px;
    &-item {
      margin: 0 30px 10px 0;
      padding: 9px 20px;
      border-radius: 15px;
      border: 1px solid #d8d8d8;
      color: #606266;
      font-size: 13px;
      cursor: pointer;
      &:hover {
        background: #ecf5ff;
        border-color: #c6e2ff;
        color: #409eff;
      }
    }
    .ishover {
      background: #ecf5ff;
      border-color: #c6e2ff;
      color: #409eff;
    }
  }
  &-plan {
    position: relative;
    // margin-top: 100px;
  }
}
</style>

<template>
  <div class="guide">
    <div class="guide-wrap">
      <div class="guide-list">
        <p class="guide-title">医院导览</p>
        <ul class="depart">
          <li v-for="(item,index) in departments" :key="index" class="depart-item" :class="[isHover===item.name ?'ishover':'']" @mouseenter="mouseen(item.name)" @mouseleave="mousele()" @click="$router.push(`/department/${item.name}`)">{{item.name}}</li>

        </ul>
      </div>
      <div class="guide-plan">
        <!-- <i class="el-icon-location hotspot"></i> -->
        <Hotspot :activeId="isHover" v-for="(item,index) in departments" :pos="item.pos" :uid="item.name" :key="index" @mouseenter.native="mouseen(item.name)" @mouseleave.native="mousele()" @click.native="$router.push(`/department/${item.name}`)" />
        <img class="guide-plan-img" src="./../../../../static/plan.jpg">
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
      isHover: '',
      departments: []
    }
  },
  computed: {},
  watch: {},
  created () {},
  mounted () {
    this.$api.getDepartmentList().then(res => {
      this.departments = res.data
    })
  },
  methods: {
    mouseen (val) {
      this.isHover = val
    },
    mousele () {
      this.isHover = ''
    }
  }
}
</script>

<style lang='scss' scoped>
.guide {
  // position:relative;
  // overflow:hidden;
  width: 1024px;

  &-wrap {
    display: flex;
    justify-content: flex-end;
    // align-items: center;
    height: 100%;
    // position:relative;
  }
  &-list {
    position: absolute;
    // height:100%;
    left: 0;
    top: 61px;
    bottom: 0;
    border: 1px solid $green;
    box-shadow: 2px 4px 3px 2px #aaa;
    width: 250px;
    display: flex;
    background: $green;
    // padding: 0 10px;
    padding-left: 40px;
    flex-direction: column;
  }
  &-title {
    font-size: 28px;
    margin-top: 20px;
    color: #fff;
    // margin: 0px 0 40px 40px;
  }
  .depart {
    margin-top: 30px;
    // flex: 1;
    display: flex;
    flex-wrap: wrap;
    // max-height: 340px;
    overflow-y: auto;
    margin-bottom: 10px;
    &-item {
      margin: 0 20px 10px 0;
      padding: 9px 20px;
      border-radius: 15px;
      // border: 1px solid #d8d8d8;
      color: #606266;
      background: #fff;
      font-size: 13px;
      cursor: pointer;
      &:hover {
        background: $yellow;
        border-color: $light-yellow;
        color: #fff;
      }
    }
    .ishover {
      background: $yellow;
      border-color: $light-yellow;
      color: #fff;
    }
  }
  &-plan {
    position: relative;
    align-self: center;
  }
}
.guide-plan-img {
  width: 750px;
}
// @media screen and (min-width: 1280px) {
//   .guide-plan {
//     margin-left: 300px;
//   }
//   .guide-plan-img {
//     width: 960px;
//   }
// }
</style>

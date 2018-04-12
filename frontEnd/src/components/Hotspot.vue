<template>
  <div class="hotspot" v-if="pos" :style="{left:cX,top:cY}">
    <i class="el-icon-location" :class="{red:isHover}"></i>
  </div>
</template>
<script>
export default {
  components: {},
  props: ['uid', 'pos', 'activeId'],
  data () {
    return {
      // uid: 1,
      // pos: '131,123'
      // activeId: 2
    }
  },
  computed: {
    cX () {
      return +this.pos.split(',')[0] + 'px'
    },
    cY () {
      return +this.pos.split(',')[1] + 'px'
    },
    isHover () {
      return this.uid === this.activeId
    }
  },
  mounted () {
  },
  methods: {}
}
</script>
<style lang="scss">
@import "./../style/vars.scss";
.hotspot {
  position: absolute;
  font-size: 35px;
  color: $green;
  cursor: pointer;
  .red {
    color: $yellow;
  }
}
</style>
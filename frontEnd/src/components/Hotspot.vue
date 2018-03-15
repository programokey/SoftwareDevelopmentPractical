<template>
  <div class="hotspot" :style="{left:cX,top:cY}">
    <i class="el-icon-location" :class="{red:isHover}"></i>
  </div>
</template>
<script>
export default {
  components: {},
  props: ['uid', 'coor', 'activeId'],
  data () {
    return {
      // uid: 1,
      // coor: '131,123'
      // activeId: 2
    }
  },
  computed: {
    cX () {
      return +this.coor.split(',')[0] + 'px'
    },
    cY () {
      return +this.coor.split(',')[1] + 'px'
    },
    isHover () {
      return +this.uid === +this.activeId
    }
  },
  mounted () {
  },
  methods: {}
}
</script>
<style lang="scss">
.hotspot {
  position: absolute;
  font-size: 25px;
  color: orange;
  cursor: pointer;
  .red {
    color: red;
  }
}
</style>
<template>
  <div class="card">
    <div class="card-background" :style="`background-image:url('./../../static/images/doctor.jpeg')`">

    </div>
    <div class="card-overlay">
      <div class="card-content">病例1</div>
    </div>
  </div>
</template>
<script>
export default {
  components: {},
  props: {},
  data () {
    return {}
  },
  computed: {},
  mounted () {},
  methods: {}
}
</script>
<style lang="scss">
.card {
  // width: 100%;
  // height: 100%;
  width: 300px;
  height: 300px;
  position: relative;
  overflow: hidden;
  &-background {
    z-index: -1;
    position: absolute;
    width: 100%;
    height: 100%;
    background-size: cover;
    &:hover {
      transition: all, 0.6s;
      transform: scale(1.2);
    }
  }
  &-overlay {
    display: flex;
    flex-direction: column;
    justify-content: center;
    height: 100%;
    opacity: 0;
    background: $green;
    transition: opacity 0.4s;
    &:hover {
      opacity: 1;
    }
  }
  &-content {
    text-align: center;
    color: #fff;
  }
}
</style>
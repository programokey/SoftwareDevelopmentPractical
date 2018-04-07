<template>
  <div class="card">
    <!-- <div class="card-background" :style="`background-image:url('./../../static/images/doctor.jpeg')`">

    </div>
    <div class="card-overlay">
      <div class="card-content">病例1</div>
    </div> -->
    <h2 @click="$emit('clickMethod',{id:info.id})">病例{{index}}</h2>
    <p>{{info.petType}}</p>
    <p>年龄：{{info.petAge}}岁</p>
  </div>
</template>
<script>
export default {
  components: {},
  props: ['info', 'index'],
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
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 300px;
  height: 300px;
  position: relative;
  overflow: hidden;
  background: $green;
  // border: 1px solid #eee;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  & > * {
    color: #fff;
  }
  h2 {
    margin-bottom: 20px;
    cursor: pointer;
  }
  // &-background {
  //   z-index: -1;
  //   position: absolute;
  //   width: 100%;
  //   height: 100%;
  //   background-size: cover;
  //   &:hover {
  //     transition: all, 0.6s;
  //     transform: scale(1.2);
  //   }
  // }
  // &-overlay {
  //   display: flex;
  //   flex-direction: column;
  //   justify-content: center;
  //   height: 100%;
  //   opacity: 0;
  //   background: $green;
  //   transition: opacity 0.4s;
  //   &:hover {
  //     opacity: 1;
  //   }
  // }
  // &-content {
  //   text-align: center;
  //   color: #fff;
  // }
}
</style>
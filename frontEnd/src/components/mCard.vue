<template>
  <div class="card">
    <!-- <div class="card-background" :style="`background-image:url('./../../../static/images/doctor.jpeg')`">

    </div>
    <div class="card-overlay">
      <div class="card-content">病例1</div>
    </div> -->
    <div class="card-content" v-if="job">
      <h2 @click="clickFunc">{{job}}
      </h2>
    </div>
    <div class="card-content" v-else>
      <h2 @click="clickFunc">病例{{index}}</h2>
      <p>{{info.petType}}</p>
      <p>年龄：{{info.petAge}}</p>
    </div>
  </div>
</template>
<script>
export default {
  components: {},
  props: ['info', 'index', 'job'],
  data () {
    return {}
  },
  computed: {},
  mounted () {},
  methods: {
    clickFunc () {
      if (this.job) {
        console.log('job')
        this.$emit('clickMethod', {job: this.job})
      } else {
        this.$emit('clickMethod', {id: this.info.id})
      }
    }
  }
}
</script>
<style lang="scss">
.card {
  // width: 100%;
  // height: 100%;
  margin: 10px;
  width: 300px;
  height: 300px;
  position: relative;
  overflow: hidden;
  background: $green;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  &-content {
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    & > * {
      color: #fff;
    }
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
<template>
  <div class="flowStep">
    <div class="flow-content" v-if="step">
      <div v-if="step.type==='Video' && step.content" class="flow-video">
        <video class="flow-video-player" :src="step.content" controls="controls" width="700px" height="568px"></video>
      </div>
      <div v-if="step.type==='Picture' && step.content" class="flow-pic" :style="{'background-image':`url(${step.content})`, 'background-size':'contain','background-repeat':'no-repeat'}">

      </div>
      <div class="flow-description" :class="step.content?'':'flow-cover'">
        <p class="flow-word">{{step.description}}</p>
        <slot></slot>
      </div>
    </div>

  </div>
</template>
<script>
export default {
  components: {},
  props: ['step'],
  data () {
    return {}
  },
  computed: {},
  mounted () {},
  methods: {}
}
</script>
<style lang="scss" scoped>
.flowStep {
  position: relative;
}
.flow {
  &-content {
    display: flex;
    // width: 846px;
    width: 100%;
    height: 100%;
    justify-content: space-between;
  }
  &-video {
    flex: 1;
    text-align: center;
    &-player {
    }
  }
  &-pic {
    flex: 1;
    height: 100%;
    img {
      width: 100%;
      height: 100%;
    }
  }
  &-description {
    width: 322px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  &-cover {
    width: 100%;
  }
  &-word {
    margin: 20px 0 0 10px;
  }
}
</style>
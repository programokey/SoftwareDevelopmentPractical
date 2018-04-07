<template>
  <div class="flowStep">
    <div class="flow-content">
      <div v-if="step.type==='video'" class="flow-video">
        <video :src="step.content" controls="controls" width="846px" height="568px"></video>
        <!-- {{step.content}} -->
      </div>
      <div v-else class="flow-pic">
        <img :src="step.content" alt="">
        <!-- {{step.content}} -->
      </div>
      <div class="flow-description">
        <p>{{step.description}}</p>
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
  }
  &-pic {
    height: 100%;
    img {
      width: 846px;
      height: 100%;
    }
  }
  &-description {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
}
</style>
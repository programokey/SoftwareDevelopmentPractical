<template>
  <div class="flow">
    <flow-step :step="currentStep" class="step">
      <div class="step-control">
        <div class="left m-button" v-if="index>0" @click="index--">上一步</div>
        <div class="right m-button" v-if="index<data.length-1" @click="index++">下一步</div>
      </div>
    </flow-step>
  </div>
</template>
<script>
import FlowStep from '@/components/FlowStep'
export default {
  components: {
    FlowStep
  },
  props: {},
  data () {
    return {
      data: [
      ],
      index: 0
    }
  },
  computed: {
    currentStep () {
      return this.data[this.index]
    }
  },
  mounted () {
    this.$api.getFlow(this.$route.params.flowId).then(res => {
      this.data = res.data
    })
  },
  methods: {
  }
}
</script>
<style lang="scss" scoped>
.step {
  height: 568px;
}
.step-control {
  position: relative;
  .left {
    position: absolute;
    left: 0;
    bottom: 0;
    margin-left: 20px;
  }
  .right {
    position: absolute;
    right: 0;
    bottom: 0;
  }
}
</style>
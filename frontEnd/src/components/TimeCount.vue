<template>
  <div class="time-count">
    <p>考试剩余时间：
      <span v-if="parseInt(count/3600)>0">{{parseInt(count/3600)}}小时</span>
      <span>{{parseInt(count/60)>=60? parseInt(count/60%60):parseInt(count/60)}}分钟</span>
      <span>{{count%60}}秒</span>
    </p>
  </div>
</template>
<script>
export default {
  components: {},
  props: ['time'],
  data () {
    return {
      count: 0,
      interval: ''
    }
  },
  computed: {},
  watch: {
    time (val) {
      this.count = val
      this.interval = setInterval(this.countDown, 1000)
    }
  },
  mounted () {
  },
  methods: {
    countDown () {
      if (this.count === 0) {
        clearInterval(this.interval)
        this.$emit('submit')
        this.$message({message: '考试结束', type: 'warning'})
      }

      this.count -= 1
    }
  }
}
</script>
<style lang="scss" scoped>
.time-count {
  position: fixed;
  right: 40px;
  background: #fff;
}
</style>
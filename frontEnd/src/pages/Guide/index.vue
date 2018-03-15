<template>
  <div class="guide">
    <div class="guide-list">
      <ul class="depart">
        <li class="depart-item">科室1</li>
        <li>科室2</li>
        <li>科室3</li>
        <li>科室4</li>
        <li>科室5</li>
        <li>科室6</li>
        <li>科室7</li>
        <li>科室8</li>

      </ul>
    </div>
    <div class="guide-plan"></div>

  </div>
</template>

<script>
import AppHeader from '@/components/AppHeader'
export default{
  name: '',
  components: {
    AppHeader
  },
  mixins: {},
  props: {},
  data () {
    return {}
  },
  computed: {},
  watch: {},
  created () {},
  mounted () {},
  methods: {}
}
</script>

<style lang='scss' scoped>
.guide {
  width: 1024px;
  &-list {
  }
  .depart {
    &-item {
    }
  }
}
</style>

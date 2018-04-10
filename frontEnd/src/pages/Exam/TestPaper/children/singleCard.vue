<template>
  <div class="single-card">
    <div class="single-card-title">{{order}}. {{subject.problem}}</div>
    <el-radio class="single-card-radio" v-for="(choice,key,index) in subject.choice" :key="key" v-model="radio" :label="+key" @change="emitChange">{{`${String.fromCharCode((65+index))}`}} {{choice}}</el-radio>
  </div>
</template>
<script>
export default {
  components: {},
  props: ['subject', 'order', 'selected'],
  data () {
    return {
      radio: ''
    }
  },
  computed: {},
  mounted () {
    if (this.selected) {
      this.radio = this.selected[0]
    }
  },
  methods: {
    emitChange () {
      this.$emit('selectOpration', {radio: this.radio, problemId: this.subject.problemId})
    }
  }
}
</script>
<style lang="scss">
.single-card {
  margin-bottom: 20px;
  border-bottom: 1px solid #eee;
  padding-bottom: 10px;

  &-title {
    font-size: 18px;
    margin-bottom: 10px;
  }
}
</style>
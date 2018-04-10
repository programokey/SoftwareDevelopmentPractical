<template>
  <div class="multiple-card">
    <div class="multiple-card-title">{{order}}. {{subject.problem}}</div>
    <el-checkbox-group v-model="checkList" @change="emitChange">
      <el-checkbox v-for="(item, key, index) in subject.choice" :key="key" :label="+key">{{`${String.fromCharCode((65+index))} ${item}`}}</el-checkbox>

    </el-checkbox-group>
  </div>
</template>
<script>
export default {
  components: {},
  props: ['subject', 'order', 'selected'],
  data () {
    return {
      checkList: []
    }
  },
  computed: {},
  mounted () {
    if (this.selected) {
      this.checkList = this.selected
    }
  },
  methods: {
    emitChange () {
      this.$emit('selectOpration', {radio: this.checkList, problemId: this.subject.problemId})
    }
  }
}
</script>
<style lang="scss">
.multiple-card {
  margin-bottom: 20px;
  border-bottom: 1px solid #eee;
  padding-bottom: 10px;
  &-title {
    font-size: 18px;
    margin-bottom: 10px;
  }
}
</style>
<template>
  <div class="paper">
    <div class=paper-wrap>
      <!-- <div>剩余时间{{data.remainingTime/60}}分钟</div> -->
      <div class="single" v-if="data.single && data.single.length!==0">
        <h3>单选题</h3>
        <div class="question-wrap">
          <single-card v-for="(subject, index) in data.single" :key="index" :subject="subject" :order="index+1" @selectOpration="selectOperation" :selected="selected[subject.problemId]" />
        </div>
      </div>
      <div class="multiple" v-if="data.multiple && data.multiple.length!==0">
        <h3>多选题</h3>
        <div class="question-wrap">
          <multiple-card v-for="(subject, index) in data.multiple" :key="index" :subject="subject" :order="index+1" @selectOpration="selectOperation" :selected="selected[subject.problemId]" />
        </div>
      </div>
      <div class="button-wrap">
        <el-button @click="saveResult">保存</el-button>
        <el-button @click="submit" type="primary" class="primary-button">提交</el-button>
      </div>
    </div>
  </div>
</template>
<script>
import SingleCard from './children/singleCard'
import MultipleCard from './children/multipleCard'
export default {
  components: {
    SingleCard,
    MultipleCard
  },
  props: {},
  data () {
    return {
      data: {},
      selected: {}
    }
  },
  computed: {},
  created () {
    this.$api.getTestQuestions(this.$route.params.id).then(res => {
      this.data = res.data
      // 对保存的选项处理
      this.selected = this.data.selected
    })
  },
  mounted () {

  },
  methods: {
    selectOperation (val) {
      if (val.radio.constructor !== Array) {
        val.radio = [val.radio]
      }
      this.selected[val.problemId] = val.radio
    },
    saveResult () {
      let answer = window.JSON.stringify(this.selected)
      this.$api.postTestResult({testId: this.$route.params.id, answer: answer}).then(res => {
        this.$message({message: '保存成功'})
      })
    },
    submit () {
      let answer = window.JSON.stringify(this.selected)
      this.$api.postTestResult({testId: this.$route.params.id, answer: answer}).then(res => {
        if (res.code === 1000) {
          this.$message({message: '试卷提交成功'})
          this.$router.push('/test')
        }
      })
    }
  }
}
</script>
<style lang="scss">
.paper {
  &-wrap {
    padding-top: 30px;
    width: 800px;
    margin: 0 auto;
  }
  h3 {
    margin-bottom: 30px;
  }
  .question-wrap {
    // border: 1px solid $green;
    border-radius: 20px;
    padding: 20px;
    margin-bottom: 40px;
  }
  .el-radio {
    display: block;
    margin: 0 0 10px 0;
  }
  .el-checkbox {
    display: block;
    margin: 0 0 10px 0;
  }
  .button-wrap {
    margin-bottom: 30px;
  }
}
.primary-button {
  span {
    color: #fff;
  }
}
</style>
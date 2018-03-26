<template>
  <el-row class="case" :gutter="20">
    <el-col :span="18" class="case-left">
      <el-input class="case-search" placeholder="请输入搜索内容" prefix-icon="el-icon-search" v-model="search">
      </el-input>
      <div class="case-cell-wrap">
        <case-cell v-for="(item,index) in caseList" :key="index" :title="index" :data="item" />
      </div>
    </el-col>
    <el-col :span="6" class="case-right">
      <classification />
    </el-col>
  </el-row>
</template>
<script>
import Classification from './children/classification'
import CaseCell from './children/caseCell'
export default {
  components: {
    Classification, CaseCell
  },
  props: {},
  data () {
    return {
      search: '',
      caseList: {
        '分类1': ['病1', '病2', '病3', '病1', '病2', '病3', '病1', '病2', '病3', '病1', '病2', '病3', '病1', '病2', '病3', '病1', '病2', '病3'],
        '分类2': ['病1', '病2', '病3', '病1', '病2', '病3', '病1', '病2', '病3', '病1', '病2', '病3', '病1', '病2', '病3', '病1', '病2', '病3'],
        '分类3': ['病1', '病2', '病3', '病1', '病2', '病3', '病1', '病2', '病3', '病1', '病2', '病3', '病1', '病2', '病3', '病1', '病2', '病3']
      }
    }
  },
  computed: {},
  mounted () {},
  methods: {}
}
</script>
<style lang="scss">
.case {
  padding-left: 40px !important;
  padding-right: 40px !important;
  overflow: hidden;
  &-left {
    height: 100%;
    display: flex;
    flex-direction: column;
    // padding-left: 40px !important;
  }
  &-right {
    height: 100%;
  }
  &-search {
    margin-top: 30px;
  }
  &-cell {
    &-wrap {
      overflow-y: scroll;
      flex: 1;
    }
  }
}
</style>
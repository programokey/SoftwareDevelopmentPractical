<template>
  <el-row class="case" :gutter="20">
    <el-col :span="20" class="case-left">
      <!-- <el-input class="case-search" placeholder="请输入搜索内容" prefix-icon="el-icon-search" v-model="search">
      </el-input> -->
      <div class="case-cell-wrap">
        <case-cell v-for="(item,index) in caseList" :key="index" :title="index" :data="item" />
      </div>
    </el-col>
    <el-col :span="4" class="case-right">
      <classification :classifyList="Object.keys(caseList)" />
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
      caseList: {}
    }
  },
  computed: {},
  mounted () {
    this.$api.getDisCategoryList().then(res => {
      this.caseList = res.data
    })
  },
  methods: {}
}
</script>
<style lang="scss">
.case {
  padding-left: 40px !important;
  padding-right: 0 !important;
  margin: 0 !important;
  overflow: hidden;
  &-left {
    height: 100%;
    display: flex;
    flex-direction: column;
    padding-right: 0 !important;
    // padding-left: 40px !important;
  }
  &-right {
    height: 100%;
    background: $green;
    padding-right: 0 !important;
  }
  &-search {
    margin: 30px 20px 0 0;
    // padding: 0 20px;
    width: auto;
  }
  &-cell {
    &-wrap {
      overflow-y: scroll;
      flex: 1;
    }
  }
}
</style>
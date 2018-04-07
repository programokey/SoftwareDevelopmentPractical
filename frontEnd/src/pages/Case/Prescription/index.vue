<template>
  <div class="case">
    <el-breadcrumb class="breadcrumb" separator="/">
      <el-breadcrumb-item :to="{ path: '/learn' }">病例学习</el-breadcrumb-item>
      <el-breadcrumb-item :to="{ path: `/case/${diseaseName}` }">{{diseaseName}}</el-breadcrumb-item>
      <el-breadcrumb-item>{{caseId}}</el-breadcrumb-item>

    </el-breadcrumb>
    <div>
      <el-form ref="form" :model="form" label-width="80px" disabled=true label-position=left>
    
        <el-form-item label="处方描述">
          <el-input v-model="data.description"></el-input>
        </el-form-item>

        
      </el-form>
      <div>本处方所用药品如下：</div>
      <el-collapse class='info' v-model="activeNames" @change="handleChange">
        <el-collapse-item v-for="(item,index) in data.medicines" :key="index" :title="item.name" :name="index">
          <div>approvalNumber: {{item.approvalNumber}}</div>
          <div>unit: {{item.unit}}</div>
          <div>name: {{item.name}}</div>
        </el-collapse-item>
        
      </el-collapse>
      
      
    </div>
  </div>
</template>
<script>
export default {
  components: {},
  props: {},
  data () {
    return {
      data: {
        description: '用于治疗。。。的处方',
        medicines: [{
          'approvalNumber': '1111111',
          'unit': '2',
          'name': '黄连上清片'

        }, {
          'approvalNumber': '2222222',
          'unit': '3',
          'name': '感冒灵'

        }]
      }
    }
  },
  computed: {
    id () {
      return this.$route.params.item
    }
  },
  mounted () {},
  methods: {}
}
</script>
<style lang="scss" scoped>
.case{
  display: block;
  width: 500px;
}
.pres{
  margin-right: 10px;
}
.info{
  margin-bottom: 20px;
}
.left{
  float:right;
}

</style>
<template>
  <div class="case">
    <el-breadcrumb class="breadcrumb" separator="/">
      <el-breadcrumb-item :to="{ path: '/learn' }">病例学习</el-breadcrumb-item>
      <el-breadcrumb-item :to="{ path: `/case/${diseaseName}` }">{{diseaseName}}</el-breadcrumb-item>
      <el-breadcrumb-item>{{caseId}}</el-breadcrumb-item>

    </el-breadcrumb>
    <div class="case-content">
      <el-form ref="form" :model="form" label-width="80px" :disabled="true" label-position=left>

        <el-form-item label="医生">
          <el-input v-model="form.doctor"></el-input>
        </el-form-item>
        <el-form-item label="宠物类型">
          <el-input v-model="form.petType"></el-input>
        </el-form-item>
        <el-form-item label="宠物年龄">
          <el-input v-model="form.petAge"></el-input>
        </el-form-item>
        <el-form-item label="宠物性别">
          <el-input v-model="form.petGender"></el-input>
        </el-form-item>
        <el-form-item label="医院部门">
          <el-input v-model="form.department"></el-input>
        </el-form-item>
        <el-form-item label="病种">
          <el-input v-model="form.disease"></el-input>
        </el-form-item>

      </el-form>
      <el-collapse class='info' v-model="activeNames">
        <el-collapse-item title="症状" name="1">
          <div>{{form.symptom}}</div>
        </el-collapse-item>
        <el-collapse-item title="诊断结果" name="2">
          <div>{{form.diagnosis}}</div>
        </el-collapse-item>
        <el-collapse-item title="治疗结果" name="3">
          <div>{{form.treatment}}</div>
        </el-collapse-item>
        <el-collapse-item title="处方" name="4">
          <div>
            <span class="pres" v-for="(item,index) in form.prescription" :key="index" @click="$router.push(`/prescription/${item}`)">{{item}}</span>
          </div>
        </el-collapse-item>
      </el-collapse>

      <el-button v-if="form.flow" class='left' type="primary" round @click="getFlow">流程体验</el-button>

    </div>
  </div>
</template>
<script>
export default {
  components: {},
  props: {},
  data () {
    return {
      form: {
      },
      activeNames: []
    }
  },
  computed: {
    diseaseName () {
      return this.$route.params.diseaseName
    },
    caseId () {
      return this.$route.params.caseId
    }
  },
  mounted () {
    this.$api.getCaseInfo(this.caseId).then(res => {
      this.form = res.data
    })
  },
  methods: {
    getFlow () {
      this.$router.push(`/flow/${this.form.flow}`)
    }
  }
}
</script>
<style lang="scss" scoped>
.case {
  &-content {
    width: 500px;

    margin: 0 auto;
  }
}
.pres {
  margin-right: 10px;
  cursor: pointer;
}
.info {
  margin-bottom: 20px;
}
.left {
  float: right;
}
</style>
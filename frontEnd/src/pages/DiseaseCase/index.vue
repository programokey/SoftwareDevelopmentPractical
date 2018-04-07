<template>
  <div class="case">
    <el-breadcrumb class="breadcrumb" separator="/">
      <el-breadcrumb-item :to="{ path: '/learn' }">病例学习</el-breadcrumb-item>
      <el-breadcrumb-item>{{diseaseName}}</el-breadcrumb-item>
      <el-breadcrumb-item>{{caseId}}</el-breadcrumb-item>

    </el-breadcrumb>
    <div>
      <div>doctor</div>
      <div>petType</div>
      <div>petAge</div>
      <div>petGender</div>
      <div>department</div>
      <div>disease</div>
      <div>symptom</div>
      <div>examinationResult</div>
      <div>diagnosis</div>
      <div>treatment</div>
      <div>operations</div>
      <div>prescriptions</div>
      <div>flow</div>
    </div>
  </div>
</template>
<script>
export default {
  components: {},
  props: {},
  data () {
    return {}
  },
  computed: {
    diseaseName () {
      return this.$route.params.diseaseName
    },
    caseId () {
      return this.$route.params.caseId
    }
  },
  mounted () {},
  methods: {}
}
</script>
<style lang="scss" scoped>

</style>
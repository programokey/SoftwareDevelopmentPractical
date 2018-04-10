<template>
  <div class="disease">
    <el-breadcrumb class="breadcrumb" separator="/">
      <el-breadcrumb-item :to="{ path: '/learn' }">病例学习</el-breadcrumb-item>
      <el-breadcrumb-item>{{diseaseName}}</el-breadcrumb-item>
    </el-breadcrumb>
    <div class="disease-cases card-container">
      <m-card class="disease-cases-item " v-for="(item,index) in cases" :key="index" :info="item" :index="index+1" @clickMethod="findCase"></m-card>
    </div>
    <div v-if="cases.length===0">暂无病例</div>
  </div>
</template>
<script>
import MCard from '@/components/MCard'
export default {
  components: {
    MCard
  },
  props: {},
  data () {
    return {
      cases: []
    }
  },
  computed: {
    diseaseName () {
      return this.$route.params.diseaseName
    }
  },
  mounted () {
    this.$api.getCaseList(this.diseaseName).then((res) => {
      this.cases = res.data
    })
  },
  methods: {
    findCase (val) {
      console.log(val)
      this.$router.push(`${this.$route.path}/${val.id}`)
    }
  }
}
</script>
<style lang="scss">
.disease {
  &-cases {
    margin-top: 30px;
  }
}
</style>
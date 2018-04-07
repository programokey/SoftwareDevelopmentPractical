<template>
  <div class="disease">
    <el-breadcrumb class="breadcrumb" separator="/">
      <el-breadcrumb-item :to="{ path: '/learn' }">病例学习</el-breadcrumb-item>
      <el-breadcrumb-item>{{diseaseName}}</el-breadcrumb-item>
    </el-breadcrumb>
    <div class="disease-cases card-container">
      <m-card class="disease-cases-item " v-for="(item,index) in cases" :key="index" :info="item" :index="index+1" @clickMethod="findCase"></m-card>
    </div>
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
      cases: [
        // {'id': 1, 'petType': '哈士奇', 'petAge': 2},
        {'id': 2, 'petType': '哈士奇', 'petAge': 3},
        {'id': 1, 'petType': '哈士奇', 'petAge': 2},
        {'id': 2, 'petType': '哈士奇', 'petAge': 3},
        {'id': 1, 'petType': '哈士奇', 'petAge': 2},
        {'id': 2, 'petType': '哈士奇', 'petAge': 3}
      ]
    }
  },
  computed: {
    diseaseName () {
      return this.$route.params.diseaseName
    }
  },
  mounted () {
    this.$api.getCaseList(this.diseaseName).then((res) => {
      this.cases = res.data.data
    })
  },
  methods: {
    findCase (val) {
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
<template>
  <div class="departmentRole">科室角色
    <div class="descrip">{{data.description}}</div>
    <ul class="jobs">
      <li v-for="(item,index) in data.jobs" :key="index">{{item}}</li>
    </ul>
  </div>
</template>
<script>
export default {
  components: {},
  props: {},
  data () {
    return {
      data: {
        description: 'xxxxxxxxxxxxxxxxxxxxxxxx',
        jobs: ['a', 'b']
      }
    }
  },
  computed: {},
  mounted () {},
  methods: {}
}
</script>
<style lang="scss">

</style>
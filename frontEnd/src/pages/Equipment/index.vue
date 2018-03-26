<template>
  <div class="equipment">
    <div class="name">{{data.name}}</div>
    <div class="descrip">{{data.description}}</div>
    <div class="operate">{{data.operateMethod}}</div>
    <div class="location">{{data.location}}</div>
    <div class="flow">{{data.flow}}</div>
  </div>
</template>
<script>
export default {
  components: {},
  props: {},
  data () {
    return {
      data: {
        name: 'a',
        description: 'xx',
        operateMethod: 'xx',
        location: 'xx',
        flow: 1
      }
    }
  },
  computed: {},
  mounted () {},
  methods: {}
}
</script>
<style lang="scss" scoped>

</style>
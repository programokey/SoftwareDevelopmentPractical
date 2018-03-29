<template>
  <div>
    <div>角色扮演</div>
    <div>
      <!-- portfolio section -->
      <section id="works" class="works section no-padding">
        <div class="container-fluid">
          <div class="row no-gutter">
            <el-row>
              <!-- v-for 循环显示三个角色 -->
              <el-col :span="8" v-for="(role,index) in roles" :key="index" >
                <div class="grid-content bg-purple work"> <a  @click="$router.push(`/roleplay/${role.name}`)" class="work-box"> <img :src="role.imgUrl" alt="">
                  <div class="overlay">
                    <div class="overlay-caption">
                      <h5>{{role.name}}</h5>
                      <p><i class="fa fa-search-plus fa-2x"></i></p>
                    </div>
                  </div>
                </a></div>
              </el-col>

              
            </el-row>  
          </div>
        </div>
      </section>
    </div>
  </div>
</template>
<script>
import AppHeader from '@/components/AppHeader'
export default {
  components: {
    AppHeader
  },
  props: {},
  data () {
    return {
      roles: [
        {name: '前台', imgUrl: './../../images/doctor.jpeg'},
        {name: '医助', imgUrl: './../../images/doctor.jpeg'},
        {name: '医师', imgUrl: './../../images/doctor.jpeg'}
      ]
    }
  },
  computed: {},
  mounted () {},
  methods: {}
}
</script>
<style>
@import "./../../style/main.css";

</style>
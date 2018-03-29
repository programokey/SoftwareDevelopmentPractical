<template>
  <div>
    <div>角色扮演</div>
    <div>
      <!-- portfolio section -->
      <section id="works" class="works section no-padding">
        <div class="container-fluid">
          <div class="row no-gutter">
            <el-row>
              <el-col :span="8">
                <div class="grid-content bg-purple work"> <a href="./../../images/doctor.jpeg" class="work-box"> <img src="./../../images/doctor.jpeg" alt="">
                  <div class="overlay">
                    <div class="overlay-caption">
                      <h5>前台</h5>
                      <p><i class="fa fa-search-plus fa-2x"></i></p>
                    </div>
                  </div>
                </a></div>
              </el-col>
              <el-col :span="8">
                <div class="grid-content bg-purple work"> <a href="./../../images/doctor.jpeg" class="work-box"> <img src="./../../images/doctor.jpeg" alt="">
                  <div class="overlay">
                    <div class="overlay-caption">
                      <h5>医助</h5>
                      <p><i class="fa fa-search-plus fa-2x"></i></p>
                    </div>
                  </div>
                </a></div>
              </el-col>
              <el-col :span="8">
                <div class="grid-content bg-purple-light work"> <a href="./../../images/doctor.jpeg" class="work-box"> <img src="./../../images/doctor.jpeg" alt="">
                  <div class="overlay">
                    <div class="overlay-caption">
                      <h5>医师</h5>
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
    return {}
  },
  computed: {},
  mounted () {},
  methods: {}
}
</script>
<style>
@import "./../../style/main.css";

</style>
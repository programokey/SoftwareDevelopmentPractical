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
              <el-col :span="8" v-for="(role,index) in roles" :key="index">
                <div class="grid-content bg-purple work">
                  <a @click="$router.push(`/roleplay/${role.name}`)" class="work-box"> <img :src="role.imgUrl" alt="">
                    <div class="overlay">
                      <div class="overlay-caption">
                        <h5>{{role.name}}</h5>
                        <p>
                          <i class="fa fa-search-plus fa-2x"></i>
                        </p>
                      </div>
                    </div>
                  </a>
                </div>
              </el-col>

            </el-row>
          </div>
        </div>
      </section>
    </div>
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
<style lang="scss">
/* @import "./../../style/main.css"; */

/* ------------------------------------------------------------------------------
	Works
-------------------------------------------------------------------------------*/
.work {
  -moz-box-shadow: 0 0 0 1px #fff;
  -webkit-box-shadow: 0 0 0 1px #fff;
  box-shadow: 0 0 0 1px #fff;

  overflow: hidden;
  position: relative;
}
.work img {
  width: 100%;
  height: 100%;
}
.work .overlay {
  background: $green;
  height: 100%;
  left: 0;
  opacity: 0;
  position: absolute;
  top: 0;
  width: 100%;
  -moz-transition: opacity, 0.3s;
  -o-transition: opacity, 0.3s;
  -webkit-transition: opacity, 0.3s;
  transition: opacity, 0.3s;
}
.work .overlay-caption {
  position: absolute;
  text-align: center;
  top: 50%;
  width: 100%;
  -moz-transform: translateY(-50%);
  -ms-transform: translateY(-50%);
  -webkit-transform: translateY(-50%);
  transform: translateY(-50%);
}
.work h5,
.work p,
.work img {
  -moz-transition: all, 0.5s;
  -o-transition: all, 0.5s;
  -webkit-transition: all, 0.5s;
  transition: all, 0.5s;
}
.work h5,
.work p {
  color: #fff;
  margin: 0;
  opacity: 0;
}
.work h5 {
  margin-bottom: 5px;
  -moz-transform: translate3d(0, -200%, 0);
  -ms-transform: translate3d(0, -200%, 0);
  -webkit-transform: translate3d(0, -200%, 0);
  transform: translate3d(0, -200%, 0);
}
.work p {
  -moz-transform: translate3d(0, 200%, 0);
  -ms-transform: translate3d(0, 200%, 0);
  -webkit-transform: translate3d(0, 200%, 0);
  transform: translate3d(0, 200%, 0);
}

.work-box:hover img {
  -moz-transform: scale(1.2);
  -ms-transform: scale(1.2);
  -webkit-transform: scale(1.2);
  transform: scale(1.2);
}
.work-box:hover .overlay {
  opacity: 1;
}
.work-box:hover .overlay h5,
.work-box:hover .overlay p {
  opacity: 1;
  -moz-transform: translate3d(0, 0, 0);
  -ms-transform: translate3d(0, 0, 0);
  -webkit-transform: translate3d(0, 0, 0);
  transform: translate3d(0, 0, 0);
}
.flex-control-paging li a {
  background: rgba(255, 255, 255, 0) none repeat scroll 0 0;
}

.flex-control-paging li a.flex-active {
  background: rgba(255, 255, 255, 0) none repeat scroll 0 0;
}

/* ------------------------------------------------------------------------------
	Work animation
-------------------------------------------------------------------------------*/
.work:nth-child(1) {
  -moz-animation-delay: 0.1s;
  -webkit-animation-delay: 0.1s;
  animation-delay: 0.1s;
}
.work:nth-child(2) {
  -moz-animation-delay: 0.2s;
  -webkit-animation-delay: 0.2s;
  animation-delay: 0.2s;
}
.work:nth-child(3) {
  -moz-animation-delay: 0.3s;
  -webkit-animation-delay: 0.3s;
  animation-delay: 0.3s;
}
.work:nth-child(4) {
  -moz-animation-delay: 0.4s;
  -webkit-animation-delay: 0.4s;
  animation-delay: 0.4s;
}
.work:nth-child(5) {
  -moz-animation-delay: 0.8s;
  -webkit-animation-delay: 0.8s;
  animation-delay: 0.8s;
}
.work:nth-child(6) {
  -moz-animation-delay: 0.7s;
  -webkit-animation-delay: 0.7s;
  animation-delay: 0.7s;
}
.work:nth-child(7) {
  -moz-animation-delay: 0.6s;
  -webkit-animation-delay: 0.6s;
  animation-delay: 0.6s;
}
.work:nth-child(8) {
  -moz-animation-delay: 0.5s;
  -webkit-animation-delay: 0.5s;
  animation-delay: 0.5s;
}

.animated {
  visibility: visible;
}
</style>
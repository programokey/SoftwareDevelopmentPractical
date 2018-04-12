<template>
  <div class="Role">
    <el-breadcrumb class="breadcrumb" separator="/">
      <el-breadcrumb-item :to="{ path: '/roleplay' }">角色扮演</el-breadcrumb-item>

      <el-breadcrumb-item :to="{ path: `/roleplay/${name}`}">{{name}}</el-breadcrumb-item>
      <el-breadcrumb-item>{{workType}}</el-breadcrumb-item>
    </el-breadcrumb>

    <!--新加入样式-->
    <div class="top-box">
      <div class="wrap">
        <div class="content-top">
          <h1>{{workType}}</h1>

          <div class="grid_6">
            <div class="box-4 clearfix">
              <img src="/src/images/pic11.jpg" alt="" class="img-ind">
              <div class="extra-wrap">
                <div class="inside">
                  <h3>描述:</h3>
                  <div class="margin">
                    <span class="quote"></span>{{data.description}}”</div>
                  <span class="arrow"></span>

                  <h3>注意事项:</h3>
                  <div>
                    <span class="quote"></span>{{data.dosAndDonots}}”</div>
                  <span class="arrow"></span>
                </div>

              </div>
            </div>
          </div>

          <div class="right a-hov" v-if="data.jobflow" @click="$router.push(`/flow/${data.jobflow}`)">职能流程体验</div>
        </div>
      </div>

      <div class="clear"></div>
    </div>
  </div>

  <!-- <div>
      <ul class="workTypeDescription">
        <li>描述：{{data.description}}</li>
        <li>注意事项：{{data.dosAndDonots}}</li>
        <li v-if="data.jobflow" @click="$router.push(`/`)">职能流程体验 </li>
        
      </ul>
    </div>
    </div> -->
</template>
<script>
export default {
  components: {},
  props: {},
  data () {
    return {
      data: {

      }
    }
  },
  computed: {
    name () {
      return this.$route.params.name
    },
    workType () {
      return this.$route.params.workType
    }

  },
  mounted () {
    this.$api.getRoleJobInfo(this.name, this.workType).then(res => {
      this.data = res.data
    })
  },
  methods: {}
}
</script>
<style lang="scss">
.right {
  text-align: right;
}
.margin {
  margin-bottom: 30px;
}
.top-box {
  background: url(./../../../../static/images/bg1.jpg);
  box-shadow: inset 0px 10px 60px 0px rgba(0, 0, 0, 0.15);
}
.wrap {
  width: 80%;
  margin: 0 auto;
  -moz-transition: all 0.2s linear;
  -webkit-transition: all 0.2s linear;
  -o-transition: all 0.2s linear;
  -ms-transition: all 0.2s linear;
}
.content-top {
  padding: 6% 0 6%;
  h1 {
    margin-bottom: 30px;
  }
}
/*--about--*/
.box-4 .inside {
  border: 1px solid #ddd;
  padding: 25px 28px 28px;
  position: relative;
  margin-left: 10px;
  background: #fff;
}
.inside h3 {
  color: #333;
  font-size: 1.3em;
  font-family: "caviar_dreamsregular";
  padding-bottom: 10px;
}
.arrow {
  position: absolute;
  width: 17px;
  height: 26px;
  background: url("./../../../../static/images/arrow-1.png") 0 0 no-repeat;
  left: -11px;
  top: 19px;
}
.img-ind {
  float: left;
  margin-right: 20px;
  width: 20%;
}
.grid_6 {
  margin-bottom: 2%;
}
.quote {
  display: inline-block;
  background: url(./../../../../static/images/quote.png) 0 bottom no-repeat;
  width: 16px;
  height: 17px;
  padding-right: 6px;
  margin-left: 3px;
}
.a-hov {
  color: #888;
  font-family: "caviar_dreamsregular";
  font-size: 1em;
  line-height: 1.5em;
  cursor: pointer;
}
.a-hov:hover {
  color: $green;
}
.about-top {
  padding-bottom: 4%;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
  line-height: 0;
}
.extra-wrap {
  overflow: hidden;
}
</style>
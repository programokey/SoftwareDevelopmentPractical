<template>
  <div class="department">
    <el-breadcrumb class="breadcrumb" separator="/">
      <el-breadcrumb-item :to="{ path: '/' }">导览</el-breadcrumb-item>
      <el-breadcrumb-item>{{name}}</el-breadcrumb-item>
    </el-breadcrumb>
    <el-container>
      <el-aside width="400px"><img src="./../../images/4.png"  alt=""></el-aside>
      <el-main>
        <div class="inside">
          <div class="content">
            <div class="name">
              <h2 class="label" style="float:left">科室名：</h2>
              <p class="info" style="float:left">{{info.name}}</p>
              <div class="clear"></div>
            </div>
            <div class="structure">
              <h2 class="label" style="float:left">基础设施：</h2>
              <p class="info" style="float:left">{{info.basicStructure}}</p>
              <div class="clear"></div>
            </div>
            <div class="function">
              <h2 class="label" style="float:left">职能：</h2>
              <p class="info" style="float:left">{{info.function}}</p>
              <div class="clear"></div>
            </div>
            <ul class="roles">
              <h2 class="label">角色：</h2>
              <li class="role info" v-for="(role,index) in info.roles" :key="index" @click="$router.push(`/department/${info.name}/role/${role}`)">{{role}}</li>
            </ul>
            <ul class="equipments">
              <h2 class="label">设备：</h2>
              <li class="equipment info" v-for="(equipment,index) in info.equipments" :key="index" @click="$router.push(`/equipment/${index}`)">{{equipment}}</li>
            </ul>
            <span class="arrow"></span>
          </div>
        </div>
          <!-- </div>
                <h3>描述:</h3>
                <div class="margin"><span class="quote"></span>{{data.description}}”</div>
                <span class="arrow"></span>
                
                <h3>注意事项:</h3>
                <div><span class="quote"></span>{{data.dosAndDonots}}”</div>
                <span class="arrow"></span> -->
        
        

      </el-main>
    </el-container>

    
  </div>
</template>
<script>
export default {
  components: {},
  props: {},
  data () {
    return {
      info: {
        name: '前台',
        basicStructure: '爱丽丝电话立刻返回开始的风格的快速改变的疯狂v不',
        function: '接待客人啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊',
        roles: ['前台1'],
        equipments: {'1': '桌子', '2': '椅子'}
      }
    }
  },
  computed: {
    name () {
      return this.$route.params.name
    }
  },
  mounted () {
    this.$api.getDepartmentInfo(name).then(res => {
      console.log(res)
    })
  },
  methods: {}
}
</script>

<style lang="scss" scoped>

//引入
.inside {
	border: 1px solid #ddd;
	padding: 25px 28px 28px;
	position: relative;
	margin-left: 10px;
	background: #FFF;
}

.arrow {
	position: absolute;
	width: 17px;
	height: 26px;
	background: url(./../../images/arrow-1.png) 0 0 no-repeat;
	left: -11px;
	top: 19px;	
}
//引出
.content {
  //margin: 50px 0 0 150px;
  postion:relative;
  width:100%;
  .label {
    
    width:20%;
    color: $green;
    font-size:1em;
  
    // padding-bottom: 1em;
    position: relative;
    // margin-bottom: 10px;

  }
  .info {
  width:80%;
    font-size: 1em;
  }
  & > div {
    display: flex;
    align-items: flex-end;
    margin-top: 20px;
  }
  & > ul {
    margin-top: 20px;
    .label {
      margin-bottom: 10px;
    }
    li {
      margin-left: 15px;
      cursor: pointer;
    }
  }

  

}
// .inActive {
//   cursor: pointer;
// }
</style>
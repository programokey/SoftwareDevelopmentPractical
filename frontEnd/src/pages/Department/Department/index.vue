<template>
  <div class="department">
    <el-breadcrumb class="breadcrumb" separator="/">
      <el-breadcrumb-item :to="{ path: '/' }">导览</el-breadcrumb-item>
      <el-breadcrumb-item>{{name}}</el-breadcrumb-item>
    </el-breadcrumb>
    <el-container>
      <el-aside width="400px"><img class="department-image" src="./../../../../static/images/4.png" alt=""></el-aside>
      <el-main>
        <div class="inside">
          <div class="content">
            <div class="name">
              <h2 class="label">科室名：</h2>
              <p class="info">{{info.name}}</p>
            </div>
            <div class="structure">
              <h2 class="label">基础设施：</h2>
              <p class="info">{{info.basicStructure}}</p>
            </div>
            <div class="function">
              <h2 class="label">职能：</h2>
              <p class="info">{{info.function}}</p>
            </div>
            <ul class="roles">
              <h2 class="label">角色：</h2>
              <li class="role info" v-for="(role,index) in info.roles" :key="index" @click="$router.push(`/department/${name}/role/${role}`)">{{role}}</li>
            </ul>
            <ul class="equipments">
              <h2 class="label">设备：</h2>
              <li class="equipment info" v-for="(equipment,index) in info.equipments" :key="index" @click="chooseEquipment(index)">{{equipment}}</li>
              <!-- @click="$router.push(`/equipment/${index}`)" -->
            </ul>
            <el-dialog
              :title="facility.name"
              :visible.sync="centerDialogVisible"
              width="30%"
              center>
              <span>
                <div>描述信息：  {{facility.description}}</div>
                <div>操作方法：  {{facility.operateMethod}}</div>
                <div>位置：     {{facility.location}}</div>
              </span>
              <span slot="footer" class="dialog-footer">
                <!-- <el-button @click="centerDialogVisible = false">取 消</el-button> -->
                <el-button v-if="facility.flow" type="primary" @click="skipFlow">流程体验</el-button>
              </span>
            </el-dialog>
          </div>
          <span class="arrow"></span>

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
      centerDialogVisible: false,
      info: {

      },
      facility: {

      }
    }
  },
  computed: {
    name () {
      return this.$route.params.name
    }
  },
  mounted () {
    this.$api.getDepartmentInfo(this.name).then(res => {
      this.info = res.data
    })
  },
  methods: {
    chooseEquipment (val) {
      this.centerDialogVisible = true
      this.$api.getEquipment(val).then(res => {
        this.facility = res.data
      })
    },
    skipFlow () {
      this.centerDialogVisible = false
      this.$router.push(`/flow/${this.facility.flow}`)
    }
  }
}
</script>

<style lang="scss" scoped>
.department {
  .el-container {
    margin-top: 30px;
  }
  .el-aside {
    margin: 20px 0 0 20px;
    overflow: hidden;
    width: 400px;
    height: 400px;
  }
  &-image {
    width: 100%;
    height: 100%;
  }
}
//引入
.inside {
  border: 1px solid #ddd;
  padding: 25px 28px 28px;
  position: relative;
  margin-left: 10px;
  background: #fff;
}

.arrow {
  position: absolute;
  width: 17px;
  height: 26px;
  background: url(./../../../../static/images/arrow-1.png) 0 0 no-repeat;
  left: -11px;
  top: 19px;
}
//引出
.content {
  //margin: 50px 0 0 150px;
  position: relative;
  width: 100%;
  .label {
    width: 20%;
    color: $green;
    font-size: 1em;

    // padding-bottom: 1em;
    position: relative;
    // margin-bottom: 10px;
  }
  .info {
    // width: 80%;
    font-size: 1em;
  }
  & > div {
    // display: flex;
    // align-items: flex-end;
    margin-top: 20px;
  }
  .label {
    margin-bottom: 10px;
  }
  p {
    // margin-right: 150px;
  }
  & > ul {
    margin-top: 20px;

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
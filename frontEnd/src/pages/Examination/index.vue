<template>
  <div class="exam">
    <el-table :data="tableData" style="width: 100%" :row-class-name="tableRowClassName">
      <el-table-column prop="name" label="试卷名">
      </el-table-column>
      <el-table-column prop="startTime" label="开始时间">
      </el-table-column>
      <el-table-column prop="endTime" label="结束时间">
      </el-table-column>
      <el-table-column prop="duration" label="考试时间"></el-table-column>
      <el-table-column prop="state" label="状态" :filters="[{ text: '正在进行', value: '正在进行' }, { text: '即将进行', value: '即将进行' },{text:'已结束',value:'已结束'}]"
      :filter-method="filterTag"
      filter-placement="bottom-end"></el-table-column>
      <el-table-column>
        <template slot-scope="scope">
          <el-button v-if="scope.row.state ==='正在进行'" @click.native.prevent="check(scope.row)" type="button" size="mini">
            开始考试
          </el-button>
          <p v-else-if="scope.row.state ==='已结束'" @click.native.prevent="check(scope.row)">
            {{`${scope.row.score} 分`}}
          </p>

        </template>
      </el-table-column>

    </el-table>
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
      tableData: [{
        id: '1',
        name: '冲刺一卷',
        startTime: '2018/1/1',
        endTime: '2019/1/1',
        duration: 1800000,
        description: '',
        state: 'going'
      }, {
        id: '1',
        name: '冲刺一卷',
        startTime: '2018/1/1',
        endTime: '2019/1/1',
        duration: 1800000,
        description: '',
        state: 'going'
      }, {
        id: '1',
        name: '冲刺一卷',
        startTime: '2018/1/1',
        endTime: '2019/1/1',
        duration: 1800000,
        description: '',
        state: 'coming'
      }, {
        id: '1',
        name: '冲刺一卷',
        startTime: '2018/1/1',
        endTime: '2019/1/1',
        duration: 1800000,
        description: '',
        state: 'ended',
        score: 80
      }]
    }
  },
  computed: {},
  mounted () {
    this.computeData(this.tableData)
  },
  methods: {
    tableRowClassName ({row, rowIndex}) {
      if (row.state === '正在进行') {
        return 'going-row'
      } else if (row.state === '即将进行') {
        return 'coming-row'
      } else if (row.state === '已结束') {
        return 'ended-row'
      } else {
        return ''
      }
    },
    filterTag (value, row) {
      return row.state === value
    },
    computeData (data) {
      data.forEach(val => {
        val.duration = val.duration / 60000 + '分钟'
        switch (val.state) {
          case 'going':
            val.state = '正在进行'
            // val.operation = '开始考试'
            break
          case 'coming':
            val.state = '即将进行'
            // val.operation = ''
            break
          case 'ended':
            val.state = '已结束'
            // val.operation = val.score + '分'
            break
          default:
            break
        }
      })
    },
    check (row) {
      // console.log(index, this.tableData[index])
      return row.state
      // if (row.state === '正在进行') { return true } else return false
    }
  }
}
</script>
<style lang="scss">
.exam{
  // padding-left:30px;
  // padding-right:30px;
  .el-table{
    
    padding:0 30px;
    
  }
}
.el-table .coming-row {
  background: oldlace;
}

.el-table .going-row {
  background: #f0f9eb;
}
.el-table .ended-row {
  background: #eee;
}
</style>
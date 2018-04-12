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
      <el-table-column prop="state" label="状态" :filters="[{ text: '进行中', value: '进行中' }, { text: '即将进行', value: '即将进行' },{text:'已结束',value:'已结束'}]" :filter-method="filterTag" filter-placement="bottom-start"></el-table-column>
      <el-table-column>
        <template slot-scope="scope">
          <el-button v-if="scope.row.state ==='进行中'" @click.native.prevent="startTest(scope.row)" type="button" size="mini">
            开始考试
          </el-button>
          <p v-else-if="scope.row.state ==='已结束'">
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
      tableData: []
    }
  },
  computed: {},
  mounted () {
    this.$api.getTest().then(res => {
      this.tableData = res.data
      if (this.tableData) {
        this.computeData(this.tableData)
      }
    })
  },
  methods: {
    tableRowClassName ({row, rowIndex}) {
      if (row.state === '进行中') {
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
        val.duration = val.duration / 60 + '分钟'
        switch (val.state) {
          case 'going':
            val.state = '进行中'
            break
          case 'coming':
            val.state = '即将进行'
            break
          case 'ended':
            val.state = '已结束'
            break
          default:
            break
        }
      })
    },
    startTest (row) {
      console.log(row)
      this.$router.push(`/test/${row.id}`)
    }
  }
}
</script>
<style lang="scss">
.exam {
  .el-table {
    padding: 0 30px;
    &::before {
      height: 0;
    }
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
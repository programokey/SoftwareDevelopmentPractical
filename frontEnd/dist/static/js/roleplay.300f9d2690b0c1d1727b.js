webpackJsonp([0],{"0fVa":function(t,e,a){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var s={render:function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"classification"},t._l(t.classifyList,function(e,s){return a("a",{key:s,attrs:{href:"#"+e}},[t._v(t._s(e))])}))},staticRenderFns:[]};var n={render:function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"casecell"},[a("h3",{staticClass:"cell-classify",attrs:{id:t.title}},[t._v(t._s(t.title))]),t._v(" "),a("ul",{staticClass:"cell-list"},t._l(t.data,function(e,s){return a("li",{key:s,staticClass:"cell-list m-button",on:{click:function(a){t.$router.push("/case/"+e)}}},[t._v(t._s(e))])}))])},staticRenderFns:[]};var r={components:{Classification:a("VU/8")({components:{},props:["classifyList"],data:function(){return{}},computed:{},mounted:function(){},methods:{}},s,!1,function(t){a("QOCO")},null,null).exports,CaseCell:a("VU/8")({components:{},props:["title","data"],data:function(){return{}},computed:{},mounted:function(){},methods:{}},n,!1,function(t){a("9dh5")},null,null).exports},props:{},data:function(){return{search:"",caseList:{}}},computed:{},mounted:function(){var t=this;this.$api.getDisCategoryList().then(function(e){t.caseList=e.data})},methods:{}},i={render:function(){var t=this.$createElement,e=this._self._c||t;return e("el-row",{staticClass:"case",attrs:{gutter:20}},[e("el-col",{staticClass:"case-left",attrs:{span:20}},[e("div",{staticClass:"case-cell-wrap"},this._l(this.caseList,function(t,a){return e("case-cell",{key:a,attrs:{title:a,data:t}})}))]),this._v(" "),e("el-col",{staticClass:"case-right",attrs:{span:4}},[e("classification",{attrs:{classifyList:Object.keys(this.caseList)}})],1)],1)},staticRenderFns:[]};var l=a("VU/8")(r,i,!1,function(t){a("edHY")},null,null);e.default=l.exports},"9dh5":function(t,e){},"E+pU":function(t,e,a){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var s={components:{AppHeader:a("VJFb").a},props:{},data:function(){return{roles:[{name:"前台",imgUrl:"static/images/doctor.jpeg"},{name:"医助",imgUrl:"static/images/doctor.jpeg"},{name:"医师",imgUrl:"static/images/doctor.jpeg"}]}},computed:{},mounted:function(){},methods:{}},n={render:function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"roleplay"},[a("section",{staticClass:"works section no-padding",attrs:{id:"works"}},[a("div",{staticClass:"container-fluid"},[a("div",{staticClass:"row no-gutter"},[a("el-row",t._l(t.roles,function(e,s){return a("el-col",{key:s,attrs:{span:8}},[a("div",{staticClass:"grid-content bg-purple work"},[a("a",{staticClass:"work-box",on:{click:function(a){t.$router.push("/roleplay/"+e.name)}}},[a("img",{attrs:{src:e.imgUrl,alt:""}}),t._v(" "),a("div",{staticClass:"overlay"},[a("div",{staticClass:"overlay-caption"},[a("h5",[t._v(t._s(e.name))]),t._v(" "),a("p",[a("i",{staticClass:"fa fa-search-plus fa-2x"})])])])])])])}))],1)])])])},staticRenderFns:[]};var r=a("VU/8")(s,n,!1,function(t){a("xcHd")},null,null);e.default=r.exports},OoaX:function(t,e){},QOCO:function(t,e){},edHY:function(t,e){},"pdn/":function(t,e,a){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var s={components:{AppHeader:a("VJFb").a},props:{},data:function(){return{tableData:[]}},computed:{},mounted:function(){var t=this;this.$api.getTest().then(function(e){t.tableData=e.data,t.computeData(t.tableData)})},methods:{tableRowClassName:function(t){var e=t.row;t.rowIndex;return"进行中"===e.state?"going-row":"即将进行"===e.state?"coming-row":"已结束"===e.state?"ended-row":""},filterTag:function(t,e){return e.state===t},computeData:function(t){t.forEach(function(t){switch(t.duration=t.duration/60+"分钟",t.state){case"going":t.state="进行中";break;case"coming":t.state="即将进行";break;case"ended":t.state="已结束"}})},startTest:function(t){console.log(t),this.$router.push("/test/"+t.id)}}},n={render:function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"exam"},[a("el-table",{staticStyle:{width:"100%"},attrs:{data:t.tableData,"row-class-name":t.tableRowClassName}},[a("el-table-column",{attrs:{prop:"name",label:"试卷名"}}),t._v(" "),a("el-table-column",{attrs:{prop:"startTime",label:"开始时间"}}),t._v(" "),a("el-table-column",{attrs:{prop:"endTime",label:"结束时间"}}),t._v(" "),a("el-table-column",{attrs:{prop:"duration",label:"考试时间"}}),t._v(" "),a("el-table-column",{attrs:{prop:"state",label:"状态",filters:[{text:"正在进行",value:"正在进行"},{text:"即将进行",value:"即将进行"},{text:"已结束",value:"已结束"}],"filter-method":t.filterTag,"filter-placement":"bottom-start"}}),t._v(" "),a("el-table-column",{scopedSlots:t._u([{key:"default",fn:function(e){return["进行中"===e.row.state?a("el-button",{attrs:{type:"button",size:"mini"},nativeOn:{click:function(a){a.preventDefault(),t.startTest(e.row)}}},[t._v("\n          开始考试\n        ")]):"已结束"===e.row.state?a("p",[t._v("\n          "+t._s(e.row.score+" 分")+"\n        ")]):t._e()]}}])})],1)],1)},staticRenderFns:[]};var r=a("VU/8")(s,n,!1,function(t){a("OoaX")},null,null);e.default=r.exports},xcHd:function(t,e){}});
//# sourceMappingURL=roleplay.300f9d2690b0c1d1727b.js.map
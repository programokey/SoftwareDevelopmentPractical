webpackJsonp([0],{"3pEW":function(t,e){},"6HdG":function(t,e){},"7vTX":function(t,e){},JEOp:function(t,e,a){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var s={components:{AppHeader:a("VJFb").a},props:{},data:function(){return{tableData:[{id:"1",name:"冲刺一卷",startTime:"2018/1/1",endTime:"2019/1/1",duration:18e5,description:"",state:"going"},{id:"1",name:"冲刺一卷",startTime:"2018/1/1",endTime:"2019/1/1",duration:18e5,description:"",state:"going"},{id:"1",name:"冲刺一卷",startTime:"2018/1/1",endTime:"2019/1/1",duration:18e5,description:"",state:"coming"},{id:"1",name:"冲刺一卷",startTime:"2018/1/1",endTime:"2019/1/1",duration:18e5,description:"",state:"ended",score:80}]}},computed:{},mounted:function(){this.computeData(this.tableData)},methods:{tableRowClassName:function(t){var e=t.row;t.rowIndex;return"正在进行"===e.state?"going-row":"即将进行"===e.state?"coming-row":"已结束"===e.state?"ended-row":""},filterTag:function(t,e){return e.state===t},computeData:function(t){t.forEach(function(t){switch(t.duration=t.duration/6e4+"分钟",t.state){case"going":t.state="正在进行";break;case"coming":t.state="即将进行";break;case"ended":t.state="已结束"}})},startTest:function(t){console.log(t)}}},n={render:function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"exam"},[a("el-table",{staticStyle:{width:"100%"},attrs:{data:t.tableData,"row-class-name":t.tableRowClassName}},[a("el-table-column",{attrs:{prop:"name",label:"试卷名"}}),t._v(" "),a("el-table-column",{attrs:{prop:"startTime",label:"开始时间"}}),t._v(" "),a("el-table-column",{attrs:{prop:"endTime",label:"结束时间"}}),t._v(" "),a("el-table-column",{attrs:{prop:"duration",label:"考试时间"}}),t._v(" "),a("el-table-column",{attrs:{prop:"state",label:"状态",filters:[{text:"正在进行",value:"正在进行"},{text:"即将进行",value:"即将进行"},{text:"已结束",value:"已结束"}],"filter-method":t.filterTag,"filter-placement":"bottom-start"}}),t._v(" "),a("el-table-column",{scopedSlots:t._u([{key:"default",fn:function(e){return["正在进行"===e.row.state?a("el-button",{attrs:{type:"button",size:"mini"},nativeOn:{click:function(a){a.preventDefault(),t.startTest(e.row)}}},[t._v("\n          开始考试\n        ")]):"已结束"===e.row.state?a("p",[t._v("\n          "+t._s(e.row.score+" 分")+"\n        ")]):t._e()]}}])})],1)],1)},staticRenderFns:[]};var r=a("VU/8")(s,n,!1,function(t){a("6HdG")},null,null);e.default=r.exports},Lgsj:function(t,e){},MPCj:function(t,e,a){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var s={render:function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"classification"},t._l(t.classifyList,function(e,s){return a("a",{key:s,attrs:{href:"#"+e}},[t._v(t._s(e))])}))},staticRenderFns:[]};var n={render:function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"casecell"},[a("h3",{staticClass:"cell-classify",attrs:{id:t.title}},[t._v(t._s(t.title))]),t._v(" "),a("ul",{staticClass:"cell-list"},t._l(t.data,function(e,s){return a("li",{key:s,staticClass:"cell-list m-button",on:{click:function(a){t.$router.push("/case/"+e)}}},[t._v(t._s(e))])}))])},staticRenderFns:[]};var r={components:{Classification:a("VU/8")({components:{},props:["classifyList"],data:function(){return{list:["分类1","分类2","分类3","分类4","分类5","分类6","分类7","分类8"]}},computed:{},mounted:function(){},methods:{}},s,!1,function(t){a("XYt1")},null,null).exports,CaseCell:a("VU/8")({components:{},props:["title","data"],data:function(){return{}},computed:{},mounted:function(){},methods:{}},n,!1,function(t){a("Lgsj")},null,null).exports},props:{},data:function(){return{search:"",caseList:{"分类1":["病病病病1","病病病2","病3","病病1","病2","病3","病1","病2","病3","病1","病2","病3","病1","病病病病病2","病3","病1","病2","病3"],"分类2":["病1","病2","病3","病病","病2","病3","病1","病2","病3","病1","病2","病3","病1","病2","病病病3","病1","病2","病3"],"分类3":["病1","病2","病3","病1","病2","病3","病病1","病2","病3","病1","病病病2","病3","病1","病2","病3","病1","病2","病3"],"分类4":["病1","病2","病3","病1","病2","病3","病病1","病2","病3","病1","病病病2","病3","病1","病2","病3","病1","病2","病3"],"分类5":["病1","病2","病3","病1","病2","病3","病病1","病2","病3","病1","病病病2","病3","病1","病2","病3","病1","病2","病3"],"分类6":["病1","病2","病3","病1","病2","病3","病病1","病2","病3","病1","病病病2","病3","病1","病2","病3","病1","病2","病3"],"分类7":["病1","病2","病3","病1","病2","病3","病病1","病2","病3","病1","病病病2","病3","病1","病2","病3","病1","病2","病3"],"分类8":["病1","病2","病3","病1","病2","病3","病病1","病2","病3","病1","病病病2","病3","病1","病2","病3","病1","病2","病3"],"分类9":["病1","病2","病3","病1","病2","病3","病病1","病2","病3","病1","病病病2","病3","病1","病2","病3","病1","病2","病3"],"分类10":["病1","病2","病3","病1","病2","病3","病病1","病2","病3","病1","病病病2","病3","病1","病2","病3","病1","病2","病3"],"分类11":["病1","病2","病3","病1","病2","病3","病病1","病2","病3","病1","病病病2","病3","病1","病2","病3","病1","病2","病3"],"分类12":["病1","病2","病3","病1","病2","病3","病病1","病2","病3","病1","病病病2","病3","病1","病2","病3","病1","病2","病3"],"分类13":["病1","病2","病3","病1","病2","病3","病病1","病2","病3","病1","病病病2","病3","病1","病2","病3","病1","病2","病3"],"分类14":["病1","病2","病3","病1","病2","病3","病病1","病2","病3","病1","病病病2","病3","病1","病2","病3","病1","病2","病3"]}}},computed:{},mounted:function(){},methods:{}},i={render:function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("el-row",{staticClass:"case",attrs:{gutter:20}},[a("el-col",{staticClass:"case-left",attrs:{span:20}},[a("el-input",{staticClass:"case-search",attrs:{placeholder:"请输入搜索内容","prefix-icon":"el-icon-search"},model:{value:t.search,callback:function(e){t.search=e},expression:"search"}}),t._v(" "),a("div",{staticClass:"case-cell-wrap"},t._l(t.caseList,function(t,e){return a("case-cell",{key:e,attrs:{title:e,data:t}})}))],1),t._v(" "),a("el-col",{staticClass:"case-right",attrs:{span:4}},[a("classification",{attrs:{classifyList:Object.keys(t.caseList)}})],1)],1)},staticRenderFns:[]};var o=a("VU/8")(r,i,!1,function(t){a("3pEW")},null,null);e.default=o.exports},XYt1:function(t,e){},jOUK:function(t,e,a){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var s={components:{AppHeader:a("VJFb").a},props:{},data:function(){return{roles:[{name:"前台",imgUrl:"./../../images/doctor.jpeg"},{name:"医助",imgUrl:"./../../images/doctor.jpeg"},{name:"医师",imgUrl:"./../../images/doctor.jpeg"}]}},computed:{},mounted:function(){},methods:{}},n={render:function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",[a("div",[t._v("角色扮演")]),t._v(" "),a("div",[a("section",{staticClass:"works section no-padding",attrs:{id:"works"}},[a("div",{staticClass:"container-fluid"},[a("div",{staticClass:"row no-gutter"},[a("el-row",t._l(t.roles,function(e,s){return a("el-col",{key:s,attrs:{span:8}},[a("div",{staticClass:"grid-content bg-purple work"},[a("a",{staticClass:"work-box",on:{click:function(a){t.$router.push("/roleplay/"+e.name)}}},[a("img",{attrs:{src:e.imgUrl,alt:""}}),t._v(" "),a("div",{staticClass:"overlay"},[a("div",{staticClass:"overlay-caption"},[a("h5",[t._v(t._s(e.name))]),t._v(" "),a("p",[a("i",{staticClass:"fa fa-search-plus fa-2x"})])])])])])])}))],1)])])])])},staticRenderFns:[]};var r=a("VU/8")(s,n,!1,function(t){a("7vTX")},null,null);e.default=r.exports}});
//# sourceMappingURL=roleplay.e508c0ef1f87bc00363c.js.map
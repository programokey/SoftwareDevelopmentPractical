webpackJsonp([5],{"28N2":function(t,e){},"Tq/P":function(t,e,r){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var a={render:function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",{staticClass:"Role"},[r("el-breadcrumb",{staticClass:"breadcrumb",attrs:{separator:"/"}},[r("el-breadcrumb-item",{attrs:{to:{path:"/roleplay"}}},[t._v("角色扮演")]),t._v(" "),r("el-breadcrumb-item",{attrs:{to:{path:"/roleplay/"+t.name}}},[t._v(t._s(t.name))]),t._v(" "),r("el-breadcrumb-item",[t._v(t._s(t.workType))])],1),t._v(" "),r("div",{staticClass:"head"},[r("h5",[t._v(t._s(t.workType))])]),t._v(" "),r("ul",{staticClass:"workTypeDescription"},[r("li",[t._v("描述："+t._s(t.data.description))]),t._v(" "),r("li",[t._v("注意事项："+t._s(t.data.dosAndDonots))]),t._v(" "),t.data.jobflow?r("li",{on:{click:function(e){t.$router.push("/")}}},[t._v("职能流程体验 ")]):t._e()])],1)},staticRenderFns:[]};var o=r("VU/8")({components:{},props:{},data:function(){return{data:{description:"工作类别详细描述",dosAndDonots:"工作类别注意事项",jobflow:"1"}}},computed:{name:function(){return this.$route.params.name},workType:function(){return this.$route.params.workType}},mounted:function(){},methods:{}},a,!1,function(t){r("28N2")},null,null);e.default=o.exports}});
//# sourceMappingURL=workType.bcc4d0374f023a8c2c77.js.map
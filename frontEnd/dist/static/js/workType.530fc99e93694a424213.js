webpackJsonp([9],{ciUG:function(t,a){},x3vL:function(t,a,s){"use strict";Object.defineProperty(a,"__esModule",{value:!0});var e={render:function(){var t=this,a=t.$createElement,s=t._self._c||a;return s("div",{staticClass:"Role"},[s("el-breadcrumb",{staticClass:"breadcrumb",attrs:{separator:"/"}},[s("el-breadcrumb-item",{attrs:{to:{path:"/roleplay"}}},[t._v("角色扮演")]),t._v(" "),s("el-breadcrumb-item",{attrs:{to:{path:"/roleplay/"+t.name}}},[t._v(t._s(t.name))]),t._v(" "),s("el-breadcrumb-item",[t._v(t._s(t.workType))])],1),t._v(" "),s("div",{staticClass:"top-box"},[s("div",{staticClass:"wrap"},[s("div",{staticClass:"content-top"},[s("h1",[t._v(t._s(t.workType))]),t._v(" "),s("div",{staticClass:"grid_6"},[s("div",{staticClass:"box-4 clearfix"},[s("img",{staticClass:"img-ind",attrs:{src:"/src/images/pic11.jpg",alt:""}}),t._v(" "),s("div",{staticClass:"extra-wrap"},[s("div",{staticClass:"inside"},[s("h3",[t._v("描述:")]),t._v(" "),s("div",{staticClass:"margin"},[s("span",{staticClass:"quote"}),t._v(t._s(t.data.description)+"”")]),t._v(" "),s("span",{staticClass:"arrow"}),t._v(" "),s("h3",[t._v("注意事项:")]),t._v(" "),s("div",[s("span",{staticClass:"quote"}),t._v(t._s(t.data.dosAndDonots)+"”")]),t._v(" "),s("span",{staticClass:"arrow"})])])])]),t._v(" "),t.data.jobflow?s("div",{staticClass:"right a-hov",on:{click:function(a){t.$router.push("/flow/"+t.data.jobflow)}}},[t._v("职能流程体验")]):t._e()])]),t._v(" "),s("div",{staticClass:"clear"})])],1)},staticRenderFns:[]};var i=s("VU/8")({components:{},props:{},data:function(){return{data:{}}},computed:{name:function(){return this.$route.params.name},workType:function(){return this.$route.params.workType}},mounted:function(){var t=this;this.$api.getRoleJobInfo(this.name,this.workType).then(function(a){t.data=a.data})},methods:{}},e,!1,function(t){s("ciUG")},null,null);a.default=i.exports}});
//# sourceMappingURL=workType.530fc99e93694a424213.js.map
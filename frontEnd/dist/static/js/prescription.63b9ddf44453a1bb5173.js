webpackJsonp([14],{cSMc:function(e,a,t){"use strict";Object.defineProperty(a,"__esModule",{value:!0});var i={render:function(){var e=this,a=e.$createElement,t=e._self._c||a;return t("div",{staticClass:"case"},[t("el-breadcrumb",{staticClass:"breadcrumb",attrs:{separator:"/"}},[t("el-breadcrumb-item",{attrs:{to:{path:"/learn"}}},[e._v("病例学习")]),e._v(" "),t("el-breadcrumb-item",{attrs:{to:{path:"/case/"+e.diseaseName}}},[e._v(e._s(e.diseaseName))]),e._v(" "),t("el-breadcrumb-item",[e._v(e._s(e.caseId))])],1),e._v(" "),t("div",[t("el-form",{ref:"form",attrs:{model:e.form,"label-width":"80px",disabled:"true","label-position":"left"}},[t("el-form-item",{attrs:{label:"处方描述"}},[t("el-input",{model:{value:e.data.description,callback:function(a){e.$set(e.data,"description",a)},expression:"data.description"}})],1)],1),e._v(" "),t("div",[e._v("本处方所用药品如下：")]),e._v(" "),t("el-collapse",{staticClass:"info",on:{change:e.handleChange},model:{value:e.activeNames,callback:function(a){e.activeNames=a},expression:"activeNames"}},e._l(e.data.medicines,function(a,i){return t("el-collapse-item",{key:i,attrs:{title:a.name,name:i}},[t("div",[e._v("approvalNumber: "+e._s(a.approvalNumber))]),e._v(" "),t("div",[e._v("unit: "+e._s(a.unit))]),e._v(" "),t("div",[e._v("name: "+e._s(a.name))])])}))],1)],1)},staticRenderFns:[]};var r=t("VU/8")({components:{},props:{},data:function(){return{data:{description:"用于治疗。。。的处方",medicines:[{approvalNumber:"1111111",unit:"2",name:"黄连上清片"},{approvalNumber:"2222222",unit:"3",name:"感冒灵"}]}}},computed:{id:function(){return this.$route.params.item}},mounted:function(){},methods:{}},i,!1,function(e){t("q53R")},"data-v-02100791",null);a.default=r.exports},q53R:function(e,a){}});
//# sourceMappingURL=prescription.63b9ddf44453a1bb5173.js.map
webpackJsonp([7],{dqY6:function(t,e){},u7j2:function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var s={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"flowStep"},[n("div",{staticClass:"flow-content"},["Video"===t.step.type?n("div",{staticClass:"flow-video"},[n("video",{attrs:{src:t.step.content,controls:"controls",width:"846px",height:"568px"}})]):n("div",{staticClass:"flow-pic"},[n("img",{attrs:{src:t.step.content,alt:""}})]),t._v(" "),n("div",{staticClass:"flow-description"},[n("p",[t._v(t._s(t.step.description))]),t._v(" "),t._t("default")],2)])])},staticRenderFns:[]};var i={components:{FlowStep:n("VU/8")({components:{},props:["step"],data:function(){return{}},computed:{},mounted:function(){},methods:{}},s,!1,function(t){n("dqY6")},"data-v-97afbb36",null).exports},props:{},data:function(){return{data:[],index:0}},computed:{currentStep:function(){return this.data[this.index]}},mounted:function(){var t=this;this.$api.getFlow(this.$route.params.flowId).then(function(e){t.data=e.data})},methods:{}},o={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"flow"},[n("flow-step",{staticClass:"step",attrs:{step:t.currentStep}},[n("div",{staticClass:"step-control"},[t.index>0?n("div",{staticClass:"left m-button",on:{click:function(e){t.index--}}},[t._v("上一步")]):t._e(),t._v(" "),t.index<t.data.length-1?n("div",{staticClass:"right m-button",on:{click:function(e){t.index++}}},[t._v("下一步")]):t._e()])])],1)},staticRenderFns:[]};var a=n("VU/8")(i,o,!1,function(t){n("ztvq")},"data-v-7e5c2b06",null);e.default=a.exports},ztvq:function(t,e){}});
//# sourceMappingURL=flow.75500f78efede0d4b9f4.js.map
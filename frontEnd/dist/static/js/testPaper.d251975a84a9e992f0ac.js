webpackJsonp([3],{"6V7y":function(t,e){},IkJr:function(t,e){},J5Q1:function(t,e){},QdNR:function(t,e){},xn6F:function(t,e,s){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var n={components:{},props:["time"],data:function(){return{count:0,interval:""}},computed:{},watch:{time:function(t){this.count=t,this.interval=setInterval(this.countDown,1e3)}},mounted:function(){},methods:{countDown:function(){0===this.count&&(clearInterval(this.interval),this.$emit("submit"),this.$message({message:"考试结束",type:"warning"})),this.count-=1}}},i={render:function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"time-count"},[s("p",[t._v("考试剩余时间：\n    "),parseInt(t.count/3600)>0?s("span",[t._v(t._s(parseInt(t.count/3600))+"小时")]):t._e(),t._v(" "),s("span",[t._v(t._s(parseInt(t.count/60)>=60?parseInt(t.count/60%60):parseInt(t.count/60))+"分钟")]),t._v(" "),s("span",[t._v(t._s(t.count%60)+"秒")])])])},staticRenderFns:[]};var a=s("VU/8")(n,i,!1,function(t){s("6V7y")},"data-v-870f5778",null).exports,r={render:function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"single-card"},[s("div",{staticClass:"single-card-title"},[t._v(t._s(t.order)+". "+t._s(t.subject.problem))]),t._v(" "),t._l(t.subject.choice,function(e,n,i){return s("el-radio",{key:n,staticClass:"single-card-radio",attrs:{label:+n},on:{change:t.emitChange},model:{value:t.radio,callback:function(e){t.radio=e},expression:"radio"}},[t._v(t._s(""+String.fromCharCode(65+i))+" "+t._s(e))])})],2)},staticRenderFns:[]};var c={render:function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"multiple-card"},[s("div",{staticClass:"multiple-card-title"},[t._v(t._s(t.order)+". "+t._s(t.subject.problem))]),t._v(" "),s("el-checkbox-group",{on:{change:t.emitChange},model:{value:t.checkList,callback:function(e){t.checkList=e},expression:"checkList"}},t._l(t.subject.choice,function(e,n,i){return s("el-checkbox",{key:n,attrs:{label:+n}},[t._v(t._s(String.fromCharCode(65+i)+" "+e))])}))],1)},staticRenderFns:[]};var o={components:{SingleCard:s("VU/8")({components:{},props:["subject","order","selected"],data:function(){return{radio:""}},computed:{},mounted:function(){this.selected&&(this.radio=this.selected[0])},methods:{emitChange:function(){this.$emit("selectOpration",{radio:this.radio,problemId:this.subject.problemId})}}},r,!1,function(t){s("QdNR")},null,null).exports,MultipleCard:s("VU/8")({components:{},props:["subject","order","selected"],data:function(){return{checkList:[]}},computed:{},mounted:function(){this.selected&&(this.checkList=this.selected)},methods:{emitChange:function(){this.$emit("selectOpration",{radio:this.checkList,problemId:this.subject.problemId})}}},c,!1,function(t){s("J5Q1")},null,null).exports,TimeCount:a},props:{},data:function(){return{data:{},selected:{}}},computed:{},created:function(){var t=this;this.$api.getTestQuestions(this.$route.params.id).then(function(e){t.data=e.data,t.selected=t.data.selected})},mounted:function(){},methods:{selectOperation:function(t){t.radio.constructor!==Array&&(t.radio=[t.radio]),this.selected[t.problemId]=t.radio},saveResult:function(){var t=this,e=window.JSON.stringify(this.selected);this.$api.postTestResult({testId:this.$route.params.id,answer:e}).then(function(e){t.$message({message:"保存成功"})})},submit:function(){var t=this,e=window.JSON.stringify(this.selected);this.$api.postTestResult({testId:this.$route.params.id,answer:e}).then(function(e){1e3===e.code&&(t.$message({message:"试卷提交成功"}),t.$router.push("/test"))})}}},l={render:function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"paper"},[s("div",{staticClass:"paper-wrap"},[s("time-count",{staticClass:"count",attrs:{time:t.data.remainingTime},on:{submit:t.submit}}),t._v(" "),t.data.single&&0!==t.data.single.length?s("div",{staticClass:"single"},[s("h3",[t._v("单选题")]),t._v(" "),s("div",{staticClass:"question-wrap"},t._l(t.data.single,function(e,n){return s("single-card",{key:n,attrs:{subject:e,order:n+1,selected:t.selected[e.problemId]},on:{selectOpration:t.selectOperation}})}))]):t._e(),t._v(" "),t.data.multiple&&0!==t.data.multiple.length?s("div",{staticClass:"multiple"},[s("h3",[t._v("多选题")]),t._v(" "),s("div",{staticClass:"question-wrap"},t._l(t.data.multiple,function(e,n){return s("multiple-card",{key:n,attrs:{subject:e,order:n+1,selected:t.selected[e.problemId]},on:{selectOpration:t.selectOperation}})}))]):t._e(),t._v(" "),s("div",{staticClass:"button-wrap"},[s("el-button",{on:{click:t.saveResult}},[t._v("保存")]),t._v(" "),s("el-button",{staticClass:"primary-button",attrs:{type:"primary"},on:{click:t.submit}},[t._v("提交")])],1)],1)])},staticRenderFns:[]};var u=s("VU/8")(o,l,!1,function(t){s("IkJr")},null,null);e.default=u.exports}});
//# sourceMappingURL=testPaper.d251975a84a9e992f0ac.js.map
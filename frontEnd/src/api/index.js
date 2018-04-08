import http from './http'
const foo = () => {
  return http.post('url', {})
}
const login = (name, hash) => {
  return http.post('/login', {
    name: name,
    hash: hash
  })
}
const getFlow = (val) => {
  return http.get(`flow/${val}`)
}
const getMedicineInfo = (val) => {
  return http.get(`/medicine/${val}`)
}
/* 科室 */
const getDepartmentList = () => {
  return http.get('/department')
}
const getDepartmentInfo = (val) => {
  return http.get(`/department/${val}`)
}
const getEquipment = (val) => {
  return http.get(`/equipment/${val}`)
}
const getDepartmentRoleJob = (department, role) => {
  return http.get(`/department/${department}/roles/${role}`)
}
/* 角色扮演 */
// 获取角色工作列表
const getRoleJobList = (role) => {
  return http.get(`/role/${role}`)
}
// 角色工作详情
const getRoleJobInfo = (role, job) => {
  return http.get(`/role/${role}/${job}`)
}
/* 病例学习 */
// 病种列表
const getDisCategoryList = () => {
  return http.get('/diseases-categories')
}
// 病例列表
const getCaseList = (category) => {
  return http.get(`/disease/${category}`)
}
// 病例单
const getCaseInfo = (id) => {
  return http.get(`/case/${id}`)
}
// 病例单包含的检查结果
const getExaminationResult = (id) => {
  return http.get(`/examinationResult/${id}`)
}
// 病例单包含的手术
const getOperation = (name) => {
  return http.get(`/operation/${name}`)
}

/** 测试 */
// 提交答案
const postTestResult = (model) => {
  return http.post('/test/submit', {
    testId: model.testId,
    answer: model.answer
  })
}
// 获取测试列表
const getTest = () => {
  return http.get('/test')
}
// 获取试题
const getTestQuestions = (id) => {
  return http.get(`/test/id/${id}`)
}
export default {
  foo,
  login,
  getFlow,
  getMedicineInfo,
  getDepartmentList,
  getDepartmentInfo,
  getEquipment,
  getDepartmentRoleJob,
  getRoleJobList,
  getRoleJobInfo,
  getDisCategoryList,
  getCaseList,
  getCaseInfo,
  getExaminationResult,
  getOperation,
  getTest,
  getTestQuestions,
  postTestResult
}

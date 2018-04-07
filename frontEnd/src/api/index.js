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

export default {
  foo,
  login,
  getFlow,
  getMedicineInfo,
  getDepartmentList,
  getDepartmentInfo,
  getEquipment,
  getDepartmentRoleJob
}

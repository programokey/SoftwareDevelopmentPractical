import http from './http'
const foo = () => {
  return http.post('url', {})
}
const getDepartmentList = () => {
  return http.get('/department')
}
const getDepartmentInfo = (val) => {
  return http.get(`/department/${val}`)
}
const login = (name, hash) => {
  return http.post('/login', {
    name: name,
    hash: hash
  })
}

export default {
  foo,
  getDepartmentList,
  getDepartmentInfo,
  login
}

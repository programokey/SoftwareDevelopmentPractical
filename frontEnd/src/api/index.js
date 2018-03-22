import http from './http'
const foo = () => {
  return http.post('url', {})
}
const getDepartmentInfo = (name) => {
  return http.post('/department/getDepartmentInfo', {
    name: name
  })
}
const login = (name, hash) => {
  return http.post('/login', {
    name: name,
    hash: hash
  })
}
export default {
  foo,
  getDepartmentInfo,
  login
}

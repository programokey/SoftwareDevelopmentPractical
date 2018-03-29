import http from './http'
const foo = () => {
  return http.post('url', {})
}
const getDepartmentList = () => {
  console.log('aaaa')
  return http.get('/department')
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
  login
}

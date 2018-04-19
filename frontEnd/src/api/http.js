import axios from 'axios'
import qs from 'qs'
// import { baseUrl } from '@/config/env'
import router from '@/router'
import { Message } from 'element-ui'
// axios.defaults.baseURL = baseUrl
axios.defaults.baseURL = 'http://106.14.141.233:5000/api'
axios.defaults.withCredentials = true
// http request 拦截器
axios.interceptors.request.use(
  config => {
    return config
  },
  err => {
    return Promise.reject(err)
  }
)

// http response 拦截器
axios.interceptors.response.use(
  response => {
    if (response.data.code === 403) {
      Message({message: '请先登录'})
      router.push('/login')
    }
    return response.data
  },
  error => {
    if (error.response) {
      return Promise.reject(error.response.data)
    } else {
      return Promise.reject(error)
    }
  }
)

let post = (url, data, { onUploadProgressCal } = {}) => {
  return axios({
    method: 'post',
    url,
    data: qs.stringify(data),
    onUploadProgress: function (progressEvent) {
      // 对原生进度事件的处理
      if (onUploadProgressCal) {
        onUploadProgressCal(progressEvent)
      }
    }
  })
}

let get = (url, params, { onUploadProgressCal } = {}) => {
  return axios({
    method: 'get',
    url,
    params,
    onUploadProgress: function (progressEvent) {
      // 对原生进度事件的处理
      if (onUploadProgressCal) {
        onUploadProgressCal(progressEvent)
      }
    }
  })
}

let put = (url, data, { onUploadProgressCal } = {}) => {
  return axios({
    method: 'put',
    url,
    data: data,
    onUploadProgress: function (progressEvent) {
      // 对原生进度事件的处理
      if (onUploadProgressCal) {
        onUploadProgressCal(progressEvent)
      }
    }
  })
}

export default { post, get, put }

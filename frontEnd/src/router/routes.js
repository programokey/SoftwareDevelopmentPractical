/**
 * 使用() => import() 懒加载路由
 * 请指定webpackChunkName，以便打包后生成的chunk带有相对应的名字。
 */

const ErrorPage = () => import(/* webpackChunkName: "errorpage" */ '@/pages/ErrorPage')
const Guide = () => import(/* webpackChunkName: "home" */ '@/pages/Guide')
const Login = () => import(/* webpackChunkName: "login" */ '@/pages/Login')
const Roleplay = () => import(/* webpackChunkName: "roleplay" */ '@/pages/Roleplay')

/* routes config */
const routes = [
  {
    path: '*',
    name: 'ErrorPage',
    component: ErrorPage,
    props: {
      error: {
        statusCode: 'Error',
        message: '这个页面不见鸟'
      }
    }
  }, {
    path: '/404',
    name: '404',
    component: ErrorPage,
    props: {
      error: {
        statusCode: 404,
        message: '这个页面不见鸟'
      }
    }
  }, {
    path: '/',
    name: 'Guide',
    component: Guide,
    meta: {}
  }, {
    path: '/login',
    name: 'Login',
    component: Login
  }, {
    path: '/roleplay',
    name: 'Roleplay',
    component: Roleplay
  }
]

export default routes

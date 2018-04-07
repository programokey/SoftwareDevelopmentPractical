/**
 * 使用() => import() 懒加载路由
 * 请指定webpackChunkName，以便打包后生成的chunk带有相对应的名字。
 */

const ErrorPage = () => import(/* webpackChunkName: "errorpage" */ '@/pages/ErrorPage')
const Guide = () => import(/* webpackChunkName: "home" */ '@/pages/Guide')
const Login = () => import(/* webpackChunkName: "login" */ '@/pages/Login')
const Roleplay = () => import(/* webpackChunkName: "roleplay" */ '@/pages/Roleplay')
const Role = () => import(/* webpackChunkName: "role" */ '@/pages/Role')
const WorkType = () => import(/* webpackChunkName: "workType" */ '@/pages/WorkType')
const CaseStudy = () => import(/* webpackChunkName: "roleplay" */ '@/pages/CaseStudy')
const Examination = () => import(/* webpackChunkName: "roleplay" */ '@/pages/Examination')
const Department = () => import(/* webpackChunkName: "department" */ '@/pages/Department')
const Equipment = () => import(/* webpackChunkName: "equipment" */ '@/pages/Equipment')
const DepartmentRole = () => import(/* webpackChunkName: "departmentRole" */ '@/pages/DepartmentRole')
const Disease = () => import(/* webpackChunkName: "disease" */ '@/pages/Disease')
const DiseaseCase = () => import(/* webpackChunkName: "diseaseCase" */ '@/pages/DiseaseCase')
/* routes config */
const routes = [
  {
    path: '*',
    name: 'ErrorPage',
    component: ErrorPage,
    props: {
      error: {
        statusCode: 'Error',
        message: '这个页面出现了错误'
      }
    }
  }, {
    path: '/404',
    name: '404',
    component: ErrorPage,
    props: {
      error: {
        statusCode: 404,
        message: '这个页面不存在'
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
  }, {
    path: '/roleplay/:name',
    name: 'Role',
    component: Role
  },
  {
    path: '/roleplay/:name/:workType',
    name: 'WorkType',
    component: WorkType
  }, {
    path: '/learn',
    name: 'CaseStudy',
    component: CaseStudy
  }, {
    path: '/test',
    name: 'Examination',
    component: Examination
  }, {
    path: '/department/:name',
    name: 'Department',
    component: Department
    // children: [
    //   {
    //     path: '/department/:name/role/:name',
    //     component: DepartmentRole
    //   }
    // ]
  }, {
    path: '/equipment/:id',
    name: 'Equipment',
    component: Equipment
  }, {
    path: '/department/:departmentName/role/:roleName',
    name: 'departmentRole',
    component: DepartmentRole
  }, {
    path: '/case/:diseaseName',
    name: 'disease',
    component: Disease
  }, {
    path: '/case/:diseaseName/:caseId',
    name: 'case',
    component: DiseaseCase
  }
]

export default routes

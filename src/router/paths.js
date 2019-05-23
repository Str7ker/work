/**
 * Define all of your application routes here
 * for more information on routes, see the
 * official documentation https://router.vuejs.org/en/
 */
export default [
  {
    path: '/dashboard',
    name: 'Главная',
    // Relative to /src/views
    view: 'Dashboard'
  },
  {
    path: '/user-profile',
    name: 'Мой профиль',
    view: 'UserProfile'
  },
  {
    path: '/table-list',
    name: 'Мои грузы',
    view: 'TableList'
  },
  {
    path: '/typography',
    view: 'Typography'
  },
  {
    path: '/icons',
    view: 'Icons'
  },
  {
    path: '/maps',
    view: 'Maps'
  },
  {
    path: '/notifications',
    view: 'Notifications'
  },
  {
    path: '/upgrade',
    name: 'Upgrade to PRO',
    view: 'Upgrade'
  }
]

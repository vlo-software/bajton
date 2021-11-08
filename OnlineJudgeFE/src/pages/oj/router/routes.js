// all routes here.
import {
  About,
  ACMRank,
  Announcements,
  FAQ,
  Home,
  Logout,
  NotFound,
  OIRank,
  Problem,
  ProblemList,
  SubmissionDetails,
  SubmissionList,
  UserHome
} from '../views'

import * as Contest from '@oj/views/contest'
import * as Setting from '@oj/views/setting'

import NextHome from '@oj/next/views/Home.vue'
import Login from '@oj/next/views/Login.vue'
import Register from '@oj/next/views/Register.vue'
import ResetPassword from '@oj/next/views/ResetPassword.vue'
import ResetPasswordVerify from '@oj/next/views/ResetPasswordVerify.vue'

import OjBase from '@oj/views/base/OjBase'
import NextBase from '@oj/views/base/NextBase'

export default [
  {
    name: 'next',
    path: '/next',
    component: NextBase,
    children: [
      {
        name: 'landing',
        path: '/',
        component: NextHome
      },
      {
        name: 'login',
        path: '/login',
        component: Login
      },
      {
        name: 'register',
        path: '/register',
        component: Register
      },
      {
        name: 'reset-password',
        path: '/reset-password',
        component: ResetPassword
      },
      {
        name: 'reset-password-verify',
        path: '/reset-password-verify/:token',
        component: ResetPasswordVerify
      }
    ]
  },
  {
    name: 'base',
    path: '/',
    component: OjBase,
    children: [
      {
        name: 'home',
        path: '/home',
        meta: {title: 'Home'},
        component: Home
      },
      {
        name: 'logout',
        path: '/logout',
        meta: {title: 'Logout'},
        component: Logout
      },
      {
        name: 'problem-list',
        path: '/problem',
        meta: {title: 'Problem List'},
        component: ProblemList
      },
      {
        name: 'problem-details',
        path: '/problem/:problemID',
        meta: {title: 'Problem Details'},
        component: Problem
      },
      {
        name: 'submission-list',
        path: '/status',
        meta: {title: 'Submission List'},
        component: SubmissionList
      },
      {
        name: 'submission-details',
        path: '/status/:id/',
        meta: {title: 'Submission Details'},
        component: SubmissionDetails
      },
      {
        name: 'contest-list',
        path: '/contest',
        meta: {title: 'Contest List'},
        component: Contest.ContestList
      },
      {
        name: 'contest-details',
        path: '/contest/:contestID/',
        component: Contest.ContestDetails,
        meta: {title: 'Contest Details'},
        children: [
          {
            name: 'contest-submission-list',
            path: 'submissions',
            component: SubmissionList
          },
          {
            name: 'contest-problem-list',
            path: 'problems',
            component: Contest.ContestProblemList
          },
          {
            name: 'contest-problem-details',
            path: 'problem/:problemID/',
            component: Problem
          },
          {
            name: 'contest-announcement-list',
            path: 'announcements',
            component: Announcements
          },
          {
            name: 'contest-rank',
            path: 'rank',
            component: Contest.ContestRank
          },
          {
            name: 'acm-helper',
            path: 'helper',
            component: Contest.ACMContestHelper
          }
        ]
      },
      {
        name: 'acm-rank',
        path: '/acm-rank',
        meta: {title: 'ACM Rankings'},
        component: ACMRank
      },
      {
        name: 'oi-rank',
        path: '/oi-rank',
        meta: {title: 'OI Rankings'},
        component: OIRank
      },
      {
        name: 'user-home',
        path: '/user-home',
        component: UserHome,
        meta: {requiresAuth: true, title: 'User Home'}
      },
      {
        path: '/setting',
        component: Setting.Settings,
        children: [
          {
            name: 'default-setting',
            path: '',
            meta: {requiresAuth: true, title: 'Default Settings'},
            component: Setting.ProfileSetting
          },
          {
            name: 'profile-setting',
            path: 'profile',
            meta: {requiresAuth: true, title: 'Profile Settings'},
            component: Setting.ProfileSetting
          },
          {
            name: 'account-setting',
            path: 'account',
            meta: {requiresAuth: true, title: 'Account Settings'},
            component: Setting.AccountSetting
          },
          {
            name: 'security-setting',
            path: 'security',
            meta: {requiresAuth: true, title: 'Security Settings'},
            component: Setting.SecuritySetting
          }
        ]
      },
      {
        path: '/about',
        name: 'about',
        meta: {title: 'About'},
        component: About
      },
      {
        path: '/faq',
        name: 'faq',
        meta: {title: 'FAQ'},
        component: FAQ
      },
      {
        path: '*',
        meta: {title: '404'},
        component: NotFound
      }
    ]
  }
]

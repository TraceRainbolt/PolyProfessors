import Vue from 'vue';
import Router from 'vue-router';
import Search from '@/components/Search';
import Results from '@/components/Results';
import Review from '@/components/Review';
import Evaluate from '@/components/Evaluate';
import About from '@/components/About';

Vue.use(Router);

export default new Router({
    mode: 'history',
    meta: {
        title: 'PolyProfessors',
    },
    routes: [
        {
            meta: { title: 'Poly Professors' },
            path: '/',
            name: 'search',
            component: Search,
        },
        {
            meta: { title: 'Search' },
            path: '/results/:terms',
            name: 'results',
            component: Results,
        },
        {
            meta: { title: 'Search' },
            path: '/professors',
            name: 'professors',
            component: Results,
        },
        {
            meta: { title: 'Reviews' },
            path: '/review/:id',
            name: 'review',
            component: Review,
        },
        {
            meta: { title: 'Evaluate' },
            path: '/evaluate/:id',
            name: 'evaluate',
            component: Evaluate,
        },
        {
            meta: { title: 'About' },
            path: '/about',
            name: 'about',
            component: About,
        },
    ],
});

<template>
    <div class="evaluate">
        <h4> Evaluate {{ `${professor[1]} ${professor[2]}` }}</h4>
        <div class="form">
            <div class="info">
                <div class="prof-grade-select">
                    <h5>How would you rate this professor?</h5>
                    <dropdown :options="ratings" :selected="rating"></dropdown>
                </div>
                <div class="course-select">
                    <h5>Select the course:</h5>
                    <dropdown :options="courses" :selected="course" ></dropdown>
                    <input class="course-num" placeholder="101" />
                </div>
                <div class="grade-select">
                    <h5>Select your grade:</h5>
                    <dropdown :options="grades" :selected="grade"></dropdown>
                </div>
                <div class="year-select">
                    <h5>Select your year:</h5>
                    <dropdown :options="years" :selected="year"></dropdown>
                </div>
                <div class="req-select">
                    <h5>Select class fufillment:</h5>
                    <dropdown :options="fufillments" :selected="fufillment"></dropdown>
                </div>
            </div>
            <div class="review">
                <h5>Please enter your review below:</h5>
                <textarea></textarea>
                <button></button>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import Dropdown from '@/components/Dropdown';

export default {
    name: 'Evaluate',
    data() {
        return {
            professor: '',
            courses: [],
            course: { name: 'AERO' },

            grade: { name: 'A' },
            grades: [{ name: 'N/A' },
                { name: 'A' },
                { name: 'B' },
                { name: 'C' },
                { name: 'D' },
                { name: 'F' },
                { name: 'Credit' },
                { name: 'No Credit' }],

            year: { name: 'Freshman' },
            years: [{ name: 'Freshman' },
                { name: 'Sophomore' },
                { name: 'Junior' },
                { name: 'Senior' },
                { name: '5th/6th Year' },
                { name: 'Grad Student' }],

            fufillment: { name: 'Major' },
            fufillments: [{ name: 'Elective' },
                { name: 'General Ed' },
                { name: 'Major' },
                { name: 'Support' }],

            rating: { name: 'A' },
            ratings: [{ name: 'A' },
                { name: 'B' },
                { name: 'C' },
                { name: 'D' },
                { name: 'F' }],

            id: -1,
        };
    },
    components: {
        dropdown: Dropdown,
    },
    methods: {
        render() {
            this.getProfessor();
            this.getReleventCourses();
            this.getCourseList();
        },
        setCourse(payload) {
            this.course = payload;
        },
        getProfessor() {
            this.id = this.$route.params.id;
            const path = `http://localhost:5000/professor?id=${this.id}`;
            axios.get(path)
                .then((res) => {
                    this.professor = res.data;
                    document.title = `${this.professor[1]} ${this.professor[2]} - evaluate`;
                })
                .catch((error) => {
                    this.professor = error;
                });
        },
        getReleventCourses() {
            const path = `http://localhost:5000/courses?id=${this.id}`;
            axios.get(path)
                .then((res) => {
                    this.courses = res.data.map(c => ({ name: c[0] }));
                    this.course = this.courses[0];
                })
                .catch((error) => {
                    this.courses = error;
                });
        },
        getCourseList() {
            const path = 'http://localhost:5000/courses';
            axios.get(path)
                .then((res) => {
                    const newCourses = res.data.map(c => ({ name: c[0] }));
                    this.courses = this.courses.concat(newCourses);
                })
                .catch((error) => {
                    this.courses = error;
                });
        },
    },
    activated() {
        this.render();
    },
    created() {
        this.render();
    },
};
</script>

<style scoped>

input:focus{
    outline: none;
}

textarea {
    width: 765px;
    height: 500px;
    margin-top: 14px;
    padding: 15px;
    font-family: 'Helvetica';
    font-size: 26px;
    border: 1px #AAAAAA solid;
    border-radius: 4px;
    resize: none;
}

textarea:focus {
    outline: none;
    border: 1px green solid;
}

h4 {
    text-align: left;
    font-size: 32px;
    margin: 10px 0;
}

h5 {
    margin: 0;
    padding: 0;
    font-size: 22px;
    text-align: left;
}

.info > div {
    height: 100px;
}

.evaluate {
    position: absolute;
    left: 50%;
    transform: translate(-50%, 0);
}

.form {
    display: grid;
    height: 700px;
    margin-bottom: 120px;
    grid-template-areas:
    'info review';
}

.info {
    display: grid;

    grid-template-areas:
    'course-select'
    'grade-select'
    'year-select'
    'req-select';

    width: 300px;
    padding: 20px 20px;
    border-top: 4px #2c3e50 solid;

    text-align: left;
    background: white;
    border-radius: 2px;
    filter: drop-shadow(0 3px 2px #b9b9b9);
    font-size: 22px;
}

.review {
    border-top: 4px #2c3e50 solid;

    padding: 20px 20px;
    margin-left: 20px;
    width: 800px;
    background: white;
    border-radius: 2px;
    filter: drop-shadow(0 3px 2px #b9b9b9);
    font-size: 22px;
}


.course-num {
    position: relative;
    width: 100px;
    color: #2c3e50;
    font-family: Montserrat;
    padding-bottom: 9px;
    top: 4px;
    left: 30px;
    font-size: 24px;
    border-style: none;
    border-bottom: 1px lightgrey solid;
}

.grade-select {
    position: relative;
    margin-left: 0;
    padding-left: 0;
}

</style>

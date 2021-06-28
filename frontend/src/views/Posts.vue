<template>
  <div>
    <div v-for="(post, i) in posts" :key="i">
      <h1 :key="i">{{ post.description }}</h1>
      <p :key="i">{{ post.body }}</p>
    </div>
    <button class="btn btn-primary">pqp</button>
  </div>
</template>

<script>
//import {getAPI} from '../axios-api'
//import {mapState} from 'vuex'
export default {
  data() {
    return {
      posts: [],
    };
  },
  //computed: mapState(['APIData']),
  mounted() {
    this.fetchPosts();
    document.title = 'Posts';
  },
  methods: {
    fetchPosts() {
      fetch('http://0.0.0.0:8000/api/posts/', {
        method: 'GET',
        headers: {
          Accept: 'application/json',
          Authorization: `Bearer ${this.$store.state.accessToken}`
        },
      })
        .then((response) => {
          if (response.ok) {
            response.json().then((json) => {
              this.posts = json;
            });
          }
        });
    },
  },
};
</script>

<style scoped>
  h1 {
    color: green;
  }
  p {
    color: blue;
  }
</style>

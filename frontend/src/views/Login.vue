<template>
  <div>
      <div class="container text-dark">
        <div class="row justify-content-md-center">
          <div class="col-md-5 p-3 login justify-content-md-center">
            <h1 class="h3 mb-3 text-center">Login</h1>
            <p v-if="incorrectAuth">Incorrect username or password.</p>
            <form v-on:submit.prevent="login">
              <div class="form-group">
                <input type="text" name="username" id="user" v-model="username" class="form-control" placeholder="Username">
              </div><br>
              <div class="form-group">
                <input type="password" name="password" id="pass" v-model="password" class="form-control" placeholder="Password">
              </div><br>
              <div class="d-grid gap-2">
                <button type="submit" class="btn btn-md btn-primary">Login</button>
              </div>
            </form>
          </div>
        </div>
      </div>
  </div>
</template>

<script>
export default {
    data() {
        return {
          username:'',
          password:'',
          incorrectAuth:false
        }
    },
    methods: {
      login(){
        this.$store.dispatch('userLogin', {
          username: this.username,
          password: this.password
        })
        .then(() => {
          this.$router.push({name:'posts'})
        }).catch((err) => {
          console.log(err),
          this.incorrectAuth= true
        });
      }
    }
}
</script>

<style>

</style>
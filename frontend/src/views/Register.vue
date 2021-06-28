<template>
  <div>
    <div class="container text-dark">
      <div class="row justify-content-md-center">
        <div class="col-md-5 p-3 login justify-content-md-center">
          <h1 class="h3 mb-3 text-center">SIGN UP</h1>
          <div class="alert alert-danger" role="alert" v-if="inputError">
            {{ error }}
          </div>
          <form v-on:submit.prevent="submitForm" v-if="!submitted">
            <div class="form-group">
              <input
                type="email"
                name="email"
                id="email"
                v-model="email"
                class="form-control"
                placeholder="E-mail"
              />
            </div>
            <br />
            <div class="form-group">
              <input
                type="text"
                name="username"
                id="user"
                v-model="username"
                class="form-control"
                placeholder="Username"
              />
            </div>
            <br />
            <div class="form-group">
              <input
                type="password"
                name="password"
                id="password"
                v-model="password"
                class="form-control"
                placeholder="Password"
              />
            </div>
            <br />
            <div class="form-group">
              <input
                type="password"
                name="password2"
                id="password2"
                v-model="password2"
                class="form-control"
                placeholder="Confirm Password"
              />
            </div>
            <br />
            <div class="d-grid gap-2">
              <button type="submit" class="btn btn-md btn-primary">
                Register
              </button>
            </div>
          </form>
          <div class="alert alert-info" role="alert" v-if="submitted">
            {{ alertMsg }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      email: "",
      username: "",
      password: "",
      password2: "",
      error: '',
      alertMsg: '',
      submitted: false,
      inputError: false
    };
  },
  methods: {
    submitForm() {
      this.submitted = false
      this.inputError = false
      const formData = {
        email: this.email,
        username: this.username,
        password: this.password,
        password2: this.password2,
      };
      axios
        .post("api/register/", formData)
        .then((response) => {
          this.alertMsg = response.data['response'],
          this.submitted = true
            setTimeout(() => {
              this.$router.push({ name: "login" });
            }, 2000);
        })
        .catch(err => {
          this.inputError = true
          this.error = err.response.data['password']
        });
    },
  },
};
</script>

<style></style>

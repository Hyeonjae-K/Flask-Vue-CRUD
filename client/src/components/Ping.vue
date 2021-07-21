<template>
  <div>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
  ],
});
</script>
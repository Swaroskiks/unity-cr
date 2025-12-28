<template>
  <div class="main-layout">
    <aside class="sidebar">
      <div class="logo glitch" data-text="UNITY" @click="handleLogoClick">
        <h1>UNITY</h1>
      </div>
      <nav class="menu">
        <router-link to="/app/tds" class="menu-item shake-hover" :class="{ active: $route.path.startsWith('/app/tds') }">TDs</router-link>
        <router-link to="/app/project" class="menu-item shake-hover" :class="{ active: $route.path.startsWith('/app/project') }">PROJET</router-link>
        <router-link to="/app/authors" class="menu-item shake-hover" :class="{ active: $route.path.startsWith('/app/authors') }">AUTEURS</router-link>
      </nav>
    </aside>
    <main class="content-area">
      <router-view></router-view>
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const clickCount = ref(0);

const handleLogoClick = () => {
  clickCount.value++;
  if (clickCount.value === 3) {
    router.push('/admin');
    clickCount.value = 0;
  }
  setTimeout(() => {
    if (clickCount.value > 0 && clickCount.value < 3) {
      clickCount.value = 0;
    }
  }, 2000);
};
</script>

<style scoped>
.main-layout {
  display: flex;
  height: 100vh;
  background-color: var(--color-background);
}

.sidebar {
  width: 300px;
  background-color: #000;
  display: flex;
  flex-direction: column;
  padding: 2rem;
  border-right: 2px solid var(--color-primary);
  box-shadow: 5px 0 15px rgba(204, 255, 0, 0.1);
}

.logo {
  margin-bottom: 4rem;
  cursor: pointer;
  user-select: none;
  text-align: center;
}

.logo h1 {
  font-size: 3.5rem;
  color: var(--color-primary);
  text-transform: uppercase;
  font-weight: 900;
  margin: 0;
}

.menu {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.menu-item {
  font-size: 1.8rem;
  color: #666;
  text-decoration: none;
  font-weight: bold;
  padding: 0.5rem;
  border-left: 4px solid transparent;
  transition: all 0.2s;
  text-transform: uppercase;
}

.menu-item:hover, .menu-item.active {
  color: var(--color-text);
  border-left: 4px solid var(--color-primary);
  text-shadow: 0 0 10px var(--color-primary);
  padding-left: 1.5rem;
  background: linear-gradient(90deg, rgba(204, 255, 0, 0.1), transparent);
}

.content-area {
  flex: 1;
  padding: 2rem;
  overflow-y: auto;
  background-color: #0a0a0a;
  background-image: radial-gradient(#151515 1px, transparent 1px);
  background-size: 20px 20px;
}
</style>

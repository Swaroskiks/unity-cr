<template>
  <div class="authors-page">
    <h2 class="page-title glitch" data-text="AUTEURS">AUTEURS</h2>
    
    <div class="authors-grid">
      <div class="author-card" v-for="author in authors" :key="author.name">
        <div class="card-content">
          <div class="avatar-circle">
            <span class="initials">{{ author.initials }}</span>
          </div>
          <h3 class="author-name">{{ author.name }}</h3>
          <p class="author-group">{{ author.group }}</p>
          <a :href="'mailto:' + author.email" class="author-email">{{ author.email }}</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const authors = ref([
  {
    name: 'Mouad MOUSTARZAK',
    initials: 'MM',
    group: 'E4FI Groupe 3I',
    email: 'mouad.moustarzak@edu.esiee.fr'
  },
  {
    name: 'Ibraguim TEMIRKHAEV',
    initials: 'IT',
    group: 'E4FI Groupe 3I',
    email: 'ibraguim.temirkhaev@edu.esiee.fr'
  }
]);
</script>

<style scoped>
.authors-page {
  padding: 2rem;
  color: var(--color-text);
  display: flex;
  flex-direction: column;
  align-items: center;
}

.page-title {
  font-size: 4rem;
  margin-bottom: 4rem;
  color: var(--color-primary);
  text-transform: uppercase;
  font-weight: 900;
  letter-spacing: 5px;
  text-align: center;
}

.authors-grid {
  display: flex;
  gap: 4rem;
  justify-content: center;
  flex-wrap: wrap;
}

.author-card {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid #333;
  padding: 3rem;
  transition: all 0.3s ease;
  width: 500px;
  text-align: center;
  position: relative;
}

.author-card:hover {
  border-color: var(--color-primary);
  transform: translateY(-10px);
  box-shadow: 0 10px 30px rgba(204, 255, 0, 0.1);
}

.avatar-circle {
  width: 120px;
  height: 120px;
  background: #1a1a1a;
  border: 3px solid var(--color-primary);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 2rem auto;
  box-shadow: 0 0 20px rgba(204, 255, 0, 0.2);
}

.initials {
  font-size: 2.5rem;
  font-weight: 900;
  color: var(--color-primary);
}

.author-name {
  font-size: 1.8rem;
  margin: 0 0 0.5rem 0;
  text-transform: uppercase;
  letter-spacing: 1px;
  font-weight: bold;
}

.author-group {
  color: #888;
  font-size: 1.2rem;
  margin-bottom: 1.5rem;
  font-weight: 300;
}

.author-email {
  color: var(--color-text);
  text-decoration: none;
  font-size: 0.9rem;
  padding: 0.5rem 1rem;
  border: 1px solid #444;
  transition: all 0.2s;
  display: block;
  width: fit-content;
  margin: 0 auto;
  word-break: break-all;
}

.author-email:hover {
  background: var(--color-primary);
  color: #000;
  border-color: var(--color-primary);
}
</style>

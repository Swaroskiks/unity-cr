<script setup>
import QuestionsManager from '@/components/QuestionsManager.vue';
</script>

<template>
  <div class="questions-container">
    <QuestionsManager />
  </div>
</template>

<style scoped>
.questions-container {
  max-width: 800px;
  width: 100%;
  margin: 0 auto;
  padding: 2rem 1rem;
  text-align: center;
  min-height: calc(100vh - 60px);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  box-sizing: border-box;
  position: relative;
}

h1 {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  text-align: center;
  margin-bottom: 1.5rem;
  font-size: 2rem;
  font-weight: 700;
  letter-spacing: -0.02em;
}

p {
  color: #6b7280;
  font-size: 1.1rem;
  margin-top: 1rem;
}

</style>


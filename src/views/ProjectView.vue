<template>
  <div class="project-view">
    <div v-if="loading">Chargement...</div>
    <div v-else-if="error">{{ error }}</div>
    <MarkdownViewer v-else :content="content" />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import MarkdownViewer from '../components/MarkdownViewer.vue';

const content = ref('');
const loading = ref(true);
const error = ref('');

const PROJECT_MD_URL = '/project/project.md';

const loadProject = async () => {
  try {
    const response = await fetch(PROJECT_MD_URL);
    if (!response.ok) {
      throw new Error(`Failed to load ${PROJECT_MD_URL}`);
    }
    content.value = await response.text();
  } catch (e) {
    error.value = 'Erreur lors du chargement du projet local.';
    console.error(e);
  } finally {
    loading.value = false;
  }
};

onMounted(loadProject);
</script>

<style scoped>
.project-view {
  width: 100%;
}
</style>

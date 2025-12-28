<template>
  <div class="project-view">
    <div v-if="loading">Chargement...</div>
    <div v-else-if="error">{{ error }}</div>
    <MarkdownViewer v-else :content="content" />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import FileService from '../services/FileService';
import MarkdownViewer from '../components/MarkdownViewer.vue';

const content = ref('');
const loading = ref(true);
const error = ref('');

onMounted(async () => {
  try {
    // Assuming the project file is at content/Projet/project.md or similar
    // We might need to list files first to find it, or hardcode it.
    // Let's assume content/Projet/README.md or similar.
    // For now, let's try to list files in Projet and pick the first one.
    const files = await FileService.listFiles();
    const projectFile = files.find(f => f.startsWith('Projet/'));
    
    if (projectFile) {
      content.value = await FileService.getFile(projectFile);
    } else {
      content.value = '# Projet\n\nAucun fichier de projet trouvé.';
    }
  } catch (e) {
    error.value = 'Erreur lors du chargement du projet.';
    console.error(e);
  } finally {
    loading.value = false;
  }
});
</script>

<style scoped>
.project-view {
  width: 100%;
}
</style>

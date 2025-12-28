<template>
  <div class="tds-view">
    <div v-if="!selectedAuthor" class="author-selection">
      <h2>Choisissez un auteur</h2>
      <div class="authors">
        <button @click="selectAuthor('Mouad')" class="author-btn">Mouad</button>
        <button @click="selectAuthor('Ibraguim')" class="author-btn">Ibraguim</button>
      </div>
    </div>

    <div v-else class="td-content-layout">
      <div class="td-sidebar">
        <button @click="selectedAuthor = null" class="back-btn">← Retour</button>
        <h3>TDs de {{ selectedAuthor }}</h3>
        <ul class="td-list">
          <li v-for="td in tds" :key="td" :class="{ active: selectedTD === td }" @click="selectTD(td)">
            {{ getTDName(td) }}
          </li>
        </ul>
      </div>
      <div class="td-viewer">
        <div v-if="loading">Chargement...</div>
        <MarkdownViewer v-else-if="selectedTD" :content="tdContent" />
        <div v-else class="placeholder">Sélectionnez un TD pour voir son contenu.</div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue';
import FileService from '../services/FileService';
import MarkdownViewer from '../components/MarkdownViewer.vue';

const selectedAuthor = ref<string | null>(null);
const tds = ref<string[]>([]);
const selectedTD = ref<string | null>(null);
const tdContent = ref('');
const loading = ref(false);

const selectAuthor = async (author: string) => {
  selectedAuthor.value = author;
  selectedTD.value = null;
  tdContent.value = '';
  await loadTDs(author);
};

const loadTDs = async (author: string) => {
  try {
    const allFiles = await FileService.listFiles();
    // Filter files for TDs/<Author>
    tds.value = allFiles.filter(f => f.startsWith(`TDs/${author}/`));
  } catch (e) {
    console.error('Error loading TDs', e);
  }
};

const selectTD = async (td: string) => {
  selectedTD.value = td;
  loading.value = true;
  try {
    tdContent.value = await FileService.getFile(td);
  } catch (e) {
    console.error('Error loading TD content', e);
  } finally {
    loading.value = false;
  }
};

const getTDName = (path: string) => {
  return path.split('/').pop()?.replace('.md', '') || path;
};
</script>

<style scoped>
.tds-view {
  height: 100%;
}

.author-selection {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
}

.authors {
  display: flex;
  gap: 2rem;
  margin-top: 2rem;
}

.author-btn {
  padding: 2rem 4rem;
  font-size: 2rem;
  background-color: var(--color-primary);
  color: var(--color-background);
  border: 4px solid var(--color-text);
  cursor: pointer;
  font-weight: bold;
  box-shadow: 8px 8px 0px var(--color-text);
  transition: transform 0.1s;
}

.author-btn:hover {
  transform: translate(-4px, -4px);
  box-shadow: 12px 12px 0px var(--color-text);
}

.td-content-layout {
  display: flex;
  height: 100%;
  gap: 2rem;
}

.td-sidebar {
  width: 250px;
  border-right: 2px solid var(--color-text);
  padding-right: 1rem;
}

.back-btn {
  background: none;
  border: none;
  font-size: 1rem;
  cursor: pointer;
  margin-bottom: 1rem;
  text-decoration: underline;
}

.td-list {
  list-style: none;
  padding: 0;
}

.td-list li {
  padding: 0.5rem;
  cursor: pointer;
  border-bottom: 1px solid #ccc;
}

.td-list li:hover, .td-list li.active {
  background-color: var(--color-primary);
  color: var(--color-background);
  font-weight: bold;
}

.td-viewer {
  flex: 1;
  overflow-y: auto;
}

.placeholder {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  font-size: 1.5rem;
  color: #666;
}
</style>

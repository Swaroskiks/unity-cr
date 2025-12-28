<template>
  <div class="admin-page">
    <div class="sidebar">
      <h2 class="glitch" data-text="ADMIN">ADMIN</h2>
      
      <div class="creation-panel">
        <h3>Nouveau Fichier</h3>
        <div class="form-group">
          <label>Type</label>
          <select v-model="fileType">
            <option value="TD">TD</option>
            <option value="Projet">Projet</option>
          </select>
        </div>

        <div v-if="fileType === 'TD'" class="form-group">
          <label>Auteur</label>
          <select v-model="author">
            <option value="Mouad">Mouad</option>
            <option value="Ibraguim">Ibraguim</option>
          </select>
        </div>

        <div v-if="fileType === 'TD'" class="form-group">
          <label>Numéro TD</label>
          <input type="number" v-model="tdNumber" min="1" placeholder="ex: 1" />
        </div>

        <button @click="initCreate" class="create-btn shake-hover">CRÉER</button>
      </div>

      <div class="file-list-container">
        <h3>Fichiers Existants</h3>
        <ul class="file-list">
          <li v-for="file in files" :key="file" :class="{ active: selectedFile === file }" @click="selectFile(file)">
            {{ file }}
          </li>
        </ul>
      </div>
      
      <router-link to="/" class="back-home">RETOUR SITE</router-link>
    </div>

    <div class="editor-area">
      <div v-if="selectedFile || isCreating" class="editor">
        <div class="toolbar">
          <span class="filename">{{ currentFilename }}</span>
          <div class="actions">
            <input type="file" ref="fileInput" @change="handleFileUpload" style="display: none" accept="image/*" />
            <button @click="triggerUpload" class="upload-btn shake-hover">IMAGE</button>
            <button @click="saveFile" class="save-btn shake-hover">SAUVEGARDER</button>
          </div>
        </div>
        <textarea v-model="fileContent" class="content-editor" spellcheck="false"></textarea>
      </div>
      <div v-else class="placeholder">
        <div class="glitch" data-text="SELECT FILE">SELECT FILE</div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import FileService from '../services/FileService';

const files = ref<string[]>([]);
const selectedFile = ref<string | null>(null);
const fileContent = ref('');
const isCreating = ref(false);

// Form data
const fileType = ref('TD');
const author = ref('Mouad');
const tdNumber = ref(1);

const currentFilename = computed(() => {
  if (selectedFile.value) return selectedFile.value;
  if (isCreating.value) {
    if (fileType.value === 'Projet') return 'Projet/project.md';
    return `TDs/${author.value}/td${tdNumber.value}.md`;
  }
  return '';
});

const loadFiles = async () => {
  try {
    files.value = await FileService.listFiles();
  } catch (e) {
    console.error('Error loading files', e);
  }
};

const selectFile = async (file: string) => {
  selectedFile.value = file;
  isCreating.value = false;
  try {
    fileContent.value = await FileService.getFile(file);
  } catch (e) {
    console.error('Error loading file content', e);
  }
};

const initCreate = () => {
  selectedFile.value = null;
  isCreating.value = true;
  fileContent.value = '# Nouveau Fichier\n\nContenu...';
};

const fileInput = ref<HTMLInputElement | null>(null);

const triggerUpload = () => {
  fileInput.value?.click();
};

const handleFileUpload = async (event: Event) => {
  const target = event.target as HTMLInputElement;
  if (target.files && target.files.length > 0) {
    try {
      const file = target.files[0];
      const url = await FileService.uploadImage(file);
      // Insert markdown image syntax at cursor position or append
      const imageMarkdown = `\n![Image](${url})\n`;
      fileContent.value += imageMarkdown;
      alert('Image uploadée !');
    } catch (e) {
      console.error('Error uploading image', e);
      alert('Erreur lors de l\'upload.');
    }
  }
};

const saveFile = async () => {
  const filename = currentFilename.value;
  if (!filename) return;

  try {
    await FileService.saveFile(filename, fileContent.value);
    await loadFiles();
    if (isCreating.value) {
      selectedFile.value = filename;
      isCreating.value = false;
    }
    alert('Fichier sauvegardé !');
  } catch (e) {
    console.error('Error saving file', e);
    alert('Erreur lors de la sauvegarde.');
  }
};

onMounted(loadFiles);
</script>

<style scoped>
.admin-page {
  display: flex;
  height: 100vh;
  background-color: #000;
  color: #fff;
}

.sidebar {
  width: 350px;
  background-color: #050505;
  border-right: 1px solid #333;
  padding: 2rem;
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.sidebar h2 {
  font-size: 2.5rem;
  color: var(--color-primary);
  margin: 0;
  text-align: center;
}

.creation-panel {
  background: #111;
  padding: 1.5rem;
  border: 1px solid #333;
}

.creation-panel h3 {
  margin-top: 0;
  color: var(--color-secondary);
  font-size: 1.2rem;
  margin-bottom: 1rem;
}

.form-group {
  margin-bottom: 1rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  color: #888;
  font-size: 0.9rem;
}

select, input {
  width: 100%;
  padding: 0.5rem;
  background: #000;
  border: 1px solid #444;
  color: #fff;
  font-family: var(--font-main);
}

select:focus, input:focus {
  border-color: var(--color-primary);
  outline: none;
}

.create-btn {
  width: 100%;
  padding: 0.8rem;
  background: var(--color-primary);
  color: #000;
  border: none;
  font-weight: bold;
  cursor: pointer;
  margin-top: 0.5rem;
}

.file-list-container {
  flex: 1;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.file-list-container h3 {
  color: #888;
  font-size: 1rem;
  margin-bottom: 0.5rem;
}

.file-list {
  flex: 1;
  overflow-y: auto;
  border: 1px solid #333;
}

.file-list li {
  padding: 0.8rem;
  cursor: pointer;
  border-bottom: 1px solid #222;
  color: #aaa;
  transition: all 0.2s;
}

.file-list li:hover, .file-list li.active {
  background-color: #111;
  color: var(--color-primary);
  padding-left: 1.2rem;
}

.back-home {
  text-align: center;
  color: #666;
  text-decoration: none;
  font-size: 0.9rem;
  text-transform: uppercase;
  letter-spacing: 2px;
}

.back-home:hover {
  color: #fff;
}

.editor-area {
  flex: 1;
  display: flex;
  flex-direction: column;
  background-color: #080808;
}

.editor {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.toolbar {
  padding: 1rem 2rem;
  background-color: #111;
  border-bottom: 1px solid #333;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.filename {
  font-family: monospace;
  color: var(--color-accent);
  font-size: 1.2rem;
}

.save-btn {
  background-color: transparent;
  color: var(--color-primary);
  border: 1px solid var(--color-primary);
  padding: 0.5rem 1.5rem;
  cursor: pointer;
  font-weight: bold;
}

.save-btn:hover {
  background-color: var(--color-primary);
  color: #000;
}

.content-editor {
  flex: 1;
  padding: 2rem;
  background-color: #080808;
  color: #ddd;
  font-family: 'Courier New', monospace;
  font-size: 1.1rem;
  border: none;
  resize: none;
  line-height: 1.6;
}

.content-editor:focus {
  outline: none;
}

.placeholder {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  font-size: 3rem;
  color: #222;
  font-weight: bold;
}
</style>

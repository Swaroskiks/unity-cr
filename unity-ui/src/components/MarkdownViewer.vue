<template>
  <div class="markdown-viewer-container">
    <div class="toc" v-if="toc.length > 0">
      <h3>Sommaire</h3>
      <ul>
        <li v-for="(item, index) in toc" :key="index" :class="`toc-level-${item.level}`">
          <a :href="`#${item.slug}`" @click.prevent="scrollTo(item.slug)">{{ item.text }}</a>
        </li>
      </ul>
    </div>
    <div class="markdown-content" v-html="renderedContent"></div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch, onMounted } from 'vue';
import { marked } from 'marked';

const props = defineProps<{
  content: string;
}>();

const renderedContent = ref('');
const toc = ref<{ level: number; text: string; slug: string }[]>([]);

const generateSlug = (text: string) => {
  return text.toLowerCase().replace(/[^\w]+/g, '-');
};

const processContent = async () => {
  if (!props.content) {
    renderedContent.value = '';
    toc.value = [];
    return;
  }

  const renderer = new marked.Renderer();
  const newToc: { level: number; text: string; slug: string }[] = [];

  renderer.heading = ({ text, depth }) => {
    const slug = generateSlug(text);
    newToc.push({ level: depth, text, slug });
    return `<h${depth} id="${slug}">${text}</h${depth}>`;
  };

  renderer.image = ({ href, title, text }) => {
    const isAudio = href && (href.endsWith('.mp3') || href.endsWith('.wav') || href.endsWith('.ogg') || href.includes('/api/audio/'));
    
    let src = href;
    if (href && !href.startsWith('http') && !href.startsWith('data:')) {
      src = `http://127.0.0.1:5001${href}`;
    }

    if (isAudio) {
      return `
        <div class="audio-player">
          <p class="audio-title">${text || 'Audio'}</p>
          <audio controls src="${src}"></audio>
        </div>
      `;
    }
    
    return `<img src="${src}" alt="${text}" title="${title || ''}" />`;
  };

  renderedContent.value = await marked(props.content, { renderer });
  toc.value = newToc;
};

const scrollTo = (slug: string) => {
  const element = document.getElementById(slug);
  if (element) {
    element.scrollIntoView({ behavior: 'smooth' });
  }
};

watch(() => props.content, processContent);
onMounted(processContent);
</script>

<style scoped>
.markdown-viewer-container {
  display: flex;
  gap: 2rem;
}

.toc {
  width: 250px;
  position: sticky;
  top: 0;
  height: fit-content;
  padding: 1rem;
  background-color: var(--color-background);
  border: 2px solid var(--color-text);
  box-shadow: 4px 4px 0px var(--color-text);
}

.toc h3 {
  margin-top: 0;
  border-bottom: 2px solid var(--color-text);
  padding-bottom: 0.5rem;
}

.toc ul {
  list-style: none;
  padding: 0;
}

.toc li {
  margin-bottom: 0.5rem;
}

.toc a {
  text-decoration: none;
  color: var(--color-text);
}

.toc a:hover {
  text-decoration: underline;
}

.toc-level-1 { padding-left: 0; font-weight: bold; }
.toc-level-2 { padding-left: 1rem; }
.toc-level-3 { padding-left: 2rem; }

.markdown-content {
  flex: 1;
  max-width: 800px;
  font-family: var(--font-body);
  font-size: 1.1rem;
  color: #e0e0e0;
  background-color: #111;
  padding: 3rem;
  border-radius: 8px;
  border: 1px solid #333;
  box-shadow: 0 10px 30px rgba(0,0,0,0.5);
}

/* Markdown Styles */
:deep(h1), :deep(h2), :deep(h3), :deep(h4), :deep(h5), :deep(h6) {
  color: var(--color-primary);
  margin-top: 2rem;
  margin-bottom: 1rem;
  font-family: var(--font-main);
  text-transform: uppercase;
  letter-spacing: 1px;
}

:deep(p) {
  line-height: 1.8;
  margin-bottom: 1.5rem;
}

:deep(ul), :deep(ol) {
  margin-bottom: 1.5rem;
  padding-left: 2rem;
}

:deep(li) {
  margin-bottom: 0.5rem;
  line-height: 1.6;
}

:deep(a) {
  color: var(--color-accent);
  text-decoration: none;
  border-bottom: 1px solid transparent;
  transition: border-color 0.2s;
}

:deep(a:hover) {
  border-bottom-color: var(--color-accent);
}

:deep(blockquote) {
  border-left: 4px solid var(--color-secondary);
  margin: 1.5rem 0;
  padding-left: 1rem;
  font-style: italic;
  color: #aaa;
  background: rgba(255, 255, 255, 0.05);
  padding: 1rem;
}

:deep(code) {
  background-color: #222;
  padding: 0.2rem 0.4rem;
  border-radius: 4px;
  font-family: var(--font-main);
  color: var(--color-primary);
  font-size: 0.9em;
}

:deep(pre) {
  background-color: #111;
  color: #fff;
  padding: 1.5rem;
  border-radius: 8px;
  overflow-x: auto;
  margin-bottom: 1.5rem;
  border: 1px solid #333;
}

:deep(img) {
  max-width: 100%;
  border: 1px solid #333;
  box-shadow: 0 4px 8px rgba(0,0,0,0.5);
  margin: 1.5rem 0;
}

:deep(.audio-player) {
  background: #1a1a1a;
  padding: 1.5rem;
  border: 1px solid #333;
  border-radius: 8px;
  margin: 1.5rem 0;
}

:deep(.audio-title) {
  margin-top: 0;
  margin-bottom: 1rem;
  font-size: 0.9rem;
  color: #888;
  text-transform: uppercase;
  letter-spacing: 1px;
}

:deep(audio) {
  width: 100%;
  height: 40px;
  filter: invert(1) hue-rotate(180deg); /* Simple way to make it look better on dark theme */
}

:deep(table) {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 1.5rem;
}

:deep(th), :deep(td) {
  padding: 0.75rem;
  border: 1px solid #333;
  text-align: left;
}

:deep(th) {
  background-color: #111;
  color: var(--color-primary);
  font-family: var(--font-main);
}
</style>

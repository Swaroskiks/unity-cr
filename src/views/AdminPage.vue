<template>
  <div class="admin-page">
    <div class="panel">
      <h2 class="glitch" data-text="MODE STATIQUE">MODE STATIQUE</h2>
      <p class="subtitle">
        L'API a ete retiree. Le contenu est maintenant servi directement depuis le dossier public.
      </p>

      <div class="paths">
        <div class="path-item">
          <span class="label">Markdown principal</span>
          <code>public/project/project.md</code>
        </div>
        <div class="path-item">
          <span class="label">Assets (images, gif, audio)</span>
          <code>public/project/</code>
        </div>
      </div>

      <div class="tips">
        <h3>Bonnes pratiques</h3>
        <ul>
          <li>Utilise des URLs absolues pour les assets, ex: /project/mon-image.png</li>
          <li>Les liens externes (YouTube, Notion) restent inchanges</li>
        </ul>
      </div>

      <router-link to="/" class="back-home">RETOUR SITE</router-link>
    </div>
  </div>
</template>

<style scoped>
.admin-page {
  min-height: 100vh;
  background-color: #000;
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
}

.panel {
  width: 100%;
  max-width: 900px;
  background: #0b0b0b;
  border: 1px solid #333;
  box-shadow: 0 0 30px rgba(0, 0, 0, 0.6);
  padding: 3rem;
}

.panel h2 {
  font-size: 2.8rem;
  color: var(--color-primary);
  margin: 0 0 1rem 0;
  text-align: center;
}

.subtitle {
  color: #aaa;
  text-align: center;
  font-size: 1.1rem;
  margin: 0 0 2.5rem 0;
}

.paths {
  display: grid;
  gap: 1rem;
  margin-bottom: 2rem;
}

.path-item {
  background: #111;
  border: 1px solid #333;
  padding: 1rem 1.25rem;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.label {
  text-transform: uppercase;
  font-size: 0.75rem;
  letter-spacing: 2px;
  color: #666;
}

.path-item code {
  background: #000;
  border: 1px solid #333;
  padding: 0.5rem 0.75rem;
  color: var(--color-accent);
  font-size: 0.95rem;
}

.tips {
  background: #0f0f0f;
  border: 1px solid #333;
  padding: 1.5rem;
  margin-bottom: 2rem;
}

.tips h3 {
  margin: 0 0 1rem 0;
  color: var(--color-secondary);
  font-size: 1.1rem;
}

.tips ul {
  margin: 0;
  padding-left: 1.5rem;
  color: #bbb;
}

.tips li {
  margin-bottom: 0.5rem;
}

.back-home {
  display: inline-block;
  text-align: center;
  color: #666;
  text-decoration: none;
  font-size: 0.9rem;
  text-transform: uppercase;
  letter-spacing: 2px;
  border: 1px solid #333;
  padding: 0.75rem 1.5rem;
}

.back-home:hover {
  color: #fff;
  border-color: var(--color-primary);
  box-shadow: 0 0 10px rgba(204, 255, 0, 0.2);
}
</style>

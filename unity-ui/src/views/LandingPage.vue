<template>
  <div class="landing-container">
    <div class="noise"></div>
    <div class="content">
      <h1 class="title glitch" data-text="PROJET UNITY">PROJET UNITY</h1>
      <p class="description">
        Bienvenue dans l'anxiété.
        <br>
        C'est moche, c'est instable, c'est le projet.
      </p>
      <div class="buttons">
        <router-link to="/app/tds" class="btn shake-hover">VOIR LES TDS</router-link>
        <router-link to="/app/project" class="btn shake-hover">VOIR LE PROJET</router-link>
      </div>
    </div>
  </div>
</template>

<style scoped>
.landing-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: var(--color-background);
  color: var(--color-text);
  text-align: center;
  position: relative;
  overflow: hidden;
}

.noise {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  background: repeating-linear-gradient(
    0deg,
    transparent,
    transparent 1px,
    rgba(255, 255, 255, 0.05) 1px,
    rgba(255, 255, 255, 0.05) 2px
  );
  z-index: 0;
}

.content {
  z-index: 1;
  position: relative;
}

.title {
  font-size: 6rem;
  margin-bottom: 2rem;
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: 0.5rem;
}

.description {
  font-size: 1.5rem;
  margin-bottom: 4rem;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
  color: #888;
  font-family: monospace;
}

.buttons {
  display: flex;
  gap: 3rem;
  justify-content: center;
}

.btn {
  padding: 1.5rem 3rem;
  font-size: 1.5rem;
  background-color: transparent;
  color: var(--color-primary);
  text-decoration: none;
  border: 2px solid var(--color-primary);
  font-weight: bold;
  text-transform: uppercase;
  transition: all 0.1s;
  position: relative;
  overflow: hidden;
}

.btn::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: var(--color-primary);
  transition: left 0.3s;
  z-index: -1;
}

.btn:hover {
  color: var(--color-background);
  box-shadow: 0 0 20px var(--color-primary);
}

.btn:hover::before {
  left: 0;
}
</style>

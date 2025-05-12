import React from 'react';
import Navbar from './components/Navbar';
import Hero from './components/Hero';
import Projects from './components/Projects';
import Skills from './components/Skills';

function App() {
  return (
    <div className="bg-primary min-h-screen">
      <Navbar />
      <main>
        <Hero />
        <Projects />
        <Skills />
      </main>
    </div>
  );
}

export default App;
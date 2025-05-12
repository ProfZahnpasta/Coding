import React, { useEffect, useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Terminal, Github, Linkedin, Mail, Code2 } from 'lucide-react';
import { TypeAnimation } from 'react-type-animation';

const App = () => {
  const [section, setSection] = useState('home');
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const timer = setTimeout(() => {
      setIsLoading(false);
    }, 1500);

    return () => clearTimeout(timer);
  }, []);

  const languages = [
    { name: 'JavaScript', level: 90 },
    { name: 'TypeScript', level: 85 },
    { name: 'Python', level: 80 },
    { name: 'Java', level: 75 },
    { name: 'C++', level: 70 }
  ];

  if (isLoading) {
    return (
      <div className="h-screen flex items-center justify-center bg-black crt">
        <Terminal className="w-16 h-16 text-[#00ff00] animate-pulse" />
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-black text-[#00ff00] crt">
      <div className="code-scroll" />
      
      {/* Navigation */}
      <nav className="fixed top-0 w-full bg-black/90 backdrop-blur-sm border-b border-[#00ff00]/20 z-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-16">
            <div className="flex items-center">
              <Code2 className="h-8 w-8 text-[#00ff00]" />
              <span className="ml-2 text-xl font-bold">ProfZ</span>
            </div>
            <div className="hidden md:flex space-x-8">
              {['home', 'languages', 'about', 'contact'].map((item) => (
                <button
                  key={item}
                  onClick={() => setSection(item)}
                  className={`btn-terminal ${section === item ? 'bg-[#00ff00]/10' : ''}`}
                >
                  {item.charAt(0).toUpperCase() + item.slice(1)}
                </button>
              ))}
            </div>
          </div>
        </div>
      </nav>

      {/* Main Content */}
      <AnimatePresence mode="wait">
        <motion.main
          key={section}
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          exit={{ opacity: 0, y: -20 }}
          transition={{ duration: 0.3 }}
          className="pt-24 px-4 max-w-7xl mx-auto"
        >
          {section === 'home' && (
            <div className="terminal min-h-[60vh] flex flex-col items-center justify-center text-center">
              <TypeAnimation
                sequence={[
                  'Welcome to my terminal.',
                  1000,
                  'I am ProfZ.',
                  1000,
                  'I create digital experiences.',
                  1000
                ]}
                wrapper="h1"
                speed={50}
                className="text-4xl md:text-6xl mb-8"
                repeat={Infinity}
              />
              <p className="text-xl mb-8 opacity-80">
                Full-stack developer // Problem solver // Code enthusiast
              </p>
              <button
                onClick={() => setSection('about')}
                className="btn-terminal text-xl"
              >
                Enter_
              </button>
            </div>
          )}

          {section === 'languages' && (
            <div className="terminal">
              <h2 className="text-3xl mb-8 typing-effect">Programming Languages_</h2>
              <div className="space-y-6">
                {languages.map((lang, index) => (
                  <motion.div
                    key={lang.name}
                    initial={{ opacity: 0, x: -20 }}
                    animate={{ opacity: 1, x: 0 }}
                    transition={{ delay: index * 0.1 }}
                    className="space-y-2"
                  >
                    <div className="flex justify-between">
                      <span>{lang.name}</span>
                      <span>{lang.level}%</span>
                    </div>
                    <div className="h-2 bg-[#00ff00]/20 rounded">
                      <motion.div
                        initial={{ width: 0 }}
                        animate={{ width: `${lang.level}%` }}
                        transition={{ duration: 1, delay: index * 0.1 }}
                        className="h-full bg-[#00ff00] rounded"
                      />
                    </div>
                  </motion.div>
                ))}
              </div>
            </div>
          )}

          {section === 'about' && (
            <div className="terminal">
              <h2 className="text-3xl mb-8 typing-effect">About Me_</h2>
              <div className="space-y-6 text-lg">
                <TypeAnimation
                  sequence={[
                    `Hello, I'm ProfZ. I've been coding for over a decade, turning complex problems into elegant solutions. My journey in software development started with a simple "Hello, World!" and evolved into a passion for creating impactful digital experiences.

                    I specialize in full-stack development, with a particular focus on:
                    - Web Applications
                    - System Architecture
                    - Performance Optimization
                    - Clean Code Practices

                    When I'm not coding, you'll find me exploring new technologies, contributing to open-source projects, or mentoring aspiring developers.`,
                    1000
                  ]}
                  wrapper="div"
                  speed={50}
                  className="whitespace-pre-line"
                />
              </div>
            </div>
          )}

          {section === 'contact' && (
            <div className="terminal">
              <h2 className="text-3xl mb-8 typing-effect">Contact_</h2>
              <form className="space-y-6 max-w-2xl mx-auto">
                <div>
                  <input
                    type="text"
                    placeholder="Name_"
                    className="input-terminal"
                  />
                </div>
                <div>
                  <input
                    type="email"
                    placeholder="Email_"
                    className="input-terminal"
                  />
                </div>
                <div>
                  <textarea
                    placeholder="Message_"
                    rows={5}
                    className="input-terminal resize-none"
                  />
                </div>
                <button type="submit" className="btn-terminal w-full">
                  Send_
                </button>
              </form>
              <div className="flex justify-center space-x-6 mt-8">
                <a href="#" className="btn-terminal p-2">
                  <Github className="w-6 h-6" />
                </a>
                <a href="#" className="btn-terminal p-2">
                  <Linkedin className="w-6 h-6" />
                </a>
                <a href="#" className="btn-terminal p-2">
                  <Mail className="w-6 h-6" />
                </a>
              </div>
            </div>
          )}
        </motion.main>
      </AnimatePresence>
    </div>
  );
};

export default App;
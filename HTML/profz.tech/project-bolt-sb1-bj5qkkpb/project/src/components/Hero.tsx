import React, { useEffect, useRef } from 'react';
import Typed from 'typed.js';

const Hero = () => {
  const el = useRef(null);

  useEffect(() => {
    const typed = new Typed(el.current, {
      strings: ['ProfZ', 'Developer', 'Creator'],
      typeSpeed: 100,
      backSpeed: 50,
      loop: true,
      backDelay: 1500
    });

    return () => {
      typed.destroy();
    };
  }, []);

  return (
    <div className="relative h-screen flex items-center justify-center overflow-hidden bg-primary">
      {/* Particle effect background */}
      <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,_var(--tw-gradient-stops))] from-secondary/20 via-primary to-primary"></div>
      
      {/* Content */}
      <div className="relative z-10 text-center">
        <h1 className="text-4xl md:text-6xl lg:text-7xl font-bold text-white mb-4">
          I am <span ref={el} className="text-secondary"></span>
        </h1>
        <p className="text-light-gray text-lg md:text-xl max-w-2xl mx-auto px-4">
          Transforming ideas into elegant digital solutions
        </p>
        <div className="mt-8">
          <a
            href="#projects"
            className="bg-secondary hover:bg-secondary/90 text-white px-8 py-3 rounded-full font-medium transition-all duration-300 hover:shadow-lg hover:shadow-secondary/50"
          >
            View My Work
          </a>
        </div>
      </div>

      {/* Animated gradient background */}
      <div className="absolute inset-0 bg-gradient-to-r from-primary via-secondary/20 to-primary opacity-30 animate-gradient"></div>
    </div>
  );
};

export default Hero;
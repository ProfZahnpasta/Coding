import React from 'react';
import { TypeAnimation } from 'react-type-animation';
import ParticlesBackground from './ParticlesBackground';

const Hero = () => {
  return (
    <div id="home" className="relative h-screen flex items-center justify-center overflow-hidden">
      <ParticlesBackground />
      <div className="z-10 text-center px-4">
        <h1 className="text-4xl md:text-6xl font-bold text-white mb-6">
          <TypeAnimation
            sequence={[
              'ProfZ',
              1000,
              'Developer',
              1000,
              'Creator',
              1000
            ]}
            wrapper="span"
            speed={50}
            repeat={Infinity}
          />
        </h1>
        <p className="text-lg md:text-xl text-gray-300 max-w-2xl mx-auto">
          Crafting digital experiences with code and creativity
        </p>
        <button className="mt-8 px-6 py-3 bg-purple-600 text-white rounded-full hover:bg-purple-700 transition-colors duration-300">
          View My Work
        </button>
      </div>
      <div className="absolute bottom-10 left-1/2 transform -translate-x-1/2 animate-bounce">
        <div className="w-6 h-10 border-2 border-white rounded-full flex justify-center">
          <div className="w-1 h-3 bg-white rounded-full mt-2 animate-scroll"></div>
        </div>
      </div>
    </div>
  );
};

export default Hero;
import React, { useCallback } from 'react';
import { loadSlim } from "tsparticles-slim";
import type { Engine } from "tsparticles-engine";
import { useEffect, useState } from "react";

const ParticlesBackground = () => {
  const [init, setInit] = useState(false);

  const particlesInit = useCallback(async (engine: Engine) => {
    await loadSlim(engine);
    setInit(true);
  }, []);

  useEffect(() => {
    if (typeof window !== 'undefined' && !init) {
      import('tsparticles-engine').then((module) => {
        module.tsParticles.load("tsparticles", {
          particles: {
            number: {
              value: 80,
              density: {
                enable: true,
                value_area: 800
              }
            },
            color: {
              value: "#8A2BE2"
            },
            shape: {
              type: "circle"
            },
            opacity: {
              value: 0.5,
              random: false
            },
            size: {
              value: 3,
              random: true
            },
            links: {
              enable: true,
              distance: 150,
              color: "#8A2BE2",
              opacity: 0.4,
              width: 1
            },
            move: {
              enable: true,
              speed: 2,
              direction: "none",
              random: false,
              straight: false,
              outModes: {
                default: "out"
              },
              bounce: false
            }
          },
          interactivity: {
            detectsOn: "canvas",
            events: {
              onHover: {
                enable: true,
                mode: "repulse"
              },
              onClick: {
                enable: true,
                mode: "push"
              },
              resize: true
            }
          },
          retina_detect: true
        }).then(() => {
          particlesInit(module.tsParticles.engine);
        });
      });
    }
  }, [init, particlesInit]);

  return (
    <div id="tsparticles" className="absolute inset-0" />
  );
};

export default ParticlesBackground;
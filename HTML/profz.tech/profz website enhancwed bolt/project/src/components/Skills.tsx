import React from 'react';
import { motion } from 'framer-motion';
import { useInView } from 'react-intersection-observer';

const skills = {
  Frontend: ['React', 'Vue.js', 'TypeScript', 'Tailwind CSS', 'Next.js'],
  Backend: ['Node.js', 'Python', 'Java', 'PostgreSQL', 'MongoDB'],
  Tools: ['Git', 'Docker', 'AWS', 'Linux', 'VS Code'],
  Languages: ['JavaScript', 'Python', 'Java', 'C++', 'Go']
};

const Skills = () => {
  const [ref, inView] = useInView({
    triggerOnce: true,
    threshold: 0.1
  });

  return (
    <section id="skills" className="py-20 bg-gradient-to-b from-black to-purple-900">
      <div ref={ref} className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <motion.h2
          initial={{ opacity: 0, y: 20 }}
          animate={inView ? { opacity: 1, y: 0 } : {}}
          transition={{ duration: 0.6 }}
          className="text-4xl font-bold text-white text-center mb-12"
        >
          Skills & Expertise
        </motion.h2>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          {Object.entries(skills).map(([category, items], categoryIndex) => (
            <motion.div
              key={category}
              initial={{ opacity: 0, y: 20 }}
              animate={inView ? { opacity: 1, y: 0 } : {}}
              transition={{ duration: 0.6, delay: categoryIndex * 0.2 }}
              className="bg-black/50 backdrop-blur-lg rounded-lg p-6"
            >
              <h3 className="text-xl font-bold text-white mb-4">{category}</h3>
              <div className="space-y-4">
                {items.map((skill, index) => (
                  <div key={skill} className="space-y-2">
                    <div className="flex justify-between text-sm text-white">
                      <span>{skill}</span>
                      <span className="text-purple-400">
                        {90 - index * 5}%
                      </span>
                    </div>
                    <div className="h-2 bg-purple-900/50 rounded-full overflow-hidden">
                      <motion.div
                        initial={{ width: 0 }}
                        animate={inView ? { width: `${90 - index * 5}%` } : {}}
                        transition={{ duration: 1, delay: categoryIndex * 0.2 + index * 0.1 }}
                        className="h-full bg-gradient-to-r from-purple-600 to-purple-400 rounded-full"
                      />
                    </div>
                  </div>
                ))}
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Skills;
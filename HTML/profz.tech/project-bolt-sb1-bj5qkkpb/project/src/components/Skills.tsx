import React from 'react';
import { motion } from 'framer-motion';

const skills = {
  Frontend: ['React', 'Vue.js', 'TypeScript', 'Tailwind CSS'],
  Backend: ['Node.js', 'Python', 'PostgreSQL', 'GraphQL'],
  Tools: ['Git', 'Docker', 'AWS', 'CI/CD'],
  Languages: ['JavaScript', 'Python', 'Go', 'Rust']
};

const SkillBar = ({ skill, index }: { skill: string; index: number }) => {
  const randomProgress = Math.floor(Math.random() * 30) + 70; // 70-100%

  return (
    <motion.div
      initial={{ opacity: 0, x: -50 }}
      animate={{ opacity: 1, x: 0 }}
      transition={{ duration: 0.5, delay: index * 0.1 }}
      className="mb-4"
    >
      <div className="flex justify-between mb-1">
        <span className="text-light-gray">{skill}</span>
        <span className="text-secondary">{randomProgress}%</span>
      </div>
      <div className="h-2 bg-gray-700 rounded-full overflow-hidden">
        <motion.div
          initial={{ width: 0 }}
          animate={{ width: `${randomProgress}%` }}
          transition={{ duration: 1, delay: index * 0.1 }}
          className="h-full bg-gradient-to-r from-secondary to-accent rounded-full"
        />
      </div>
    </motion.div>
  );
};

const Skills = () => {
  return (
    <section id="skills" className="py-20 bg-primary">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 className="text-4xl font-bold text-center text-white mb-12">
          Technical <span className="text-secondary">Skills</span>
        </h2>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-12">
          {Object.entries(skills).map(([category, categorySkills], categoryIndex) => (
            <div
              key={category}
              className="bg-black/50 p-6 rounded-xl backdrop-blur-sm"
            >
              <h3 className="text-2xl font-bold text-secondary mb-6">{category}</h3>
              <div>
                {categorySkills.map((skill, index) => (
                  <SkillBar
                    key={skill}
                    skill={skill}
                    index={index + categoryIndex * 4}
                  />
                ))}
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Skills;
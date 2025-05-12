// Typed.js initialization
document.addEventListener('DOMContentLoaded', function() {
    new Typed('#typed-text', {
        strings: ['ProfZ', 'Developer', 'Creator'],
        typeSpeed: 50,
        backSpeed: 50,
        backDelay: 1000,
        loop: true
    });

    // Initialize particles
    tsParticles.load("tsparticles", {
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
    });

    // Projects data
    const projects = [
        {
            title: 'E-Commerce Platform',
            description: 'A full-stack e-commerce solution with real-time inventory management',
            image: 'https://images.unsplash.com/photo-1661956602116-aa6865609028?ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=764&q=80',
            tech: ['React', 'Node.js', 'MongoDB', 'Redux'],
            demo: 'https://example.com',
            github: 'https://github.com'
        },
        {
            title: 'AI Task Manager',
            description: 'Smart task management app with AI-powered prioritization',
            image: 'https://images.unsplash.com/photo-1518770660439-4636190af475?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=870&q=80',
            tech: ['Python', 'TensorFlow', 'FastAPI', 'React'],
            demo: 'https://example.com',
            github: 'https://github.com'
        },
        {
            title: 'Social Media Dashboard',
            description: 'Unified dashboard for managing multiple social media accounts',
            image: 'https://images.unsplash.com/photo-1611162617474-5b21e879e113?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=774&q=80',
            tech: ['Vue.js', 'Firebase', 'Node.js', 'Express'],
            demo: 'https://example.com',
            github: 'https://github.com'
        }
    ];

    // Skills data
    const skills = {
        Frontend: ['React', 'Vue.js', 'TypeScript', 'Tailwind CSS', 'Next.js'],
        Backend: ['Node.js', 'Python', 'Java', 'PostgreSQL', 'MongoDB'],
        Tools: ['Git', 'Docker', 'AWS', 'Linux', 'VS Code'],
        Languages: ['JavaScript', 'Python', 'Java', 'C++', 'Go']
    };

    // Render projects
    const projectsGrid = document.getElementById('projects-grid');
    projects.forEach(project => {
        const projectCard = document.createElement('div');
        projectCard.className = 'project-card relative group overflow-hidden rounded-lg';
        projectCard.innerHTML = `
            <div class="aspect-w-16 aspect-h-9">
                <img src="${project.image}" alt="${project.title}" class="object-cover w-full h-full transform group-hover:scale-110 transition-transform duration-300">
            </div>
            <div class="absolute inset-0 bg-gradient-to-b from-transparent to-black/90 group-hover:from-purple-900/50 group-hover:to-black transition-all duration-300">
                <div class="absolute bottom-0 p-6 space-y-3">
                    <h3 class="text-xl font-bold text-white">${project.title}</h3>
                    <p class="text-gray-300 text-sm">${project.description}</p>
                    <div class="flex flex-wrap gap-2">
                        ${project.tech.map(tech => `
                            <span class="text-xs bg-purple-600/50 text-white px-2 py-1 rounded">${tech}</span>
                        `).join('')}
                    </div>
                    <div class="flex space-x-4 pt-2">
                        <a href="${project.github}" class="text-white hover:text-purple-400 transition-colors">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/>
                            </svg>
                        </a>
                        <a href="${project.demo}" class="text-white hover:text-purple-400 transition-colors">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/>
                                <polyline points="15 3 21 3 21 9"/>
                                <line x1="10" y1="14" x2="21" y2="3"/>
                            </svg>
                        </a>
                    </div>
                </div>
            </div>
        `;
        projectsGrid.appendChild(projectCard);
    });

    // Render skills
    const skillsGrid = document.getElementById('skills-grid');
    Object.entries(skills).forEach(([category, items], categoryIndex) => {
        const skillCard = document.createElement('div');
        skillCard.className = 'bg-black/50 backdrop-blur-lg rounded-lg p-6';
        skillCard.innerHTML = `
            <h3 class="text-xl font-bold text-white mb-4">${category}</h3>
            <div class="space-y-4">
                ${items.map((skill, index) => `
                    <div class="space-y-2">
                        <div class="flex justify-between text-sm text-white">
                            <span>${skill}</span>
                            <span class="text-purple-400">${90 - index * 5}%</span>
                        </div>
                        <div class="h-2 bg-purple-900/50 rounded-full overflow-hidden">
                            <div class="skill-bar h-full bg-gradient-to-r from-purple-600 to-purple-400 rounded-full" style="width: ${90 - index * 5}%"></div>
                        </div>
                    </div>
                `).join('')}
            </div>
        `;
        skillsGrid.appendChild(skillCard);
    });
});

// Mobile menu toggle
function toggleMenu() {
    const mobileMenu = document.getElementById('mobile-menu');
    mobileMenu.classList.toggle('hidden');
}

// Navbar scroll effect
window.addEventListener('scroll', function() {
    const navbar = document.getElementById('navbar');
    if (window.scrollY > 20) {
        navbar.classList.add('navbar-scrolled');
    } else {
        navbar.classList.remove('navbar-scrolled');
    }
});
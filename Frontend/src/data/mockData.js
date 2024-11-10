// src/data/mockData.js

const projects = [
    {
      id: 1,
      name: "EcoTech Solutions",
      description: "EcoTech Solutions is revolutionizing the way we approach sustainable energy. Our innovative solar panel technology increases efficiency by 30% while reducing production costs.",
      logo: "/placeholder.svg?height=100&width=100",
      fundingGoal: 1000000,
      currentFunding: 750000,
      endDate: "2023-12-31",
      milestones: [
        { title: "Prototype Development", date: "2023-06-30", completed: true },
        { title: "Patent Filing", date: "2023-08-15", completed: true },
        { title: "Pilot Installation", date: "2023-11-30", completed: false },
        { title: "Mass Production", date: "2024-03-31", completed: false },
      ],
      team: [
        { name: "Jane Doe", role: "CEO", avatar: "/placeholder.svg?height=50&width=50" },
        { name: "John Smith", role: "CTO", avatar: "/placeholder.svg?height=50&width=50" },
        { name: "Alice Johnson", role: "Lead Engineer", avatar: "/placeholder.svg?height=50&width=50" },
      ],
      nfts: [
        { id: 1, name: "Early Supporter", price: 500, image: "/placeholder.svg?height=150&width=150" },
        { id: 2, name: "Green Innovator", price: 1000, image: "/placeholder.svg?height=150&width=150" },
        { id: 3, name: "Eco Warrior", price: 2500, image: "/placeholder.svg?height=150&width=150" },
      ],
      updates: [
        { date: "2023-09-15", title: "Milestone Achieved", content: "We're excited to announce that we've successfully completed our prototype development phase!" },
        { date: "2023-10-01", title: "New Partnership", content: "EcoTech Solutions has partnered with GreenEnergy Corp to expand our distribution network." },
      ],
      faqs: [
        { question: "How does your technology differ from traditional solar panels?", answer: "Our panels use advanced nanotechnology to capture a broader spectrum of light, resulting in higher efficiency." },
        { question: "What's your projected ROI for investors?", answer: "We project a 15-20% annual return on investment over the next 5 years, based on current market trends and our growth projections." },
      ],
    },
    // Add more projects as needed
  ];
  
  export const getProjects = () => {
    return new Promise((resolve) => {
      resolve(projects);
    });
  };
  
  export const getProjectById = (id) => {
    return new Promise((resolve, reject) => {
      const project = projects.find((project) => project.id === id);
      if (project) {
        resolve(project);
      } else {
        reject(new Error("Project not found"));
      }
    });
  };
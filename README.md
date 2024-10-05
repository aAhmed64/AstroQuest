Here’s an improved version of your GitHub README for **Astro Quest**, incorporating the updated data and providing a clearer structure. I also included the link to your main website:

---

# Astro Quest

**Astro Quest** is an innovative project developed for the NASA Space Apps Challenge, aimed at solving real-world challenges by leveraging space science and technologies. This immersive VR simulation allows users to explore and gain insights into space-related data through interactive tools and educational resources, making space exploration accessible to both the general public and researchers.

## Try It Out

Experience Astro Quest live by visiting our website: [Astro Quest](https://asatan64.github.io/AstroQuest/)


## Table of Contents
1. [Project Overview](#project-overview)
2. [Motivation](#motivation)
3. [Features](#features)
4. [Technology Stack](#technology-stack)
5. [Installation Guide](#installation-guide)
6. [Usage](#usage)
7. [Contributors](#contributors)
8. [License](#license)
9. [Try It Out](#try-it-out)


## Project Overview

Astro Quest is designed to:
- Analyze and visualize data from NASA's public API.
- Provide real-time information about space events, such as meteor showers and planetary positions.
- Enable users to explore the solar system through an interactive VR interface.
- Help identify and track celestial objects like asteroids and satellites.

By simplifying access to space data, Astro Quest brings the wonders of the universe closer to the public and makes space exploration engaging for everyone.

## Motivation

The driving force behind Astro Quest is our passion for space and the desire to make space data accessible to everyone. The NASA Space Apps Challenge provides a platform to showcase how technology can be utilized to solve problems and contribute to scientific discovery.

Our goals include:
- Inspiring curiosity about space.
- Assisting researchers with advanced data analysis tools.
- Promoting STEM education through interactive and enjoyable learning experiences.

## Features

- **Interactive VR Solar System Explorer**: Experience an immersive 3D visualization of the solar system, allowing users to navigate through celestial bodies.
- **Real-Time Space Events**: Stay updated with upcoming space events, including meteor showers, eclipses, and satellite launches.
- **Data Visualization**: Graphical representation of space data such as asteroid trajectories and space weather phenomena.
- **Search and Filter**: Easily search for and filter information about specific celestial objects, enhancing the learning experience.
- **Educational Resources**: Access comprehensive information about various planets, stars, galaxies, and their significance in our universe.

## Technology Stack

- **Frontend**: HTML, CSS, JavaScript, Three.js (for 3D visualizations)
- **Backend**: Python, Flask
- **APIs**: NASA APIs (NeoWs, Mars Rover Photos, etc.), SpaceWeather API
- **Database**: SQLite (for data caching and storing user preferences)
- **Additional Tools**: Tesseract OCR (for space-related document reading), Google Text-to-Speech

## Installation Guide

### Prerequisites
- Python 3.x
- Bootstrap
- Git
- Any modern web browser

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/astro-quest.git
   ```
2. Navigate into the project directory:
   ```bash
   cd astro-quest
   ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   ```bash
   export NASA_API_KEY=your_nasa_api_key
   export FLASK_APP=astro_quest
   ```
5. Run the application:
   ```bash
   flask run
   ```
6. Open your web browser and visit:
   ```
   http://127.0.0.1:5000
   ```

## Usage

Once installed and running, you can:
1. **Explore the Solar System**: Navigate through the solar system using the interactive 3D model.
2. **Check Space Events**: View upcoming meteor showers, eclipses, and satellite launches.
3. **Search for Celestial Bodies**: Enter the name of an asteroid or planet to access detailed information.
4. **Learn**: Access educational resources about space phenomena, astronomy, and NASA missions.

## Contributors

- **Ahmed Mahmoud Gaballah** - Lead Developer
- **Amr Bassem Farouk** - Developer
- **Yassin Bassem Farouk** - Researcher
- **Ali Mahmoud Shaddad** - Researcher
- **Abdelrahman** - Researcher

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.


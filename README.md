
# Astro Quest

**Astro Quest** is an innovative project developed for the NASA Space Apps Challenge, designed to solve real-world challenges by leveraging space and science technologies. Our aim is to explore and provide insights into space-related data, helping researchers, scientists, and the general public gain a deeper understanding of our universe.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Motivation](#motivation)
3. [Features](#features)
4. [Technology Stack](#technology-stack)
5. [Installation Guide](#installation-guide)
6. [Usage](#usage)
7. [Contributors](#contributors)
8. [License](#license)

![Uploading image.png…]()

## Project Overview

Astro Quest is designed to:
- Analyze and visualize data from NASA's public API
- Provide real-time information about space events, such as meteor showers and planetary positions
- Enable users to explore the solar system through an interactive interface
- Help identify and track celestial objects like asteroids and satellites

The project brings space closer to the public by simplifying access to data and making space exploration engaging for everyone.

## Motivation

The driving force behind Astro Quest is the passion for space and the desire to make space data accessible to everyone. The NASA Space Apps Challenge is the perfect platform to showcase how technology can be used to solve problems and contribute to scientific discovery.

Our goal is to:
- Inspire curiosity about space
- Assist researchers with advanced data analysis tools
- Promote STEM education through interactive and fun learning experiences

## Features

- **Interactive Solar System Explorer**: Navigate through the solar system with 3D visualizations.
- **Real-Time Space Events**: Stay updated with upcoming space events and news.
- **Data Visualization**: Graphical representation of space data such as asteroid trajectories, space weather, etc.
- **Search and Filter**: Easily search for and filter information about specific celestial objects.
- **Educational Resources**: Learn about different planets, stars, and galaxies.

## Technology Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript, Three.js (for 3D visualizations)
- **APIs**: NASA APIs (NeoWs, Mars Rover Photos, etc.), SpaceWeather API
- **Database**: SQLite (for data caching and storing user preferences)
- **Others**: Tesseract OCR (for space-related document reading), Google Text-to-Speech

## Installation Guide

### Prerequisites
- Python 3.x
- Flask
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
1. **Explore the Solar System**: Use the interactive 3D model to explore planets and their moons.
2. **Check Space Events**: View upcoming meteor showers, eclipses, and satellite launches.
3. **Search for Celestial Bodies**: Enter the name of an asteroid or planet to view detailed information.
4. **Learn**: Access educational resources about space phenomena, astronomy, and NASA missions.

## Contributors

- Ahmed Mahmoud Gaballah - Lead Developer
- Amr Bassem Farouk - Developer
- Yassin Bassem Farouk- Researcher
- Ali Mahmoud Shaddad-  Researcher
- Abdelrahman - Researcher
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

# ⚠️ THIS SECTION IS A WIP, SOME INFORMATION MAY BE INCORRECT OR INCOMPLETE ⚠️
# Warhammer Fantasy Roleplay 2nd Edition Virtual Tabletop (VTT)

Welcome to the Warhammer Fantasy Roleplay 2nd Edition Virtual Tabletop (VTT) project! This project aims to provide a comprehensive and user-friendly virtual tabletop experience for Warhammer Fantasy Roleplay 2nd Edition, allowing players and game masters to easily manage their games  online.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Character Management**: Create, edit, and manage player characters and NPCs with ease.
- [WIP] **Combat Tracker**: Easily track combat encounters, initiative, and statuses.
- **Map and Token Management**: Upload and manage maps, place tokens, and control visibility.
- **Dice Roller**: Integrated dice roller supporting all Warhammer Fantasy Roleplay 2nd Edition mechanics.
- [WIP] **Handouts and Notes**: Share handouts and keep game notes accessible to all players.
- **Audio Integration**: Play ambient sounds and music to enhance the gaming experience.
- [WIP] **Customizable UI**: Tailor the interface to fit your group's needs and preferences.
- **Secure and Reliable**: Ensure data integrity and security with robust backend solutions.

## Installation

To get started with the Warhammer Fantasy Roleplay 2nd Edition VTT, follow these steps:

### Prerequisites

- [Python](https://www.python.org/) (version 3.7 or higher)
- [pip](https://pip.pypa.io/en/stable/) (version 20 or higher)

### Clone the Repository

```bash
git clone https://github.com/wkrzos/bardzofajenvtt.git
cd bardzofajenvtt
```

### Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file in the root directory and add your environment variables. For example:

```
MONGO_URI=mongodb://localhost:27017/bardzofajenvtt
SECRET_KEY=your_secret_key
```

### Run the Application

```bash
flask run
```

## Usage

### Creating a Game
Currently the app supports hot-seat only mode:
1. Run the applicataion.
2. Choose the language.
3. You're all set.

### Managing Characters

1. Navigate to the "Characters" section.
2. Click "Add Character" and enter the character details.
3. Edit or update character information as needed.

### [WIP] Running a Session

1. Use the "Combat Tracker" to manage encounters.
2. Upload maps and place tokens for visual representation.
3. Roll dice using the integrated dice roller.
4. Share handouts and keep notes accessible in the "Handouts" section.

## Contributing

We welcome contributions from the community! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

Please ensure your code follows our [Code of Conduct](CODE_OF_CONDUCT.md) and [Contributing Guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions, issues, or suggestions, feel free to reach out:

- **Email**: [wip]
- **GitHub Issues**: [Issues Page](https://github.com/wkrzos/bardzofajenvtt/issues)

We hope you enjoy using the Warhammer Fantasy Roleplay 2nd Edition VTT! Happy gaming!

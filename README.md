# Site

A cross-platform application built with Flet framework, supporting desktop, web, and mobile platforms.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Building for Production](#building-for-production)
- [Project Structure](#project-structure)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## Overview

This is a Flet-based application that can be deployed across multiple platforms including web browsers, desktop operating systems (Windows, macOS, Linux), and mobile devices (Android, iOS).

## Features

- Cross-platform compatibility
- Modern UI with Flet framework
- Support for desktop, web, and mobile deployment
- Built with Python for rapid development
- Responsive design

## Prerequisites

Before you begin, ensure you have one of the following installed:

- **Python 3.9 or higher**
- **uv** (recommended for faster dependency management)
- **Poetry** (alternative package manager)

## Installation

### Using uv (Recommended)

```bash
# Install uv if you haven't already
pip install uv

# Install dependencies
uv sync
```

### Using Poetry

```bash
# Install Poetry if you haven't already
pip install poetry

# Install dependencies
poetry install
```

## Running the Application

### Development Mode

#### With uv

Run as a desktop application:

```bash
uv run flet run
```

Run as a web application:

```bash
uv run flet run --web
```

#### With Poetry

Run as a desktop application:

```bash
poetry run flet run
```

Run as a web application:

```bash
poetry run flet run --web
```

For more details on running the app, refer to the [Flet Getting Started Guide](https://flet.dev/docs/getting-started/).

## Building for Production

### Android

Build an APK package:

```bash
flet build apk -v
```

For more details on building and signing `.apk` or `.aab` files, refer to the [Android Packaging Guide](https://flet.dev/docs/publish/android/).

### iOS

Build an IPA package:

```bash
flet build ipa -v
```

Note: iOS builds require a macOS environment with Xcode installed.

For more details on building and signing `.ipa` files, refer to the [iOS Packaging Guide](https://flet.dev/docs/publish/ios/).

### macOS

Build a macOS application bundle:

```bash
flet build macos -v
```

For more details on building macOS packages, refer to the [macOS Packaging Guide](https://flet.dev/docs/publish/macos/).

### Linux

Build a Linux package:

```bash
flet build linux -v
```

For more details on building Linux packages, refer to the [Linux Packaging Guide](https://flet.dev/docs/publish/linux/).

### Windows

Build a Windows executable:

```bash
flet build windows -v
```

For more details on building Windows packages, refer to the [Windows Packaging Guide](https://flet.dev/docs/publish/windows/).

### Web

Build for web deployment:

```bash
flet build web -v
```

The built files will be available in the `build/web` directory.

## Project Structure

```
Site/
├── src/                    # Source code directory
│   ├── main.py            # Main application entry point
│   └── assets/            # Application assets
├── storage/               # Storage directory (gitignored)
│   ├── data/             # Application data
│   └── temp/             # Temporary files
├── build/                 # Build outputs (gitignored)
├── pyproject.toml        # Project configuration and dependencies
├── README.md             # This file
├── LICENSE               # License information
├── .gitignore            # Git ignore rules
└── .gitattributes        # Git attributes configuration
```

## Development

### Code Structure

The main application logic is located in `src/main.py`. You can add additional Python modules in the `src` directory as your application grows.

### Dependencies

Dependencies are managed through `pyproject.toml`. The project uses:

- **Flet 0.28.3** - The main framework for building the UI

To add new dependencies:

With uv:
```bash
uv add package-name
```

With Poetry:
```bash
poetry add package-name
```

### Hot Reload

Flet supports hot reload during development. Changes to your Python files will automatically reload the application when running in development mode.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Resources

- [Flet Documentation](https://flet.dev/docs/)
- [Flet Examples](https://flet.dev/docs/examples/)
- [Flet GitHub Repository](https://github.com/flet-dev/flet)
- [Python Documentation](https://docs.python.org/3/)
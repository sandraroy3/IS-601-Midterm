# Advanced Python Calculator

## Project Overview

The Advanced Python Calculator is a command-line (REPL) application developed as part of a Software Engineering graduate course. It is designed to showcase professional software development practices, such as clean and maintainable code, the application of design patterns, dynamic configuration via environment variables, comprehensive logging, and data handling with Pandas. The calculator provides basic arithmetic operations, supports a plugin system for extensibility, and enables efficient history management.

## Project Submission

You are required to create a new repository and maintain a clear commit history as you work on the assignment. The repository should contain relevant documentation, configuration examples, and code for all components of the project. A short video demonstration (3-5 minutes) of the calculator should be created, highlighting its key features and functionalities. The project must also pass all tests using GitHub Actions.

## Core Functionalities

### Command Line Interface (REPL)

The calculator supports the following functionalities through the REPL interface:

- **Arithmetic Operations**: Addition, subtraction, multiplication, and division.
- **History Management**: The REPL interface allows users to access and manage calculation history.
- **Plugin System**: Supports integration of new commands via dynamically loaded plugins, extending the calculator’s capabilities.

### Plugin System

The plugin system enables the integration of new features without modifying the core application code. This system provides:

- **Dynamic Plugin Integration**: New commands can be added seamlessly.
- **Menu Command**: A `menu` command to list all available plugin commands, ensuring ease of use and discoverability.

### Calculation History Management

Pandas is used to manage a robust calculation history. Users can:

- Load, save, clear, and delete history records directly through the REPL interface.
- Efficiently store and manipulate historical calculation data in CSV files.

### Professional Logging Practices

Logging is implemented in the application to track operations, data manipulations, and errors. Features include:

- **Log Levels**: Logs differentiate between informational messages, warnings, and errors.
- **Dynamic Logging Configuration**: Log levels and output destinations can be adjusted using environment variables.

### Advanced Data Handling with Pandas

Pandas is utilized for efficient data handling, including:

- Reading and writing calculation history to and from CSV files.
- Managing and manipulating the calculation history with a DataFrame for easy access and storage.

### Design Patterns for Scalable Architecture

Key design patterns are applied to improve the flexibility and scalability of the application:

- **Facade Pattern**: Simplifies complex Pandas data operations.
- **Command Pattern**: Structures commands within the REPL for effective execution and history management.
- **Factory Method, Singleton, and Strategy Patterns**: These patterns further enhance the modularity, flexibility, and scalability of the application.

## Testing and Code Quality

### Testing

- Achieve a minimum of **90% test coverage** using **Pytest**.
- All code should adhere to **PEP 8 standards**, verified by **Pylint**.
- Unit tests should cover all critical components, ensuring the functionality of the calculator, plugin system, and history management.

### Code Quality

- Ensure clean, maintainable code through logical commits and following software engineering best practices.
- Use **GitHub Actions** to run tests automatically on each commit, ensuring code quality and correctness.

## Version Control and Documentation

### Version Control

- Commit messages should be clear, concise, and logically group features, bug fixes, and tests.
- Maintain a consistent commit history throughout the development process to demonstrate your progress.

### Documentation

The README file provides an overview of the project and includes the following sections:

- **Setup Instructions**: How to install and configure the project.
- **Usage Examples**: Instructions on using the REPL interface and available commands.
- **Design Patterns Explanation**: A description of the design patterns implemented and their purpose.
- **Logging Configuration**: Explanation of how logging is set up and configured using environment variables.

## Evaluation Criteria

### Functionality (40 Points)

- **Calculator Operations** (20 points): Correct implementation of basic arithmetic operations (addition, subtraction, multiplication, and division).
- **History Management** (10 points): Effective use of Pandas to manage calculation history.
- **Configuration via Environment Variables** (5 points): Flexible application configuration using environment variables.
- **REPL Interface** (5 points): User-friendly command-line interface for calculator interaction.

### Design Patterns (20 Points)

- **Implementation and Application** (10 points): Effective use of design patterns, including the Facade, Command, Factory Method, Singleton, and Strategy patterns.
- **Documentation and Explanation** (10 points): Thorough documentation of design patterns and their implementation in the project.

### Testing and Code Quality (20 Points)

- **Comprehensive Testing with Pytest** (10 points): Minimum of 90% test coverage with detailed test cases.
- **Code Quality and Adherence to Standards** (10 points): Code that adheres to PEP 8 standards and is verified using Pylint.

### Version Control, Documentation, and Logging (20 Points)

- **Commit History** (10 points): Clear, logical, and informative commit messages.
- **README Documentation** (5 points): Comprehensive documentation with setup, usage, and architectural decisions.
- **Logging Practices** (5 points): Proper use of logging with different log levels and configuration through environment variables.

## Setup Instructions

To set up and run the Advanced Python Calculator, follow these steps:

1. **Clone the Repository**: 
git clone https://github.com/your-username/advanced-python-calculator.git

2. **Install Dependencies**: 
Navigate to the project directory and install required dependencies:
cd advanced-python-calculator  
pip install -r requirements.txt

3. **Configure Environment Variables**:
Set up any necessary environment variables for logging and configuration. Example:
export LOG_LEVEL=INFO


4. **Run Tests**: 
Ensure all tests pass with Pytest:
pytest --cov=calculator


5. **Start the REPL**: 
Run the calculator in the terminal:  
python main.py


6. **Interact with the Calculator**:
Use the REPL to perform calculations, manage history, and access available plugin commands.

## Conclusion

The Advanced Python Calculator combines essential features for a robust command-line application, including arithmetic operations, dynamic plugin integration, and history management using Pandas. By applying design patterns, logging best practices, and maintaining code quality, this project demonstrates real-world software engineering principles.

## Video Demo
[Link] (https://drive.google.com/file/d/1ChSq5ovF4TdZWZJTNQQ-mZdXsnFBJsUY/view?usp=drive_link)
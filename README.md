# Software Design Patterns
This repository contains a collection of common software design patterns implemented in Python. The patterns are categorized into three main categories: **creational**, **structural**, and **behavioral**. Each pattern comes with an example code snippet to illustrate its usage.

Feel free to explore the patterns, use the code in your projects, and adapt them to your specific requirements. The goal is to provide a reference and learning resource for developers interested in understanding and applying design patterns in Python.

## Getting Started
To use the code examples, simply navigate to the desired design pattern folder and review the corresponding Python file. Each file contains a detailed explanation of the pattern's purpose, implementation details, and an example usage scenario. You can copy the code into your project or modify it as needed.

## Contributing
Contributions to this repository are welcome! If you have implemented additional design patterns in Python or have suggestions for improvements/test cases, please feel free to open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE). Feel free to use the code in this repository in any way you find helpful for your projects.

## Unit Testing
I use [pytest](https://docs.pytest.org) to conduct unit testing to ensure the patterns behave as expected. To run the unit tests, run the following command from the **root** directory:

```python -m pytest test\ -v``` or ```python -m pytest test\<test file>.py -v```

## All Patterns
### Creational Patterns
#### Singleton
The Singleton pattern is a creational pattern that ensures only one instance of a class is created and provides a global point of access to it. The pattern is useful when you need to ensure only one instance of a class is created and shared across the application. The pattern is commonly used in logging, caching, and database connection classes. The Singleton Metaclass pattern is a variation of the Singleton pattern that uses a metaclass to create the singleton instance. 
- [Singleton](design_patterns/creational/singleton.py)
- [Singleton Metaclass](design_patterns/creational/singleton_meta.py)

### Structural Patterns
#### Adapter
The Adapter pattern is a structural pattern that allows incompatible classes to work together by converting the interface of one class into another expected by the client. The pattern is useful when you need to integrate a third-party class into your application but cannot modify the class directly. The pattern is commonly used to integrate legacy code into new applications. The Adapter pattern can be implemented using either a class or an object. The class implementation uses multiple inheritance to adapt the interface of the adaptee to the target interface, therefore the programming language must support multiple inheritance. The object implementation uses composition to adapt the interface of the adaptee to the target interface.
- [Adapter (Class)](design_patterns/structural/adapter_class.py)
- [Adapter (Object)](design_patterns/structural/adapter_object.py)

### Behavioral Patterns
#### Observer
The Observer pattern is a behavioral pattern that defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically. The pattern is useful when you need to notify multiple objects about changes in another object. The pattern is commonly used in GUIs, event-driven systems, and distributed systems. 
- [Observer](design_patterns/behavioral/observer.py)

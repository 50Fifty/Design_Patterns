# Software Design Patterns
This repository contains a collection of common software design patterns implemented in Python. The patterns are categorized into three main categories: creational, structural, and behavioral. Each pattern comes with an example code snippet to illustrate its usage.

Feel free to explore the patterns, use the code in your projects, and adapt them to your specific requirements. The goal is to provide a reference and learning resource for developers interested in understanding and applying design patterns in Python.

## Creational Patterns
### Singleton
- [Singleton](design_patterns/creational/singleton.py)
- [Singleton Metaclass](design_patterns/creational/singleton_meta.py)

## Structural Patterns
### Adapter 
- [Class](design_patterns/structural/adapter_class.py)
- [Object](design_patterns/structural/adapter_object.py)

## Behavioral Patterns

## Getting Started
To use the code examples, simply navigate to the desired design pattern folder and review the corresponding Python file. Each file contains a detailed explanation of the pattern's purpose, implementation details, and an example usage scenario. You can copy the code into your project or modify it as needed.

## Contributing
Contributions to this repository are welcome! If you have implemented additional design patterns in Python or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE). Feel free to use the code in this repository in any way you find helpful for your projects.

## Unit Testing
I use [pytest](https://docs.pytest.org) to conduct unit testing to ensure the patterns behave as expected. To run the unit tests, run the following command from the <b>root</b> directory:

```python -m pytest test\ -v``` or ```python -m pytest test\<test file>.py -v```

To hide ```DeprecationWarning```s, add:
```-W error::DeprecationWarning```

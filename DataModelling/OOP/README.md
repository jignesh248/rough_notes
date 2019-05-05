https://www.oodesign.com/

https://medium.com/omarelgabrys-blog/requirements-engineering-introduction-part-1-6d49001526d3 //TODO

### OOPS 
- https://medium.com/omarelgabrys-blog/object-oriented-analysis-and-design-introduction-part-1-a93b0ca69d36
- https://medium.com/omarelgabrys-blog/object-oriented-analysis-and-design-conceptual-model-part-2-ce730ac4eb31
- https://medium.com/omarelgabrys-blog/object-oriented-analysis-and-design-structural-models-part-3-4054e11157ff
- https://medium.com/omarelgabrys-blog/object-oriented-analysis-and-design-interaction-models-part-4-b11f03ef3ccf //TODO
- https://medium.com/omarelgabrys-blog/object-oriented-analysis-and-design-behavioral-models-part-5-42ab2d291fba //TODO
- https://medium.com/omarelgabrys-blog/object-oriented-analysis-and-design-design-principles-part-6-b78e2b9da023
- https://medium.com/omarelgabrys-blog/object-oriented-analysis-and-design-design-patterns-part-7-bc9c003a0f29

- https://www.codeproject.com/Articles/1137299/Object-Oriented-Analysis-and-Design //TODO
- https://www.codeproject.com/Articles/1166136/S-O-L-I-D-GRASP-And-Other-Basic-Principles-of-Obje //TODO
- https://www.codeproject.com/Articles/1231715/Object-Oriented-Programming-Concepts-With-a-System //TODO

MVC //TODO
http://www.tedfelix.com/software/oo.html //TODO
http://www.cs.nuim.ie/~dkelly/CS100-2/Elevator%20Problem.htm //TODO
indirection object //TODO

- https://www.lynda.com/Python-tutorials/Programming-Foundations-Object-Oriented-Design/731735-2.html //TODO
- https://www.udemy.com/advanced-object-oriented-analysis-of-hard-problems/ //TODO
- https://www.udemy.com/refactoring-to-patterns/ //TODO
- https://www.udemy.com/patterns-cplusplus/ //TODO

### Solid Principles
- Summary : https://hackernoon.com/solid-principles-made-easy-67b1246bcdf //TODO
- Detailed : https://www.udemy.com/solid-principles-object-oriented-design-architecture/ //TODO

https://medium.com/educative/the-7-most-important-software-design-patterns-d60e546afb0e //TODO

- https://github.com/leocavalcante/siler/wiki/Classes,-OOP,-MVC-and-where-is-the-Controller //TODO


- Elevator system //TODO
- Design a petrol pump management system //TODO
- Design Tank Game //TODO

___________________________________________________________________________________________________


What is OOPS?
Object-oriented programming (OOP) is a programming language model organized around objects rather than "actions" and data rather than logic. Historically, a program has been viewed as a logical procedure that takes input data, processes it, and produces output data.

basic Concepts of OOPs?
Abstraction.
Encapsulation. 
Inheritance. 
Polymorphism.

A class is used to specify the form of an object and it combines data representation and methods for manipulating that data into one neat package. The data and functions within a class are called members of the class.

What is an object?
Objects are created from Classes, in C#, is an instance of a class that is created dynamically. Object is also a keyword that is an alias for the predefined type System.

What is Encapsulation?
Encapsulation is the packing of data and functions into a single component.
Encapsulation is the technique of making the fields in a class private and providing access to the fields via public methods. If a field is declared private, it cannot be accessed by anyone outside the class, thereby hiding the fields within the class. For this reason, encapsulation is also referred to as data hiding.
Encapsulation can be described as a protective barrier that prevents the code and data being randomly accessed by other code defined outside the class. Access to the data and code is tightly controlled by an interface.
The main benefit of encapsulation is the ability to modify our implemented code without breaking the code of others who use our code. With this feature Encapsulation gives maintainability, flexibility and extensibility to our code.

- A good read for [Abstraction vs  Encapsulation vs Information Hiding](https://docs.google.com/document/d/1V4NLeCjOwaSRnnBjzqPClhmC9x5caLHdSskModDSeu4/edit?usp=sharing)

Polymorphism is an object-oriented programming concept that refers to the ability of a variable, function or object to take on multiple forms. A language that features polymorphism allows developers to program in the general rather than program in the specific.

. An abstract class is a class that is declared using the abstract keyword. An abstract class cannot be instantiated. It can be used only as a super-class for those classes that extend the abstract class.

Moreover, an abstract class may contain methods without any implementation, called abstract methods. The declaration of an abstract method starts with the abstract keyword and ends with a semicolon, instead of the method’s body. If a class contains an abstract method, either declared or inherited, it must be declared as an abstract class.
A class that extends an abstract class must implement all its abstract methods (if any). Otherwise, the sub-class must be declared as abstract as well. Finally, any implementation of an abstract method can be overridden by additional sub-classes.

An interface is a collection of abstract methods. A class implements an interface, thereby inheriting the abstract methods of the interface.
A class describes the attributes and behaviors of an object. An interface contains behaviors that a class implements.
Unless the class that implements the interface is abstract, all the methods of the interface need to be defined in the class.
An interface is similar to a class in the following ways:
An interface can contain any number of methods.
 an interface is different from a class in several ways, including:
You cannot instantiate an interface.
An interface does not contain any constructors.
All of the methods in an interface are abstract.
An interface cannot contain instance fields. The only fields that can appear in an interface must be declared both static and final.
An interface is not extended by a class; it is implemented by a class.
An interface can extend multiple interfaces.
Interfaces have the following properties:
An interface is implicitly abstract. You do not need to use the abstract keyword when declaring an interface.
Each method in an interface is also implicitly abstract, so the abstract keyword is not needed.
Methods in an interface are implicitly public.
When implementation interfaces there are several rules:
A class can implement more than one interface at a time.
A class can extend only one class, but implement many interfaces.
An interface can extend another interface, similarly to the way that a class can extend another class.

Use abstract class and inheritance if you can make the statement "A is a B". Use interfaces if you can make the statement "A is capable of [doing] as", or also, abstract for what a class is, interface for what a class can do.

http://www.javatpoint.com/difference-between-abstract-class-and-interface



7. What is Inheritance?
inheritance is when an object or class is based on another object or class, using the same implementation (inheriting from a class) specifying implementation to maintain the same behavior (realizing an interface; inheriting behavior).

It is a mechanism for code reuse and to allow independent extensions of the original software via public classes and interfaces.
8. What is Constructor?
A is special method of the class that will be automatically invoked when an instance of the class is created is called as constructor.

Constructors are mainly used to initialize private fields of the class while creating an instance for the class.

9. Types of Constructors
Basically constructors are 5 types those are
Default Constructor
Parameterized Constructor
Copy Constructor
Static Constructor
Private Constructor

10. Define Destructor?
A destructor is a method which is automatically invoked when the object is destroyed.

Its main purpose is to free the resources (memory allocations, open files or sockets, database connections, resource locks, etc.)

11. What is Inline function?
In the C and C++ programming languages, an inline function is one qualified with the keyword inline; this serves two purposes.
Firstly, it serves as a compiler directive, which suggests (but does not require) that the compiler substitute the body of the function inline by performing inline expansion,
The second purpose of inline is to change linkage behavior; the details of this are complicated


12. What is operator overloading?
In programming, operator overloading—less commonly known as operator ad hoc polymorphism—is a specific case of polymorphism, where different operators have different implementations depending on their arguments. Operator overloading is generally defined by the language, the programmer, or both.

13. Different between method overriding and  method overloading?
In Overriding methods it will create two or more methods with same name and same parameter in different classes.

while Overloading it will create more then one method with same name but different parameter in same class






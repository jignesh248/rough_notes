### Requirement Elicitation

- What is the system like? : One way you can find out more about a system is to figure out what the system is like. In other words, are there some things that you do know about that the system functions or behaves like?

This is called commonality... what things are similar?

- What is the system not like?  Another great way to find out what a system should do is to figure out what it’s not like. This helps you determine what you don’t need to worry about in your system.

This is called variability... what things are different?

- Domain analysis : The process of identifying, collecting, organizing, and representing the relevant information of a domain, based upon the study of existing systems and their development histories, knowledge captured from domain experts, underlying theory, and emerging technology within a domain.

### Solving Big Problems

- Listen to the customer, and figure out what they want you to build

- Put together a feature list, in language the customer understands.

- Make sure your features are what the customer acutally wants.

- Create blueprints of the system using use case diagrams (and use cases).

- Break the big system up into lots of smaller sections.

- Apply design patterns to the smaller sections of the system.

- Use basic OOA & D principles to design and code each smaller section.

### Bullet Points 

- The best way to look at a big problem is to view it as a collection of smaller problems.

- Just like in small projects, start working on big projects by gathering features and requirements.

- Features are usually “big” things that a system does, but also can be used interchangeably with the term “requirements.”

- Commonality and variability give you points of comparison between a new system and things you already know about.

- Use cases are detail-oriented; use case diagrams are focused more on the big picture.

- Your use case diagram should account for all the features in your system.

- Domain analysis is representing a system in language that the customer will understand.

### Requirements Change & Analysis

- When your system needs to work in a new or different way, begin by updating your use case.

- textual analysis : Looking at the nouns (and verbs) in your use case to figure out classes and methods is called textual analysis.

-- The nouns of a use case are candidates for classes in your system

-- The verbs in your use case are (usually) the methods of the objects in your system. The verbs are candidates for operations

- A good use case precisely lays out what a system does, but does not indicate how the system accomplishes that task.

- Each use case should focus on only one customer goal. If you have multiple goals, you will need to write multiple use cases.

- Class diagrams leave lots of detail out, such as class constructors, some type information, and the purpose of operations on your classes.

-----------

BULLET POINTS
Analysis helps you ensure that your software works in the real world context, and not just in a perfect environment.

Use cases are meant to be understood by you, your managers, your customers, and other programmers.

You should write your use cases in whatever format makes them most usable to you and the other people who are looking at them.

A good use case precisely lays out what a system does, but does not indicate how the system accomplishes that task.

Each use case should focus on only one customer goal. If you have multiple goals, you will need to write multiple use cases.

Class diagrams give you an easy way to show your system and its code constructs at a 10,000-foot view.

The attributes in a class diagram usually map to the member variables of your classes.

The operations in a class diagram usually represent the methods of your classes.

Class diagrams leave lots of detail out, such as class constructors, some type information, and the purpose of operations on your classes.

Textual analysis helps you translate a use case into code-level classes, attributes, and operations.

The nouns of a use case are candidates for classes in your system, and the verbs are candidates for methods on your system’s classes.



----------


### UML

- When the name of the class is in italic, the class is abstract.

- The line with a diamond means aggregation. Aggregation is a special form of association and means that one thing is made up(in part) of another thing.

- A line with an arrow that isn't colored-in means generalization. You use a generalization to show that a class extents and inherits behaviour from a more generalizaed class.
------

### OOP Analysis

- By coding to an interface, your code will work with all of the interface’s subclasses—even ones that haven’t been created yet.
eg. use interface as type for function arguments or it's return types.

- Encapsulation also helps you protect your classes from unnecessary changes. Anytime you have behavior in an application that you think is likely to change, you want to move that behavior away from parts of your application that probably won’t change very frequently. In other words, you should always try to encapsulate what varies.

### Good Design Change
- You already know that the one constant in software is CHANGE. Software that isn’t well-designed falls apart at the first sign of change, but great software can change easily. 

The easiest way to make your software resilient to change is to make sure each class has only one reason to change. In other words, you’re minimizing the chances that a class is going to have to change by reducing the number of things in that class that can cause it to change.

When you see a class that has more than one reason to change, it is probably trying to do too many things. See if you can break up the functionality into multiple classes, where each individual class does only one thing—and therefore has only one reason to change.

- Cohesion measures the degree of connectivity among the elements of a single module, class, or object. The higher the cohesion of your software is, the more well-defined and related the responsibilities of each individual class in your application. Each class has a very specific set of closely related actions it performs.

![](https://learning.oreilly.com/library/view/head-first-object-oriented/0596008678/httpatomoreillycomsourceoreillyimages2069334.png.jpg)

![](https://learning.oreilly.com/library/view/head-first-object-oriented/0596008678/httpatomoreillycomsourceoreillyimages2069336.png.jpg)

### Analysis and Design

- Well-designed software is easy to change and extend.
- Use basic OO priciples like encapsulation and inheritance to make your software more flexible.
- If a design isn't flexible, then CHANGE IT! Never settle on bad design, even if it's your bad desing, that has to change.
- Make sure each of your classes is cohsive each of your classes should focus on doing ONE THING really well.
- Always strive for higher cohesion as you move through your software's desing life cycle.


----

The things in your application that are really important are architecturally significant, and you should focus on them FIRST.
----


### OO Principles

- Encapsulate what varies.
- Code to an interface rather than to an implementation.
- Each class in your application should have only one reason to change.
- Classes are about behaviour and functionality.
- Open-Closed Principle : Classes should be open for extension, and closed for modification.
There are lots of different ways to accomplish this, and while inheritance is often the easiest to implement, it’s certainly not the only option
- Don’t Repeat Yourself : Avoid duplicate code by abstracting out things that are common and placing them in a single location. DRY is about having each piece of information and behavior in your system in a single, sensible place.
- Single Responsibility Principle : Every object in your system should have a single responsibility, and all the object’s services should be focused on carrying out that single responsibility.

You’ve implemented the Single Responsibility Principle correctly when each of your objects has only one reason to change.

Spotting multiple responsibilities : Most of the time, you can spot classes that aren’t using the SRP with a simple test:

1. On a sheet of paper, write down a bunch of lines like this: The ______________   ______________ itself. You should have a line like this for every method in the class you’re testing for the SRP.

2. In the first blank of each line, write down the class name; in the second blank, write down one of the methods in the class. Do this for each method in the class.

3. Read each line out loud (you may have to add a letter or word to get it to read normally). Does what you just said make any sense? Does your class really have the responsibility that the method indicates it does?

If what you’ve just said doesn’t make sense, then you’re probably violating the SRP with that method. The method might belong on a different class... think about moving it.

Q: How does SRP analysis work when a method takes parameters, like wash(Automobile) on the CarWash class?
A: Good question! For your SRP analysis to make any sense, you need to include the parameter of the method in the method blank. So you would write “The CarWash washes [an] automobile itself.” That method makes sense (with the Automobile parameter), so it would stay on the CarWash class.

- If a parameter that might cause a method to make sense, your SRP analysis might be misleading. That’s why you always need to apply a good amount of your own common sense and knowledge of the system in addition to what you learn from the SRP analysis.

- When we used a Map to store properties for all types of units in the Unit class, we were using the SRP. So instead of having game-specific Units have to deal with their properties, and still have the base Unit class dealing with a different set of properties, we moved all property-related functionality into the nit class. So handling the properties feature is taken care of in ONE single place—the Unit class.

- The Liskov Substitution Principle (LSP) : Subtypes must be substitutable for their base types

- Delegation : If you need to use functionality in another class, but you don’t want to change that functionality, consider using delegation instead of inheritance.
Delegate behavior to another class when you don’t want to change the behavior, but it’s not your object’s responsibility to implement that behavior on its own.

- Composition : You can reuse behavior from one or more classes, and in particular from a family of classes, with composition. Your object completely owns the composed objects, and they do not exist outside of their usage in your object.

Use composition to assemble behaviors from other classes

- When to use composition : When we reference a whole family of behaviors like in the Unit class, we’re using composition. The Unit’s weapons property is composed of a particular Weapon implementation’s behavior. 
Composition is most powerful when you want to use behavior defined in an interface, and then choose from a variety of implementations of that interface, at both compile time and run time.
Composition allows you to use behavior from a family of other classes, and to change that behavior at runtime.
When an object is composed of other objects, and the owning object is destroyed, the objects that are part of the composition go away, too.
In composition, the object composed of other behaviors owns those behaviors. When the object is destroyed, so are all of its behaviors.

- Aggregation : When you want the benefits of composition, but you’re using behavior from an object that does exist outside of your object, use aggregation.
If the object does make sense existing on its own, then you should use aggregation; if not, then go with composition.

It’s easy to get confused about when you should use composition, and when you should use aggregation. The easiest way to figure this out is to ask yourself, Does the object whose behavior I want to use exist outside of the object that uses its behavior?

- If you favor delegation, composition, and aggregation over inheritance, your software will usually be more flexible, and easier to maintain, extend, and reuse.

- aggregation or delegation are two great ways to fix an inheritance tree that doesn’t conform to the LSP

----------------------------

![](https://learning.oreilly.com/library/view/head-first-object-oriented/0596008678/httpatomoreillycomsourceoreillyimages2069238.png.jpg)

----------------------------

### BULLET POINTS
The Open-Closed Principle keeps your software reusable, but still flexible, by keeping classes open for extension, but closed for modification.

With classes doing one single thing through the Single Responsibility Principle, it’s even easier to apply the OCP to your code.

When you’re trying to determine if a method is the responsibility of a class, ask yourself, Is it this class’s job to do this particular thing? If not, move the method to another class.

Once you have your OO code nearly complete, be sure that you Don’t Repeat Yourself. You’ll avoid duplicate code, and ensure that each behavior in your code is in a single place.

DRY applies to requirements as well as your code: you should have each feature and requirement in your software implemented in a single place.

The Liskov Substitution Principle ensures that you use inheritance correctly, by requiring that subtypes be substitutable for their base types.

When you find code that violates the LSP, consider using delegation, composition, or aggregation to use behavior from other classes without resorting to inheritance.

If you need behavior from another class but don’t need to change or modify that behavior, you can simply delegate to that class to use the desired behavior.

Composition lets you choose a behavior from a family of behaviors, often via several implementations of an interface.

When you use composition, the composing object owns the behaviors it uses, and they stop existing as soon as the composing object does.

Aggregation allows you to use behaviors from another class without limiting the lifetime to those behaviors.

Aggregated behaviors continue to exist even after the aggregating object is destroyed.

TOOLS FOR YOUR OOA&D TOOLBOX
We’ve got a lot more OO principles to add to the toolbox. Let’s add what we’ve learned to our notes—and remember: these principles are best used together, not separately!


----------------------------

Architecutre bringing order to Chaos
____________________

- Architecture : Architecture is the organizational structure of a system, including its decomposition into parts, their connectivity, interaction mechanisms, and the guiding principles and decisions that you use in the design of a system.

- The things in your application that are really important are architecturally significant, and you should focus on them FIRST.

---------------------

The three Qs of architecture
When you’re trying to figure out if something is architecturally significant, there are three questions you can ask:

1. Is it part of the essence of the system?Is the feature really core to what a system actually is? Think about it this way: can you imagine the system without that feature? If not, then you’ve probably found a feature that is part of the essence of a system.

2. What the fuck does it mean?
If you’re not sure what the description of a particular feature really means, it’s probably pretty important that you pay attention to that feature. Anytime you’re unsure about what something is, it could take lots of time, or create problems with the rest of the system. Spend time on these features early, rather than late.

3. How the “heck” do I do it?
Another place to focus your attention early on is on features that seem really hard to implement, or are totally new programming tasks for you. If you have no idea how you’re going to tackle a particular problem, you better spend some time up front looking at that feature, so it doesn’t create lots of problems down the road.

---------------------

- I probably won’t know how to do anything on my feature list. So won’t the 3rd Q of architecture about not knowing how to do something always apply?

- Q: If the Tile class handles adding and removing units, and you can get the tile at a coordinate from the Board using getTile(), why add those addUnit() and removeUnit() methods to Board. Couldn’t you just call getTile(), and then use the Tile to do those things?
We decided to add the Unit-related methods to Board, and have Board be the entry point for game designers

_____________________

- Good design will always reduce risk.

### ---------------------

- Architecture helps you turn all your diagrams, plans, and feature lists into a well-ordered application.

- The features in your system that are most important to the project are architecturally significant.

- Focus on features that are the essence of your system, that you’re unsure about the meaning of, or unclear about how to implement first.

- Everything you do in the architectural stages of a project should reduce the risks of your project failing.

- If you don’t need all the detail of a use case, writing a scenario detailing how your software could be used can help you gather requirements quickly.

- When you’re not sure what a feature is, you should ask the customer, and then try and generalize the answers you get into a good understanding of the feature.

- Use commonality analysis to build software solutions that are flexible.

- Customers are a lot more interested in software that does what they want, and comes in on time, than they are in code that you think is really cool.

###----------------------

- You write great software iteratively.Work on the big picture, and then iterate over pieces of the app until it’s complete.

- Two choices to make when diving deeper on Big Projects

1. Feature driven development : is when you pick a specific feature in your app, and plan, analyze, and develop that feature to completion.
2. Use case driven development : is when you pick a scenario through a use case, and write code to support that complete scenario through the use case.
You’ll often see the terms “flow” and “scenario” used interchangeably.

| Feature driven development is more granular | Use case driven development is more “big picture” |
|------|-------|
|Works well when you have a lot of different features that don’t interconnect a whole lot. | Works well when your app has lots of processes and scenarios rather than individual pieces of functionality. |
| Allows you to show the customer working code faster. | Allows you to show the customer bigger pieces of functionality at each stage of development. |
| Is very functionality-driven. You’re not going to forget about any features using feature driven development. | Is very user-centric. You’ll code for all the different ways a user can use your system with use case driven development. |
| Works particularly well on transactional systems, where the system is largely defined by lengthy, complicated processes. | Works particularly well on systems with lots of disconnected pieces of functionality. |

- storage of attributes of a class is decided based on 

1. Emphasizing Commonality 

- The emphasis is on keeping the common properties of a class outside of a properties Map each as an class attribute, and leaving properties that vary inside the properties Map.

cons : 
 -- two different ways to access properties : different getters and setters(property-specific) for common properties of all instances and properties that are stored in Map. 
 
 -- 2 different ways to access properties leads to code duplication. When removing or changing properties, requires code change in class.


2. Emphasizing Encapsulation : The emphasis is on encapsulation, and a flexible design. Even if the names of common properties change, the Unit class can stay the same, since no property names are hardcoded into the class itself

cons : 

-- No way to differntiate standard properties and properties that varies.

-- Lots of work at runtime as you’re going to have to cast that into the right value type for each different property, all at runtime, even for the properties that are common to all instances of class.

Q: What happens when I can’t decide between a couple of good design choices?
A: You always have to make a choice, even if you’re not 100% sure if it’s the right one. It’s always better to take your best guess, and see how things work out, rather than spend endless hours debating one choice or another. That’s called analysis paralysis, and it’s a sure way to not get anything done. It’s much better to start down one path, even if you’re not totally sure it’s the right one, and get some work done, than to not make a choice at all.

- Good software is built iteratively. Analyze, design, and then iterate again, working on smaller and smaller parts of your app.

Each time you iterate, reevaluate your design decisions, and don’t be afraid to CHANGE something if it makes sense for your design.

- When you program by contract, you and your software’s users are agreeing that your software will behave in a certain way. When you programm defensively you check for all invalid, abusive ways client can use the code and protect against them crashing your code and their code.

_____
BULLET POINTS

The first step in writing good software is to make sure your application works like the customer expects and wants it to.

Customers don’t usually care about diagrams and lists; they want to see your software actually do something.

Use case driven development focuses on one scenario in a use case in your application at a time.

In use case driven development, you focus on a single scenario at a time, but you also usually code all the scenarios in a single use case before moving on to any other scenarios, in other use cases.

Feature driven development allows you to code a complete feature before moving on to anything else.

You can choose to work on either big or small features in feature-driven development, as long as you take each feature one at a time.

Software development is always iterative. You look at the big picture, and then iterate down to smaller pieces of functionality.

You have to do analysis and design at each step of your development cycle, including when you start working on a new feature or use case.

Tests allow you to make sure your software doesn’t have any bugs, and let you prove to your customer that your software works.

A good test case only tests one specific piece of functionality.

Test cases may involve only one, or several, methods in a single class, or may involve multiple classes.

Test driven development is based on the idea that you write your tests first, and then develop software that passes those tests. The result is fully functional, working software.

Programming by contract assumes both sides in a transaction understand what actions generate what behavior, and will abide by that contract.

Methods usually return null or unchecked exceptions when errors occur in programming by contract environments.

Defensive programming looks for things to go wrong, and tests extensively to avoid problem situations.

Methods usually return “empty” objects or throw checked exceptions in defensive programming environments.


------

### Programming Practices

- Programming by contracts sets up an agreement about how your software behaves that you and users of your software agree to abide by.

- Defensive programming doesn't trust other software and does extensive error and data checking to ensure the other software doesn't give you bad or unsafe information. 

### Development Approaches

- Use Case driven development takes a single use case in your system, and focuses on completing the code to implement the entire use case, including all of its scenarios before moving on to anything else in the aplication.

- Feature driven development focuses on a single feature, and codes all the behaviour of that feature, before moving on to anything else in the application

- Test driven development writes test scenarious for a piece of functionality before writing the code for that functionality. Then you write software to pass all the tests.

- Good software development usually incorporates all of these development models at different stages of the development cycle.




- Use cases reflect usage, features reflect functionality
- The features in your system reflect your system’s functionality. Your system must do those things in order for the use cases to actually work, even though the functionality isn’t always an explicit part of any particular use case.
- The features in your system are what the system does, and are not always reflected in your use cases, which show how the system is used.

Q. Desing a Subway

- https://learning.oreilly.com/library/view/head-first-object-oriented/0596008678/httpatomoreillycomsourceoreillyimages2070084.png.jpg

- When you override equals() in Java, you should usually also override hashCode() to ensure correct comparisons.

- The Java specification recommends that if two objects are equal, they should have the same hash code. So if you’re deciding on equality based on a property, it’s a good idea to also override hashCode() and return a hash code based on that same property. This is particularly important if you’re using your object in a Hashtable or HashMap, which both make heavy use of the hashCode() method.

- You should only expose clients of your code to the classes that they NEED to interact with.
Classes that the clients don’t interact with can be changed with minimal client code being affected.

- It’s your job to balance making sure the customer gets the functionality they want with making sure your code stays flexible and well-designed.


- Problems with some OOD conventions

#1. IS-A and HAS-A
IS-A REFERS TO INHERITANCE
HAS-A REFERS TO COMPOSITION OR AGGREGATION

The problem with IS-A and HAS-A 
- they tend to break down in certain situations. eg. when modeling shapes, like Circle, Rectangle, and Diamond.

Square object has a IS-A relationship: Square IS-A Rectangle. So you should make Square extend Rectangle, right? No! 
remember LSP, and that subtypes should be substitutable for their base types. So Square should be a direct substitute for Rectangle.
The problem is that when you set the width in setWidth() on Square, the square is going to have to set its height, too, since squares have equal width and height. So even though Square IS-A Rectangle, it doesn’t behave like a rectangle. Squares behave differently than rectangles, and aren’t substitutable for them—that’s a violation of the LSP.

Use inheritance when one object behaves like another, rather than just when the IS-A relationship applies.

- CRC cards
CRC stands for Class, Responsibility, Collaborator. These cards are used to take a class and figure out what its responsibility should be, and what other classes it collaborates with.

CRC cards are typically just 3x5 index cards, with each individual card representing a class. The card has two columns: one for the responsibilities of the class, and another for other classes that are collaborators, and used to fulfill those responsibilities.

CRC cards help implement the SRP
You can use CRC cards to make sure your classes follow the Single Responsibility Principle.

![SRP-CRC](https://learning.oreilly.com/library/view/head-first-object-oriented/0596008678/httpatomoreillycomsourceoreillyimages2070280.png.jpg)

- encapsulation. The process of enclosing programming elements inside larger, more abstract entities. Also known as information hiding, or separation of concerns.
Encapsulation separates your data from your app’s behavior.Then you can control how each part is used by the rest of your application.

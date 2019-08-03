### The Object_Oriented Analysis and Design Project Lifecycle

#### 1. Make sure you software does what the customer wants it to do. 

##### a. Feature List 
- Figure out what your app is supposed to do at a high level.
- Your feature lists are all about understanding what your software is supposed to do.

##### b. Use case Diagrams 
- Nail dow the big processes that your app performs, and any external forces that are involved.
- Your use case diagrams let you start thinking about how your software will be used, without getting into a bunch of unnecessary details.

##### c. Break Up the Problem 
- Break your application up into modules of functionality, and then decide on an order in which to tackle each of your modules.

##### d. [Iterative] Requirements
 - Figure out the individual requirements for each module, and make sure those fit in with the big picture.

##### e. [Iterative] Domain Analysis 
- Figure out how your use cases map to objects in your app, and make sure your customer is on the same page as you are.

#### 2. Apply basic OO principles to add flexibility.

##### f. [Iterative] Preliminary Design
- Fill in details about your objects, define relationships between the objects, and apply pricinple and patterns.

#### 3. Strive for a maintainable reusable design.

##### g. [Iterative] Implementation
 - Write code, test it, and make sure it works. Do this for each behavior, each feature, each use case, each problem, until you're done.

##### h. Delivery 
- You're done! Release your software, submit your invoices and get paid.

_________

### 2. Apply basic OO principles to add flexibility : OO Principles

##### Encapsulate what varies.

##### Code to an interface rather than to an implementation.

##### Each class in your application should have only one reason to change.

##### Classes are about behaviour and functionality.

##### Open-Closed Principle 
Classes should be open for extension, and closed for modification.
There are lots of different ways to accomplish this, and while inheritance is often the easiest to implement, it’s certainly not the only option

##### Don’t Repeat Yourself 
Avoid duplicate code by abstracting out things that are common and placing them in a single location. DRY is about having each piece of information and behavior in your system in a single, sensible place.

##### Single Responsibility Principle 
- Every object in your system should have a single responsibility, and all the object’s services should be focused on carrying out that single responsibility.

- You’ve implemented the Single Responsibility Principle correctly when each of your objects has only one reason to change.

```
 Spotting multiple responsibilities : Most of the time, you can spot classes that aren’t using the SRP with a simple test:

1. On a sheet of paper, write down a bunch of lines like this: 

The ______________   ______________ itself. 

You should have a line like this for every method in the class you’re testing for the SRP.

2. In the first blank of each line, write down the class name; in the second blank, write down one of the methods in the class. Do this for each method in the class.

3. Read each line out loud (you may have to add a letter or word to get it to read normally). Does what you just said make any sense? Does your class really have the responsibility that the method indicates it does?

If what you’ve just said doesn’t make sense, then you’re probably violating the SRP with that method. The method might belong on a different class... think about moving it.
```
```
Q: How does SRP analysis work when a method takes parameters, like wash(Automobile) on the CarWash class?
A: Good question! For your SRP analysis to make any sense, you need to include the parameter of the method in the method blank. So you would write “The CarWash washes [an] automobile itself.” That method makes sense (with the Automobile parameter), so it would stay on the CarWash class.

- If a parameter that might cause a method to make sense, your SRP analysis might be misleading. That’s why you always need to apply a good amount of your own common sense and knowledge of the system in addition to what you learn from the SRP analysis.

- When we used a Map to store properties for all types of units in the Unit class, we were using the SRP. So instead of having game-specific Units have to deal with their properties, and still have the base Unit class dealing with a different set of properties, we moved all property-related functionality into the nit class. So handling the properties feature is taken care of in ONE single place—the Unit class.
```

##### The Liskov Substitution Principle (LSP)
Subtypes must be substitutable for their base types


###### Aggregation or Delegation are two great ways to fix an inheritance tree that doesn’t conform to the LSP

___Delegation___

- Delegation is when you hand over the responsibility for a particular task to another class or method.

- When to use delegation?
If you need to use functionality in another class, but you don’t want to change that functionality, consider using delegation instead of inheritance.
Delegate behavior to another class when you don’t want to change the behavior, but it’s not your object’s responsibility to implement that behavior on its own.

___Composition___ 

- Composition allows you to use behavior from a family of other classes, and to change that behavior at runtime. Your object completely owns the composed objects, and they do not exist outside of their usage in your object.

- When to use composition? Use composition to assemble behaviors from other classes. When we reference a whole family of behaviors like in the Unit class, we’re using composition. The Unit’s weapons property is composed of a particular Weapon implementation’s behavior. 
Composition is most powerful when you want to use behavior defined in an interface, and then choose from a variety of implementations of that interface, at both compile time and run time.
Composition allows you to use behavior from a family of other classes, and to change that behavior at runtime.
When an object is composed of other objects, and the owning object is destroyed, the objects that are part of the composition go away, too.
In composition, the object composed of other behaviors owns those behaviors. When the object is destroyed, so are all of its behaviors.

___Aggregation___

- Aggregation is when one class is used as part of another class, but still exists outside of that other class.
 
- When to use aggregation? When you want the benefits of composition, but you’re using behavior from an object that does exist outside of your object, use aggregation.
If the object does make sense existing on its own, then you should use aggregation; if not, then go with composition.



___If you favor delegation, composition, and aggregation over inheritance, your software will usually be more flexible, and easier to maintain, extend, and reuse.___



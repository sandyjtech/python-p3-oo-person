# OO Person Lab

## Learning Goals

- Gain proficiency instantiating a class
- Gain ability when to configure attributes as `properties` with `getter` and `setter` methods
- Practice protecting 'private' properties by omitting setters after initialization

## Introduction

To practice object oriented programming (OOP), you're going to create a `Person` class. Each instance of the class will have the ability to:

- Get paid/receive payments
- Take a bath
- Call a friend
- Start a conversation
- State if they are happy and/or clean

## A Note on Notation

In the instructions below, you'll see the class constructor, instance methods, and properties referenced with different notation.
- `Class_Name(optional_values)` indicates invoking a classes constructor to create a new instance of the class
- `Class property attribute` indicates that an attribute should be configured as a property of the class, with getter and setter methods assigned as needed
- `Class method_name(self, *optional_args)` indicates an instance method of the class

## Instructions

Create a `Person` class with the behavior described below. You may need to configure some attributes as properties with custom setter and/or getter methods.

- `Person(name)`: takes a string argument of a name and saves it to the instantiated object. You should indicate that the name property should be treated as private after initialization and shoud not be changed. When a new person is instantiated, they should have the following attributes in addition to their name (saved as instance attributes on initialization):

    - `Person bank_account` with an initial value of 25
    - `Person happines` with an initial value of 8
    - `Person hygiene` with an initial value of 8

- `Person property name` gets and returns the person's name (no setter)
- `Person property bank_account` gets and/or sets the person's bank account
- `Person property happiness` gets and/or sets the value of the person's happines points
- `Person property hygiene` gets and/or sets the value of the person's hygiene points

### Instance methods

- `Person is_clean(self)` returns `True` if the person's hygiene is more than 7; otherwise, `False`
- `Person is_happy(self)` returns `True` if the person's happiness is more than 7; otherwise, `False`
- `Person get_paid(self, amount)` accepts a salary amount and adds this to the person's bank account. The method should also return `"all about the benjamins"`
- `Person take_bath(self)` increments the person's hygiene points by 4 and returns the string `"♪ Rub-a-dub just relaxing in the tub ♫"`
- `Person work_out(self)`: increments the person's happiness by two points, decreases
  their hygiene by three points, and returns the Queen lyrics,
  `"♪ another one bites the dust ♫"`
- `Person call_friend(self, friend)`: accepts another instance of the `Person` class,
  or "friend". The method should increment the person AND the friend's happiness
  points by three. It should also return a string. For example, if Stella calls
  her friend Felix, the method increment both Stella and Felix's happiness
  points and then returns `"Hi Felix! It's Stella. How are you?"`
- `Person start_conversation(self, friend, topic)`: accept two arguments, the friend
  to start a conversation with and the topic of conversation.

  - If the topic is politics, both people get sadder (their happiness decreases
    by 2) and the method returns `"blah blah partisan blah lobbyist"`.
  - If the topic is weather, both people get a little happier (their happiness
    increases by 1) and the method returns `"blah blah sun blah rain"`.
  - If the topic is not politics or weather, their happiness points don't change
    and the method returns `"blah blah blah blah blah"`.


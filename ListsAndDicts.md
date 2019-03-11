# Collections

Python has a few different ways that you can create collections. Collections make it easy to store large amounts of values into just one variable. The two most common types are **Lists** and **Dictionaries**.

## Lists

Lists are Python's equivalent of Arrays. They store multiple values of the same type, and those values can be accessed by their index in the list. Lists are very easy to instantiate:

```python
mylist = []
```

This will make an empty list with no elements. This doesn't really help us, so let's make a list with a few things in it:

```python
pets = ["Dog", "Cat", "Fish"]
```

Now we have a list of three strings. We can access elements by using `pets[i]`, which will give us the item at index i of the list. Since programming always starts counting at 0, `pets[0]` will give us the first element of the list, which is "Dog". So the following code should print "Dog".

```python
pets = ["Dog", "Cat", "Fish"]
pet_dog = pets[0]
print(pet_dog)
```

You can also change elements of the list using the same syntax. The following code should now print "Bird"

```python
pets = ["Dog", "Cat", "Fish"]
pets[1] = "Bird"
print(pets[1])
```


## Dictionaries

Sometimes you don't want to access elements of a collection by their index. Instead, you might want to associate keys with every value in your collection. This key-value pair is the idea behind dictionaries.

A dicionary is very similar in syntax to lists, but uses {} instead of []. So making a new Dictionary looks like this:

```python
my_dict = {}
```

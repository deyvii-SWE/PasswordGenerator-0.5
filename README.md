# Password Generator 0.5

## How the Program Works

It's pretty simple, just like the name suggests: it generates a password for you! You can customize its length and choose whether to include letters and special characters.

You can have a password with numbers and letters but without special characters, for example. However, numbers are the only non-customizable option here, as they are a **PRIORITY**.

We also have more features planned, such as saving passwords, but they are still a work in progress.

## About the Code

The first thing I want to show here is this part:

```python
def get_option():
    option = int(input(" +- Option: "))

    if option < 1 or option > 4:
        raise ValueError

    return option

try:
    in_option = get_option()
except ValueError:
```

I just noticed that I was repeating this validation logic way too often, so I turned it into a function that does exactly the same thing. Now I don't need to rewrite this logic every time, because we already have a function for it!

Now, let's talk about the main part of the code: password generation.

```python
# Password generation logic
def generate_password(interface):
    # Get all numbers as a string
    numbers = string.digits

    # Get lowercase and uppercase letters and merge them
    alpha_lower = string.ascii_lowercase
    alpha_upper = alpha_lower.upper()
    alpha = alpha_lower + alpha_upper

    # Get all punctuation characters as a string
    punctuations = string.punctuation

    # Put everything together
    everything = numbers

    if interface.alphabet_stats:
        everything += alpha

    if interface.punctuations_stats:
        everything += punctuations

    # Generate
    interface.set_password("".join(
        choice(everything)
        for _ in range(interface.password_size)
    ))
```

That was pretty simple! I imported `string` and `choice` from `secrets` (which is safer for password generation than using `random.choice`). I used `string` to get numbers, punctuation characters (special characters), and the entire alphabet without having to type everything out manually.

Then, I put everything together based on the alphabet and punctuation settings stored in the interface.

Finally, there's the generation part. I could return the password instead of storing it directly in the interface and save it later. That would probably be cleaner and more appropriate, since it's better when a function has just one clear responsibility.

```python
if in_option == 1:
    generate_password(interface)

space()
interface.display_password_generated()

try:
    in_option = get_option()
except ValueError:
    interface.display_invalid_option()
    in_option = None

if in_option != None:
    match in_option:
        case 1: # Generate
            pass
        case 2: # Copy
            pyperclip.copy(interface.password)
        case 3: # Exit
            break
        case _: 
            interface.display_invalid_option()
```

This time, in the main menu, I didn't use `while True` for the option validation. When the input raises a `ValueError`, the `except` block uses `continue` to send us right back to the beginning of the loop. However, we don't need it again in the other parts of the code.

For the options, I'm using `match/case`. I think it's a better fit for this situation and makes the code clearer.

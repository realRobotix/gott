# Features

  - [me](#me)
    - [role](#role)
      - [get](#get)
      - [remove](#remove)
    - [colour](#colour)
      - [rgb](#rgb)
      - [hex](#hex)
      - [random](#random)
  - [cat](#cat)
    - [breed](#breed)
    - [vote](#vote)
  - [dog](#dog)
    - [breed](#breed-1)
    - [vote](#vote-1)
  - [advice](#advice)
  - [smort](#smort)
  - [moderator](#moderator)
    - [messages](#messages)
      - [delete](#delete)

<br>

## Command Arguments

Types:

#### `int`: Numbers  
#### `str`: Letters & Numbers  
#### `bool`: True / False  
#### `member`: Mention of an user (@Robotix)  
#### `regex`: [Regular Expression](https://en.wikipedia.org/wiki/Regular_expression)

<br>

## me

### role

---

#### get

---

Syntax: `/me role get`

Give yourself a custom role which you can customize.

#### remove

---

Syntax: `/me role remove`

Remove your customizable role.

### colour

---

#### rgb

---

Syntax: `/me colour rgb [r: int] [g: int] [b: int]`

Change the colour of your rank to a RGB encoded colour.

#### hex

---

Syntax: `/me colour hex [hex: str]`

Change the colour of your rank to a HEX encoded colour.

#### random

---

Syntax: `/me colour`

Change the colour of your rank to a random colour.

## cat

### breed

---

Syntax: `/cat breed [page: int] [search: str]`

Returns an embed with information about cat breeds.  
You can jump to a specific page by providing [page] and you can limit the results by providing [search].

### vote

---

Syntax: `/cat vote`

Returns an embed with a picture of a cat.  
You can use the buttons to like, dislike and refresh the picture.

## dog

### breed

---

Syntax: `/dog breed [page: int] [search: str]`

Returns an embed with information about dog breeds.  
You can jump to a specific page by providing [page] and you can limit the results by providing [search].

### vote

---

Syntax: `/dog vote`

Returns an embed with a picture of a dog.  
You can use the buttons to like, dislike and refresh the picture.

## advice

Syntax: `/advice`

Returns random advice.

## smort

Syntax: `/smort`

Returns a random summary of a Wikipedia article.

## moderator

### messages

---

#### delete

---

Syntax: `/moderator messages delete [limit: int] [member: member] [regex: regex]`

Delete [limit] amount of Messages in the current text channel.  
You can further limit the Messages wich will be deleted by providing a [member] and/or a [regex].

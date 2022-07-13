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

---

Types:
<div style="padding-left: 2em">

#### `int`: Numbers  
#### `str`: Letters & Numbers  
#### `bool`: True / False  
#### `member`: Mention of an user (@Robotix)  
#### `regex`: [Regular Expression](https://en.wikipedia.org/wiki/Regular_expression)

</div>
<br>

## me

---
<div style="padding-left: 2em">

### role

---

<div style="padding-left: 2em"> 

### get

---

<div style="padding-left: 2em; padding-bottom: 2em;">

Syntax: `/me role get`

Give yourself a custom role which you can customize.

</div>

### remove

---

<div style="padding-left: 2em; padding-bottom: 2em;">

Syntax: `/me role remove`

Remove your customizable role.

</div>
</div>

### colour

---
<div style="padding-left: 2em">

### rgb

---

<div style="padding-left: 2em; padding-bottom: 2em;">

Syntax: `/me colour rgb [r: int] [g: int] [b: int]`

Change the colour of your rank to a RGB encoded colour.

</div>

### hex

---

<div style="padding-left: 2em; padding-bottom: 2em;">

Syntax: `/me colour hex [hex: str]`

Change the colour of your rank to a HEX encoded colour.

</div>

### random

---

<div style="padding-left: 2em; padding-bottom: 2em;">

Syntax: `/me colour`

Change the colour of your rank to a random colour.

</div>
</div>
</div>

## cat

---
<div style="padding-left: 2em">

### breed

---

<div style="padding-left: 2em; padding-bottom: 2em;">

Syntax: `/cat breed [page: int] [search: str]`

Returns an embed with information about cat breeds.  
You can jump to a specific page by providing [page] and you can limit the results by providing [search].

</div>

### vote

---

<div style="padding-left: 2em; padding-bottom: 2em;">

Syntax: `/cat vote`

Returns an embed with a picture of a cat.  
You can use the buttons to like, dislike and refresh the picture.
</div>
</div>

## dog

---

<div style="padding-left: 2em">

### breed

---

<div style="padding-left: 2em; padding-bottom: 2em;">

Syntax: `/dog breed [page: int] [search: str]`

Returns an embed with information about dog breeds.  
You can jump to a specific page by providing [page] and you can limit the results by providing [search].

</div>

### vote

---

<div style="padding-left: 2em; padding-bottom: 2em;">

Syntax: `/dog vote`

Returns an embed with a picture of a dog.  
You can use the buttons to like, dislike and refresh the picture.

</div>
</div>

## advice

---

<div style="padding-left: 2em; padding-bottom: 2em;">

Syntax: `/advice`

Returns random advice.

</div>

## smort

---

<div style="padding-left: 2em; padding-bottom: 2em;">

Syntax: `/smort`

Returns a random summary of a Wikipedia article.

</div>

## moderator

---

<div style="padding-left: 2em">

### messages

---

<div style="padding-left: 2em">

### delete

---

<div style="padding-left: 2em; padding-bottom: 2em;">

Syntax: `/moderator messages delete [limit: int] [member: member] [regex: regex]`

Delete [limit] amount of Messages in the current text channel.  
You can further limit the Messages wich will be deleted by providing a [member] and/or a [regex].

</div>
</div>
</div>

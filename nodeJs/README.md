# Node JS Tutorial
## Introduction
**`Node Js`** or **`Node`** is an **open source** and **cross-platform** runtime envirnonment for executing JavaScript code outside of a browser. Quite often we use `node` to build `back-end services` also called `apis` or `application programming interfaces`, these are the `services` that power our `client` **apllications** like a **web app** running inside of a **web browser** or a **mobile app** on a **mobile device**. These `client apps` are simply what the user sees and interact with, They're just the `surface` they need to talk to some `services` sitting on the `server` or in the `cloud` to store **data**, send **emails** or push **notifications**, kick off **workflows**,...

![Screenshot 2024-05-06 154500](https://github.com/elyse502/Practices/assets/125453474/a578d970-cd31-4903-a5ca-e36f1581f90a)

`Node` is ideal for building **Highly-scalable**, **data-intensive** and **real-time apps/back-end sevices** that power our `client applications`. Now you might ask but there are other `tools` and `frameworks` out there for building `back-end` services such as **asp.net**, **rails** & **Django**,... So what's special about `Node`?

* Well **`Node`** is easy to get started and can be used for `prototyping` and `agile development`, but it can also be used for building `super fast` and `highly scalable` services. It is used in production by large companies such as `PayPal`, `Uber`, `Netflix`, `Walmart`,... In fact at `PayPal` they rebuilt one of their `Java` and `spring` based **applications** using **`Node Js`** and they found that the `Node` application was built twice as fast with fewer people in 33% fewer lines of code and 40% fewer files and more importantly they doubled the number requests served per second while decreasing the average response time by 35%. So **`Node`** is an excellent choice for building `highly scalable` services

![Screenshot 2024-05-06 162536](https://github.com/elyse502/Practices/assets/125453474/92288b74-4dc7-44c4-a154-2cc252512f4d)

* Another reason for using **`Node`** is that in old applications we use `JavaScript`, so if you're a **Front-end Developer** and know `JavaScript` you can reuse your `JavaScript skills` and a **Transtion** to a `Full-stack` developer and get a better job with a better pay! You don't have to learn a new `programming language` also because you can use `JavaScript` both on the **Front-end** and on the **Back-end** your `source code` will be cleaner and more consistent, so you will use the same `naming conventions`, the same `tools` and the same `best practices`
* And finally another reason for using **`Node`** is that it has the largest `ecosystem` of `open source libraries` available to you! So for pretty much any **features** or **building blocks** you want to add to your `application`, there is some free `open source library` out there that you can use. So you don't have to build this `building blocks` from scratch and instead you can focus on the **core** of your `application`.

![Screenshot 2024-05-06 161439](https://github.com/elyse502/Practices/assets/125453474/be06371a-3cfe-423f-85ba-409840d27fb4)

---

## Node Architecture
So above we learnt that **`Node`** is a **runtime environment** for executing `JavaScript code`, but what is a **runtime environment** really? Well before **`Node`** we used `JavaScript` only to build `applications` that run inside of a `browser`, so every `browser` out there has what we call a `JavaScript Engine` That takes our `JavaScript code` and converts it to `code` that a `computer` can understand.

![Screenshot 2024-05-06 163736](https://github.com/elyse502/Practices/assets/125453474/c5a258d9-ec36-4194-9ff0-06f72b2482a2)

* For **example** `Micosoft Edge`  uses `chakra`, `Firefox` uses `SpiderMonkey` and `Chrome` uses `V8`.

![Screenshot 2024-05-06 164037](https://github.com/elyse502/Practices/assets/125453474/c570bb7a-153b-46cc-a025-f4bb2cab098c)

* And it's beacause of these **varieties** of `engines` that sometimes `JavaScript code` can behave differently in one `browser` or `another`. Now a `browser`provides a **runtime environment** for `JavaScript code`

![Screenshot 2024-05-06 164808](https://github.com/elyse502/Practices/assets/125453474/baa18290-0374-472e-8df1-78a037b81830)

* For **instance** you probably know that in `browsers` we have the `window` or the `document` **object**, these `objects` allow us to work with the `environment` in which our `code` is running.
```groovy
document.getElementById('');
```
* Now up to `2009` the only way to execute `JavaScript code` was inside of a `browser`.
  * In `2009` **`Ryan Dahl`** the creator of **`Node`** came up with a `brilliant idea`, he thought it would be great to execute `JavaScript` outside of a `browser`, so he took `Google's V8 Engine` which is the fastest `JavaScript Engine` out there and embedded it inside a `C++ program` and called that **program** `Node`. So similar to a `browser` **`Node`** is a **runtime environment** for `JavaScript code`, it contains a `JavaScript Engine` that can execute our `JavaScript code`, but it also has certain `objects` that provide an **environment** for our `JavaScript code`. But these `objects` are different from the `environment objects` we have in `browsers`, for **example:**
    * We don't have the `document object`, instead we have other `objects` that give us more interesting **capabilities**, for **example**; We can work with `file system`, listen for `requests` on a given `port`,... We can't do stuff like that inside of a `browser`, right?

**`browser's object:`**
```groovy
document.getElementById('');
```

**`Node's objects:`**
```groovy
fs.readFile()
```
```groovy
http.createServer()
```

![Screenshot 2024-05-06 165400](https://github.com/elyse502/Practices/assets/125453474/67f2b73e-e3cc-46bf-99a2-e4ee90cd76cd)

* **`Ryan Dahl's`** brilliant idea:

![Screenshot 2024-05-06 170057](https://github.com/elyse502/Practices/assets/125453474/721dc16d-ee49-4afe-b365-fe68bf15afa5)

* In `essence` **`Node`** is a `program` that includes the `V8 JavaScript Engine` plus some additional `modules` that give us **capabilities** not available inside `browsers`, we can work with the `file system` or the `network`,... Both `Chrome` and `Node` share the same `JavaScript Engine`, but they provide different **runtime environments** for `JavaScript`.
  * Some people compare **`Node`** to `C#` or `Ruby` or some other `Programming Languages`, but these **comparisons** are fundamentally **wrong!** Because **`Node`**  is not a `programming language`, it's like comparing a `car` with an `apple`. By the same `token` **`Node`** should not be compared with `frameworks` such as `ASP.NET` or `Rails` or `Django`,... These are `frameworks` for building `web applications`. **`Node`** is not a `framework`, it's a **runtime environment** for executing `JavaScript code`

![Screenshot 2024-05-06 172419](https://github.com/elyse502/Practices/assets/125453474/7e9b3274-dbf5-40fd-9bca-ca062d865e25)

![Screenshot 2024-05-06 172808](https://github.com/elyse502/Practices/assets/125453474/cb7d985f-0fac-4bc6-b977-7e7fb86d283f)

![Screenshot 2024-05-06 173015](https://github.com/elyse502/Practices/assets/125453474/85ce6aa0-7d32-42af-842d-15af425f0616)

![Screenshot 2024-05-06 173316](https://github.com/elyse502/Practices/assets/125453474/3938e6f3-2ca6-46a7-97df-9951f31f1909)

![Screenshot 2024-05-06 173520](https://github.com/elyse502/Practices/assets/125453474/6fc9b779-5669-4b84-b638-e91971b5d012)

---

## How Node works?
Above it's mentioned that `Node applications` are **Highly-scalable** and this is because of the `Non-blocking` or `ASYNCHRONOUS` nature of `Node`, what does it mean by `ASYNCHRONOUS` here is a **metaphor**; imagine you go to a restaurant a `waiter` comes to your `table` takes your `order` and gives it to the `kitchen` then they move on to serve another `table` while the `chef` is preparing your `meal`, so the same `person` can serve many different `tables`, they don't have to wait for the `chef` to cook one `meal` before they serve another `table`, this is what we call `Non-blocking` or `ASYNCHRONOUS` **architecture** and this is how `Node applications` work. The `waiter` is like a `thread` allocated ho handle a `request` so a single `thread` is used to handle multiple `requests`.

In contrast to `Non-blocking` or `ASYNCHRONOUS` **architecture** we have `Blocking` or `SYNCHRONOUS` **architecture**, let's see how this one works; So back to our `restaurant` **example** imagine you go to another `restaurant` and in that `restaurant` a `waiter` is allocated to you, they take your `order` and give it to the `kitchen` now they are sitting in the `kitchen` waiting for the `chef` to prepare your `meal` at this time they're not doing anything else, they're just waiting, they're not going to take an `order` from another `table` until your `meal` is ready! This is what we call `Blocking` or `SYNCHRONOUS` **architecture**, and that's how `applications` built with `frameworks` like `ASP.NET` or `Rails` work out of the `box`. So when we receive a `request` on the `server` a `thread` is allocated to handle that `request`, as part of handling that `requests` it is likely that we're going to **query** a `database` and as you know sometimes it may take a little while until the result is ready, when the `database` is executing the **query** that `thread` is sitting there waiting. It can't be used to serve another `client`, so we need a new `thread` to serve another `client`.

* `Non-blocking` OR `ASYNCHRONOUS` Architecture

![Screenshot 2024-05-06 174931](https://github.com/elyse502/Practices/assets/125453474/7972032d-074d-440f-8c46-c5f1ae207f69)

https://github.com/elyse502/Practices/assets/125453474/3cb82345-707e-4bda-8a48-8b038ef3de25

* `Blocking` OR `SYNCHRONOUS` Architecture

![Screenshot 2024-05-06 181823](https://github.com/elyse502/Practices/assets/125453474/c78763f2-181d-44ed-88f9-282ae06ff7a2)

https://github.com/elyse502/Practices/assets/125453474/d1e83b4e-4db2-4ff0-95f8-d293573e9c36

Now imagine what would happen if we have a large number of `concurrent clients`, at some point we're going to run out of `threads` to serve these `clients`, so new `clients` have to wait until `three threads` are available or if we don't want them to wait, we need to add more `hardware`, So with this kind of **architecture** we are not utilizing our resources efficiently. This is the problem with `Blocking` or `SYNCHRONOUS` **architecture** and as expalined that's how `applications` built with `frameworks` like `ASP.NET` work by default of course in `ASP.NET`, it is possible to use `ASYNCHRONOUS` **architecture** but you will have to do extra work for now, in contrast `Node applications` are **asynchronous** by default, so you don't have to do anything extra.

![Screenshot 2024-05-06 183419](https://github.com/elyse502/Practices/assets/125453474/a1c0276b-d6af-4b47-af7d-a4d11d3e4b02)

![Screenshot 2024-05-06 183636](https://github.com/elyse502/Practices/assets/125453474/493fd2fc-46e4-450b-9ad6-d0b7a14151ae)

![Screenshot 2024-05-06 183821](https://github.com/elyse502/Practices/assets/125453474/f1b376f6-59d5-4a94-8ab6-48190b4385c5)

In `Node` we have a single `thread` to handle all `requests`, when a `request` arrives that single `thread` is used to handle that `request`, if you need to **query** a `database` or `thread` doesn't have to wait for the `database` to return the `data`. 

![Screenshot 2024-05-06 195618](https://github.com/elyse502/Practices/assets/125453474/2a17b2fa-87d2-499d-bc69-48028c064756)

While the `database` is executing our `query` that `thread` will be used to serve another `client`, when the `database` prepares the **result** it puts a message in what we call an `Event queue`.

![Screenshot 2024-05-06 200016](https://github.com/elyse502/Practices/assets/125453474/ed7a5a93-30e4-49f0-ba75-4abb82b3e272)

![Screenshot 2024-05-06 200058](https://github.com/elyse502/Practices/assets/125453474/927acb34-25fa-490d-bc57-e715a9fab944)

**`Node Js`** is continuously monitoring this `queue` in the **background**, when it finds an event in this `queue` it will take it out and process it, this kind of **architecture** makes `Node` ideal for building `applications` that include a lot of `disk` or `network` **access**.

![Screenshot 2024-05-06 200429](https://github.com/elyse502/Practices/assets/125453474/822518a5-bc7e-4b22-be8c-1247ca8b3202)

![Screenshot 2024-05-06 200807](https://github.com/elyse502/Practices/assets/125453474/c7c56b40-90aa-43c2-a784-0b61084bb934)

* We can serve more `clients` without the need to throw in more `hardware` and that's why `Node applications` are **Highly-scalable**. 

![Screenshot 2024-05-06 201209](https://github.com/elyse502/Practices/assets/125453474/3487e1f0-9fd7-46f0-8891-41c4e3338635)

* In contrast **`Node`** should not be used for `CPU-intensive` **applications** like a `video encoding` or an `image manipulation service`, in this kind of applications we have a lot of calcuations that should be done by `CPU` and few `operations` that touch the `file system` or the `network`

![Screenshot 2024-05-06 201454](https://github.com/elyse502/Practices/assets/125453474/3a9d6f3d-6d74-461e-9ee7-585baa2e84ed)

* Since `Node applications` are single `threaded` when performing the calculation to serve one `client` other `clients` have to wait, and that's why `Node` should not be used for `CPU-intensive` **applications**. It should only be used for building `data-intensive` and `real-time` **applications**.

![Screenshot 2024-05-06 202342](https://github.com/elyse502/Practices/assets/125453474/0812ba13-d0da-4c9a-b394-34ee303fa786)




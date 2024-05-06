# Node JS Tutorial
## Introduction
**`Node Js`** or **`Node`** is an **open source** and **cross-platform** runtime envirnonment for executing JavaScript code outside of a browser. Quite often we use `node` to build `back-end services` also called `apis` or `application programming interfaces`, these are the `services` that power our `client` **apllications** like a **web app** running inside of a **web browser** or a **mobile app** on a **mobile device**. These `client apps` are simply what the user sees and interact with, They're just the `surface` they need to talk to some `services` sitting on the `server` or in the `cloud` to store **data**, send **emails** or push **notifications**, kick off **workflows**,...

![Screenshot 2024-05-06 154500](https://github.com/elyse502/Practices/assets/125453474/a578d970-cd31-4903-a5ca-e36f1581f90a)

`Node` is ideal for building **Highly-scalable**, **data-intensive** and **real-time apps/back-end sevices** that power our `client applications`. Now you might ask but there are other `tools` and `frameworks` out there for building `back-end` services such as **asp.net**, **rails** **Django**,... So what's special about `Node`?

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
  * Some people compare **`Node`** to `C#` or `Ruby` or some other `Programming Languages`

![Screenshot 2024-05-06 172419](https://github.com/elyse502/Practices/assets/125453474/7e9b3274-dbf5-40fd-9bca-ca062d865e25)







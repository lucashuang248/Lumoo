{% include navigation.html %}

## 1 Minute Video: https://www.loom.com/share/52a2145758c1432e8b7eec24cf662178
[Create Task Video](https://drive.google.com/file/d/19WveZC_9lHEb9BbEP6NmZ4k68LnXI8TT/view?usp=sharing)

# PBL Feature: Collectable Recommendation Filter

Description: 
> Users are given a tree structure survey in which they will select a series of options based on their interests which finally displays a recommendation. The **GOAL** is to provide users with a Funko Pop recommendation that will be based on the answers that they choose and in this case, will display a Funko Pop that we think they will like.   

***

### Inspiration/Layout Idea
We will use the idea of a binary tree or a tree format in general. This will have different branches which will eventually lead to an outcome or in this case, a recommendation. 

Binary Tree Layout
> ![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/binary-tree-to-DLL.png)

Tree Structure/Brainstorming Web Layout
> ![](https://www.researchgate.net/profile/Masoud-Sattari/publication/271952500/figure/fig1/AS:392074961670149@1470489363273/Simple-tree-structure-of-activities.png)

***


## Plan: Use a series of buttons in a tree-like format which finally leads to a collection of funkos to choose from. 
Here is our tree structure plan and what we imagine implementing into our website: 

> ![IMG_5445 HEIC](https://user-images.githubusercontent.com/89277966/153532546-2d0c0d0e-c098-401e-b7ff-ad47af59af4f.jpg)

***

### Week 9 Plan: 
1. Create Plan and outline on the Wiki. Include Images. 
2. Plan for the next 3 weeks.
3. Create a wireframe.
![Funko Pop Recommendations Wireframe](https://cdn.discordapp.com/attachments/645054705847762944/941596065755447306/unknown.png)
4. Begin the code. 

### Week 10 Plan: 
1. Continue working on create-task plan and make more branches for the trees. 
2. Insert/substitute photos in for buttons.
3. Clean/Polish up the page.

### Week 11 Plan: 
1. Re-set up deployment instance again (deleted because I thought it was charging money).
2. Get domain and everything up and running again with updated website. 
3. Clean up make the website look better, fix bugs, organize for final submit. 


***


## For the Future:

### Create Performance Task General Requirements 

You will be provided with a significant amount of class time during the remainder of the trimester to complete and submit the following

1. Final program code (created independently or collaboratively) 
2. A video that displays the running of your program and demonstrates functionality you developed (created independently) 
3. Written responses to all the prompts in the performance task (created independently)

***

## Written Portion

### 3a. Provide a written response that does all three of the following: 
#### i. Describes the overall purpose of the program
The overall purpose of the program is to help the users of the website choose a Funko Pop they like based on their opinion of different shows.
#### ii. Describes what functionality of the program is demonstrated in the video
My partner and I made a survey based on the binary tree concept where we start from a few different choices and slowly narrow them down to help the user choose their best options. We did this by putting images on a html file that directs to different files based on what the user chooses, the content presented is slowly narrowed down until the user reaches the end and have their results displayed.
#### iii. Describes the input and output of the program demonstrated in the video
The input of the program are the parameters from onclick and the output is the dropdown below.

### 3b. Capture and paste two program code segments you developed during the administration of this task that contain a list (or other collection type) being used to manage complexity in your program.
#### i. The first program code segment must show how data have been stored in the list. 
```
def recommendations():
    topic = [
        {"topic": "/static/assets/LGcreatetask/animebutton.PNG", "file": "/subcategories1/"},
        {"topic": "/static/assets/LGcreatetask/fortnitebutton.PNG", "file": "/subcategories2/"},
        {"topic": "/static/assets/LGcreatetask/marvelbutton.PNG", "file": "/subcategories3/"},
        {"topic": "/static/assets/LGcreatetask/starwarsbutton.PNG", "file": "/subcategories4/"},
    ]
    return render_template("LGcreatetask/recommendations.html", topic=topic)
```
#### ii. The second program code segment must show the data in the same list being used, such as creating new data from the existing data or accessing multiple elements in the list, as part of fulfilling the program’s purpose
```
<div class="buttons">
    {% for x in topic %}
    <!--    iteration that puts dictionary under route in main.py repeatedly inside "buttons" css-->
    <div>
        <a href="{{x['content']}}">
            <img src={{x["topic1"]}} alt="none" style="height: 180px;">
        </a>
    </div>
    {% endfor %}
```
#### iii. Identifies the name of the list being used in this response
"topic"
#### iv. Describes what the data contained in the list represent in your program
The data contained in the list are image file names and directory to different html pages
#### v. Explains how the selected list manages complexity in your program code by explaining why your program code could not be written, or how it would be written differently, if you did not use the list
The list manages complexity in my program by making iteration possible. Without the list I would have to list out each image url and app route in the html file itself and add css to each of them, but with the list I can just loop the image url and app routes I want in my html with a few lines of code.

### 3c. Capture and paste two program code segments you developed during the administration of this task that contain a student-developed procedure that implements an algorithm used in your program and a call to that procedure.
#### i. The first program code segment must be a student-developed procedure that
- [x] Defines the procedure’s name and return type (if necessary) 
- [x] Contains and uses one or more parameters that have an effect on the functionality of the procedure
- [x] Implements an algorithm that includes sequencing, selection, and iteration
```
<h1 style="text-align: center; color: white;">Marvel Categories</h1>
<div class="dropdown">
    <input src="/static/assets/LGcreatetask/avengersbutton.png" alt="none" type="image" class="dropbtn" onclick="myFunction('myDropdown')">
    <div id="myDropdown" class="dropdown-content">
        <a href="https://www.amazon.com/Funko-Avengers-Endgame-Glow-Dark/dp/B083YS9R43/ref=sr_1_3?keywords=marvel+funko+pop&qid=1646038826&sr=8-3">Iron Man</a>
        <a href="https://www.amazon.com/Funko-Pop-Deluxe-Marvel-Exclusive/dp/B083W31TBK/ref=sr_1_5?crid=22JL7JSG55R6Y&keywords=avengers+funko+pop&qid=1646038970&sprefix=avengers+funko+pop%2Caps%2C135&sr=8-5">Hulk</a>
        <a href="https://www.amazon.com/Funko-Pop-Marvel-Strange-Exclusive/dp/B08QXQK2VN/ref=sr_1_13?keywords=marvel+funko+pop&qid=1646038826&sr=8-13">Dr. Strange</a>
    </div>
</div>

<div class="dropdown">
    <input src="/static/assets/LGcreatetask/guardiansofthegalaxybutton.png" alt="none" type="image" class="dropbtn" onclick="myFunction('myDropdown1')">
    <div id="myDropdown1" class="dropdown-content">
        <a href="https://www.amazon.com/Funko-Pop-Marvel-Gamora-Daughter/dp/B08MQGSGZZ/ref=sr_1_1?crid=RXSTNYKYD0VL&keywords=guardians+of+the+galaxy+funko+pop&qid=1646038891&sprefix=guardians+of+the+galaxy+funko+pop%2Caps%2C125&sr=8-1">Gamora</a>
        <a href="https://www.amazon.com/Funko-POP-Movies-Guardians-Toddler/dp/B01M7YNDXI/ref=sr_1_4?crid=RXSTNYKYD0VL&keywords=guardians+of+the+galaxy+funko+pop&qid=1646038891&sprefix=guardians+of+the+galaxy+funko+pop%2Caps%2C125&sr=8-4">Groot</a>
        <a href="https://www.amazon.com/Funko-5177-POP-Marvel-Guardians/dp/B00RUE4L18/ref=sr_1_6?crid=RXSTNYKYD0VL&keywords=guardians+of+the+galaxy+funko+pop&qid=1646038891&sprefix=guardians+of+the+galaxy+funko+pop%2Caps%2C125&sr=8-6">Nebula</a>
    </div>
</div>

<div class="dropdown">
    <input src="/static/assets/LGcreatetask/norsemythologybutton.png" alt="none" type="image" class="dropbtn" onclick="myFunction('myDropdown2')">
    <div id="myDropdown2" class="dropdown-content">
        <a href="https://www.amazon.com/Funko-Pop-Marvel-Loki-President/dp/B08T5TWX96/ref=sr_1_4?keywords=marvel+funko+pop&qid=1646038826&sr=8-4">Loki</a>
        <a href="https://www.amazon.com/Funko-Pop-Deluxe-Marvel-Exclusive/dp/B0892SWZCV/ref=sr_1_1_sspa?crid=22JL7JSG55R6Y&keywords=avengers+funko+pop&qid=1646038963&sprefix=avengers+funko+pop%2Caps%2C135&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzRTdFNlJGNExMM0pRJmVuY3J5cHRlZElkPUEwNDQ2Mjc5Mlo1M1lBTDJSSFFUMCZlbmNyeXB0ZWRBZElkPUEwMjQ5OTE2M1Y1OUozREIxN1lDQSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=">Thor</a>
        <a href="https://www.amazon.com/Funko-Odin-Compatible-Graphical-Protector/dp/B07N95SVLQ/ref=sr_1_1?crid=1DMKZQNAQ1AMF&keywords=odin+funko+pop&qid=1646039020&sprefix=odin+funko+pop%2Caps%2C121&sr=8-1">Odin</a>
    </div>
</div>
```
#### ii. The second program code segment must show where your student-developed procedure is being called in your program
```
<script>
    /* When the user clicks on the button,
    toggle between hiding and showing the dropdown content */
    function myFunction(myDropdown) {
        document.getElementById(myDropdown).classList.toggle("show");
    }

    // Close the dropdown if the user clicks outside of it
    window.onclick = function(event) {
        if (!event.target.matches('.dropbtn')) {
            var dropdowns = document.getElementsByClassName("dropdown-content");
            var i;
            for (i = 0; i < dropdowns.length; i++) {
                var openDropdown = dropdowns[i];
                if (openDropdown.classList.contains('show')) {
                    openDropdown.classList.remove('show');
                }
            }
        }
    }
</script>
```
#### iii. Describes in general what the identified procedure does and how it contributes to the overall functionality of the program
The procedure takes in the id parameter of the onclick function of each dropdown layout and 

### 3d. Provide a written response that does all three of the following:
#### i. Describes two calls to the procedure identified in written response 3c. Each call must pass a different argument(s) that causes a different segment of code in the algorithm to execute.
First call: 
```
    <input src="/static/assets/LGcreatetask/avengersbutton.png" alt="none" type="image" class="dropbtn" onclick="myFunction('myDropdown')">
```
Second call: 
```
    <input src="/static/assets/LGcreatetask/guardiansofthegalaxybutton.png" alt="none" type="image" class="dropbtn" onclick="myFunction('myDropdown1')">
```
#### ii. Identifies the result of each call
Result of the first call: Drop down below the avengers image
Result of the second call: Drop down below the guardians of the galaxy image

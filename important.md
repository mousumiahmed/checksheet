



javascript and react:

<https://github.com/airbnb/javascript>

Bootstrap

<https://hackerthemes.com/bootstrap-cheatsheet/#dropright>

Mongodb class video:

https://drive.google.com/open?id=18ORTLhKHTEmlWpZZN8IXoml1aMZuMd9g

https://drive.google.com/open?id=175gA9Z3u8rRCfmFYcKVsgOzXETsWYZi2

https://drive.google.com/open?id=1abdlEdLzseDsx3HH7Yhl2KcqyhHts-i7

https://drive.google.com/open?id=1mGtOb_4C7kUsJ2uTZjsYqJxHx-sX2oKR

https://drive.google.com/open?id=1t17_9LrmrkU3wCNl8Gzqnyrh3L9ZIXI5





https://docs.mongodb.com/manual/applications/data-models-tree-structures/



Hekarrank class:

https://drive.google.com/drive/folders/1YUPppn5qwax41TXmjegUFRmhltWNU2KM?usp=sharing













<https://medium.com/fbdevclagos/a-complete-guide-to-building-a-restful-api-using-node-express-and-mongodb-9712619f7172>

<https://medium.com/fbdevclagos/developing-basic-crud-operations-with-node-express-and-mongodb-e754acb9cc15>

<https://medium.com/fbdevclagos/setting-up-your-development-environment-96a6858ed5bb>

https://medium.com/employbl/depth-first-and-breadth-first-search-on-trees-in-javascript-58dcd6ff8de1

https://github.com/trekhleb/javascript-algorithms/tree/master/src/algorithms/graph/depth-first-search

Albert:

https://github.com/albseb511/frontend/blob/master/day_001/frontend_001.md

https://masaischool.slack.com/archives/CKAA9S3S9/p1567598064070700?thread_ts=1567596049.065400

https://masaischool.slack.com/archives/CKAA9S3S9/p1568046794024800

https://masaischool.slack.com/archives/CKAA9S3S9/p1567572340046700

https://codesandbox.io/s/props-parent-child-sibling-r2bwu

Class videos:

https://drive.google.com/drive/folders/1eELQcJST9eHCSYDyLpcBFYM5dGuzLz_7



Hakerank:

Links of all contests so far:

www.hackerrank.com/arrays-day-1
www.hackerrank.com/arrays-day-2
www.hackerrank.com/arrays-day-3
www.hackerrank.com/arrays-and-strings-day-4
www.hackerrank.com/arrays-and-strings-day-5
www.hackerrank.com/arrays-and-strings-day-6
www.hackerrank.com/arrays-and-strings-day-7
www.hackerrank.com/arraystrings-and-stacks-day-8
www.hackerrank.com/data-structures-day-9
www.hackerrank.com/data-structures-day-10
www.hackerrank.com/data-structures-day-11
www.hackerrank.com/data-structures-day-12
www.hackerrank.com/data-structures-day-13
https://www.hackerrank.com/data-structures-day-14-a
https://www.hackerrank.com/data-structures-day-14-b
https://www.hackerrank.com/data-structures-day-14-c
www.hackerrank.com/vikings-data-structures-day-15
https://www.hackerrank.com/vikings-data-structures-day-16
https://www.hackerrank.com/vikings-data-structures-day-17
https://www.hackerrank.com/vikings-data-structures-day-18
https://www.hackerrank.com/vikings-algorithms-day-19
https://www.hackerrank.com/vikings-algorithms-day-20
http://www.hackerrank.com/vikings-algorithms-day-21
https://www.hackerrank.com/vikings-algorithms-day-22
https://www.hackerrank.com/vikings-algorithms-day-23
https://www.hackerrank.com/vikings-algorithms-day-24
www.hackerrank.com/vikings-algorithms-day-25
www.hackerrank.com/data-structures-algo-mock-2

It is your responsibility to collate and keep all the links for practice and future refrences























https://drive.google.com/file/d/1ygAhhUSXl8SYzFjNPF-J7JzaDvXrfQhQ/view?usp=sharing

https://drive.google.com/open?id=1EQpOLrvY-sqX2GtqF-pw6cIEVoCJi2Q9

**https://drive.google.com/open?id=1EQpOLrvY-sqX2GtqF-pw6cIEVoCJi2Q9**

https://drive.google.com/open?id=1umUVTNr7h_phpxIgoS2fZXyOweV9h4i7

https://www.hackerrank.com/contests/arrays-and-strings-day-7



 var newArr = input.split('\n');
    var els = newArr[1];
    els = els.split(' ');
    els = els.map(el=>Number(el));



var newArr = input.split(' ');
    newArr = newArr.map(num => Number(num));



var newArr = input.split('\n');
    var bats1 = newArr[1];
    var bats2 = newArr[2];
    bats1 = bats1.split(' ');
    bats1 = bats1.map(score=>Number(score));
    bats2 = bats2.split(' ');
    bats2 = bats2.map(score=>Number(score)); 

var newArr = input.split('\n')[1];
    newArr = newArr.split(' ');
    newArr = newArr.map(el=>Number(el)); 



var data = input.split('\n');
    var firstLine = data[0].split(' ');
    var len = firstLine[0];
    var arr = data[1].split(' ');





var arr = input.split("\n")
    var data=arr[1].split(" ")
    let final=[],product=1;
   for(let i=0;i<data.length;i++)
       {
           final.push(Number(data[i]))
       }

function processData(input) {
    //Enter your code here
    var arr = input.split("\n")
    arr.shift()
   // console.log(arr);
    var data=[];
    var a=[];
    for(var i=0;i<arr.length;i++){
       a.push(arr[i].split(" "));        
    }
    



Waiting Line Problem:

    function processData(input) {
        //Enter your code here
        var arr = input.split("\n")
        arr.shift()
       // console.log(arr);
        var data=[];
        var a=[];
        for(var i=0;i<arr.length;i++){
           a.push(arr[i].split(" "));        
        }
        
        //console.log(a);
        for(var i=0;i<a.length;i++){
            if(a[i][0]=='E'){
            data.push(a[i][1]);
            console.log(data.length);
           }
           else if(a[i][0]=='D' && data.length!==0){
                var ele=data[0];
               data.shift()
                //console.log(ele);
                //data.pop()
                console.log(ele+" "+data.length)
            }else if(a[i][0]=='D' && data.length==0){
                console.log(-1+" "+data.length)
            }


​            
​            
​            var arr = input.split("\n")
​        var data=arr[1].split(" ")
​        let final=[],product=1;
​       for(let i=0;i<data.length;i++)
​           {
​               final.push(Number(data[i]))
​           }


​       
​        }
​        
​    } 

   function processData(input) {
    //Enter your code here
    var arr = input.split("\n")
    arr.shift()
   // console.log(arr);
    var data=[];
    var a=[];
    for(var i=0;i<arr.length;i++){
       a.push(arr[i].split(" "));        
    }
    



    }

} 



https://www.hackerrank.com/arrays-day-2



 Morning lecture video - https://drive.google.com/file/d/1Fwi7Oc151rG2f9NdSbU1dK3__-sfxdPv/view?usp=sharing 

https://www.hackerrank.com/arrays-day-3

https://www.youtube.com/playlist?list=PLxB5dizTJPofK1Un-7YJOxHc9LGYI4sgI

https://drive.google.com/open?id=1BwQyASyemSEOcXXmZjdJIlYzUF-v3FGG

https://www.hackerrank.com/challenges/array-left-rotation/problem

https://github.com/masai-school/full-stack-dev/wiki/MongoDB-Installation

https://drive.google.com/open?id=18ORTLhKHTEmlWpZZN8IXoml1aMZuMd9g

https://drive.google.com/open?id=12RePJqmbpmfz333sIM6Dh2ae_07FvHdb

https://www.hackerrank.com/arrays-and-strings-day-4

https://drive.google.com/file/d/1RUD904gNTWwoy5jMS12NyX_wb6J4VQU4/view?usp=sharing

https://drive.google.com/open?id=1hob44gUwkEiBAQ4tUx71wq3gftxOctD-

https://drive.google.com/open?id=175gA9Z3u8rRCfmFYcKVsgOzXETsWYZi2

https://drive.google.com/open?id=1IcVKFQJV2ErYyNwISdrsCJ-Ui9t8d58e

https://docs.google.com/forms/d/e/1FAIpQLSdy85kKfhNc9vTnYU5CzR9QCUr3E0_X61Z-RVpMAyvqf2p9Aw/viewform?usp=sf_link

https://www.khanacademy.org/computing/computer-science/algorithms/recursive-algorithms/a/using-recursion-to-determine-whether-a-word-is-a-palindrome

https://www.hackerrank.com/contests/arrays-and-strings-day-5

https://drive.google.com/file/d/1s8j9FnwWxtnSMjxKxiksrVcJRHeqYLIQ/view?usp=sharing

https://drive.google.com/file/d/15rBFQTExQ0yWDodzxMaFJ_6HZSNozj_Y/view

****

https://www.hackerrank.com/arrays-and-strings-day-6

package com.masaischool.dashboard;

import java.util.Scanner;

public class Matrix {
    public static void main(String args[]) {

        Scanner in = new Scanner(System.in);
    
        // how to take string in javascript
        String inputFirstLine = in.nextLine();
        
        // splitting the string input and converting to string array
        String[] inputs = inputFirstLine.split(" ");
        
        // convert strings to integer
        int N = Integer.parseInt(inputs[0]);
        int M = Integer.parseInt(inputs[1]);
        System.out.println(N + " " + M);
    
        // initialisation of 2D array or matrix
        int[][] A = new int[N][M];
        int sum = 0;
        
        /*
         * 
         * 00 01 02
         * 10 11 12
         * 20 21 22
         * 
         * [ 0 -> N-1 ]
         * 
         * 3*3
         * 
         * 
         */
    
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                System.out.println(i+""+j);
                A[i][j] = in.nextInt();
                System.out.println(A[i][j]);
                sum += A[i][j];
            }
        }
        in.nextLine(); // dont worry about this line
        
        // initialisation of temporary sum2 variable
        int sum2 = 0;
        
        // repetition of above lines
        String inputLaterLine = in.nextLine();
        String[] inputs2 = inputLaterLine.split(" ");
        int n = Integer.parseInt(inputs2[0]);
        int m = Integer.parseInt(inputs2[1]);
        System.out.println(n + " " + m);
    
        // initialisation of 2D array or matrix
        int[][] B = new int[n][m];
    
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                B[i][j] = in.nextInt();
                System.out.println(B[i][j]);
                sum2 += B[i][j];
            }
        }
    
        System.out.println(Math.max(sum, sum2));
    
        in.close();
    
    }
}





http://hackerrank.com/data-structures-day-10

function processData(input) {
    //Enter your code here
    var arr = input.split("\n")
    arr.shift()
   // console.log(arr);
    var data=[];
    var a=[];
    for(var i=0;i<arr.length;i++){
       a.push(arr[i].split(" "));        
    }
    

    //console.log(a);
    for(var i=0;i<a.length;i++){
        if(a[i][0]=='E'){
        data.push(a[i][1]);
        console.log(data.length);
       }
       else if(a[i][0]=='D' && data.length!==0){
            var ele=data[0];
           data.shift()
            //console.log(ele);
            //data.pop()
            console.log(ele+" "+data.length)
        }else if(a[i][0]=='D' && data.length==0){
            console.log(-1+" "+data.length)
        }

   




















    }

} 



https://www.w3schools.com/jsref/jsref_obj_array.asp

https://drive.google.com/file/d/1FMa25VNHlu3WdxXVkdwQm2MEW3EEHC6q/view?usp=sharing

https://drive.google.com/file/d/1W9mSkJNkiZFz6wSDPXZdcnzuFA5jhPFO/view?usp=sharing



python:

https://drive.google.com/open?id=1ROhuYp2Eue_xPamiA8auUpf70k4vRV4h

https://drive.google.com/open?id=1KucCrjTR1VJov1PWkOhQzaMEgYtz6O1x

https://drive.google.com/open?id=1AYrLMBMVoNRc1mc1K2sWQF-RWNiuaWf1

https://drive.google.com/open?id=1buU1o2MKadL-Obx5XwGTFaiS5rKn527S

https://drive.google.com/open?id=16CT8eoIC9m_kpdav0_k-BgQRNpqeFC5q

https://drive.google.com/open?id=1uydeReonLa_cotijK_qD7rFwwLd3hW0b

https://github.com/masai-school/full-stack-dev/wiki/Python-Installers

https://drive.google.com/open?id=1yMuUExN8DoZ6hTlOubKcK4AYQ5Jrvozi

https://drive.google.com/open?id=1IuSlfV0nTWyWznDZQe_ehu1kRPXrU_YT

https://drive.google.com/open?id=1--ZMzC7YDzCDWMKFy8z9BQp00uO0N_tS



```py
python -m pip install flask
```

```
export FLASK_ENV=development
export FLASK_DEBUG=1
$ export FLASK_APP=server.py
$ flask run
```

**MONDAY TO THURSDAY**
9.00    9.15    SCRUM
9.15    10.00    DS CLASS    SECOND WEEK ONWARD STUDENT EXPLANATION SESSIONS
10.00    11.30    HACKERRANK
11.45    12.30    CODING CLASS
12.30    1.30    FRONT END TEST
1.30    2.30    LUNCH
2.30    9.00    CODING SESSIONS
5.30    6.30    SOFT SKILLS
8.00    8.30    PRATEEK SESSIONS
8.30    9.00    COACHING TO SPARTANS BY VIKINGS
**FRIDAY**
9.00    9.15    SCRUM
9.15    10.00    CODING CLASS
10.00    12.30    CODING SESSION
12.30    1.30    FRONT END TEST
2.30    4.00    CODING PRACTISE
4.00    9.00    DS DISCSSIONS
5.30    6.30    SOFT SKILLS
**SATURDAY**
9.00    9.15    SCRUM
9.15    5.00    PROJECT
5.00    6.00    CODE TAKERS
6.00    8.00    SPILL OVER FOR THE WEEK, REVIEWS, DISCUSSIONS









react-redux curd app-

https://www.thegreatcodeadventure.com/building-a-simple-crud-app-with-react-redux-part-1/

https://egghead.io/lessons/react-redux-the-single-immutable-state-tree

Project:

https://docs.google.com/document/d/1iE4IiIJPGxXLwDHPEuXv79Rln2xxmc8W_9fzaVJ4Kjk/edit?usp=sharing

note:

https://github.com/masai-school/full-stack-dev-1908/blob/master/course/week_9/day_2/notes_1.md



calculator

<https://codepen.io/anneklapwijk/pen/vKGLMx/?editors=1010>



Memoization is the same concept of storing the result so that you don't have to recalculate it. => Trading space for time. That's where dynamic programming optimizes time complexity. Hope it's clear
The cache[] array was Memoization



https://postimages.org/
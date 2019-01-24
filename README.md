## Welcome to a-r0n and codebrotherone's data visualization 2 day challenge


### Challenge
 *Create a Data Science visualization of some sort using Python, Javascript, etc... in 2 days!*
 
### Solution

Create a cool interactive d3.js map with locations of national park services added to the map. Served via GithubPages!

### What did we learn?

Never having used d3.js before (aside from simple graphs and charts, and c3.js) we learned many different things about this js package. 

1. *d3.js is **not easy** to learn! It is also not a visualization library!*

  - In fact, it is quite difficult to master as it is quite unique in it's implementation

  - This library gives the user the *tools* required to build components which can *then be used as visualizations*
  
  
2. *d3.v3.js and d3.v4.js have huge differences!*
 
  - There are many differences between the version 3 and 4 of the js package, which is something we initially struggled with. 


3. *Projections are cool!*
 
  - Most people are familiar with mercator projections, but we decided to use the AlbersUSA projection in d3. 
 
  - These projections are based on formulas which can take into account (standard parallels, center position, etc...)
 
  - Knowing the projection *greatly simplifies* the process so we don't have to guess and tune the parameters required for translating (lat, long) -> projected svg coordinates 


*More to come! Currently at < 1 day left for this project.*

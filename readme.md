# Wiki Project
## For CS50w Project 1, a Django based Wiki project.

### Tasks
* ~~Entry Page~~
* ~~Index Page~~
* ~~Search~~
* ~~New Page~~ 
* ~~Edit Page~~
* ~~Random Page~~
* ~~Markdown to HTML~~

### Project Log
#### 7.3.21
Entry form is functional, creates new .md file, validation in place, displays error message. Needs to redirect to individual entry page once that view is established.

Core functionality is done. Can create, edit and view posts. Need to implement search and markdown conversion.

### 7.4.21
Search function works, but needs improvement. Want 'enter' key to submit, case matching, etc. (Fireworks suck.)

### 7.5.21
Trying to make search better with case sensitivity removed. Convert list to lowercase, see if its in the lowercased list. If so, get the query from the original list at that same index...if I can get the index. All set!

Going to put this project on pause for now, as the core functionality is there. Might return to spit and polish later. 

TODO:
* Clean up search functionality. 
* Do some new styling, maybe try to work with something like Tailwind?

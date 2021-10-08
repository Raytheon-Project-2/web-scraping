# GitHub for Data Mine CP Raytheon BI team

* note: install git on local machine

# Section 1: Intro to GitHub
	GitHub is a version control software for managing coding projects. The main functionalities of GitHub
	are the ability to have a repository that contains all of the files nessecary for a project. From the 
	repository, there are some key functions that help with version control.
	
	1. Branching: Initially, a repository will start out with 1 branch called the main or master branch. This 
				  branch is where the final code will be located. For best practices, it is common to create a 
				  new branch off of the main branch to test and write new code related to the project.
	2. Commit: Committing is analagous to saving. Once a change is made to file, committing it will save the progress
			   that has been made.
	3. Push: Pushing will update the changes that were made to the file to GitHub.
	4. Merge/Pull request: If there are multiple working branches, the merge/pull request function is used to merge the branch
	   with another one (typically main). Submitting a pull request allows the admin of the repository to look over the change
	   that were made on a branch to determine wether or not to merge the changes to the main code.
	
# Section 2: Typical work flow using GitHub
	In this section, we will discuss how the typical work flow would look like when using Github. This is to give a general overview 
	of work flow so there might be slight discrepancies depending on the IDE you use. First, you want to clone the repository you 
	will be using to your local system. This will enable you to edit the files located in the repository. Once cloned, you can start
	editing any file located in the repository. Once a change is made, commit the change and push it to GitHub. If you are working in 
	a different branch other than main, the changes that were pushed will only affect the branch you are working in. If you want to see
	the changes that were made in the main branch, submit a pull request to the main branch which will enable the repository admin to merge
	the changes.

* This is just a brief introduction to GitHub. All information presented is what I have learned so far. I am not an expert at using GitHub.
	
References:
1. For VS code users: https://www.youtube.com/watch?v=3Tn58KQvWtU&list=PLpPVLI0A0OkLBWbcctmGxxF6VHWSQw1hi&index=1&ab_channel=DevWorld
2. Intro to GitHub: https://guides.github.com/activities/hello-world/

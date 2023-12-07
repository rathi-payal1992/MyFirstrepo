## Branching strategy

Currently we are following git flow partially where we have one main branch.
For everychange a new feature branch needs to be created and once the changes are completed a pull request is to be raised to main from the feature branch.

Once a pull request is raised, it has to be reviewed by anyone of a pre-approved list of approvers.

A review has three possible statuses:

- __Comment__: Submit general feedback without explicitly approving the changes or requesting additional changes.
- __Approve__: Submit feedback and approve merging the changes proposed in the pull request.
- __Request changes__: Submit feedback that must be addressed before the pull request can be merged.

Once the request is approved, it can be merged to main branch and the source branch can then be deleted.

**Note**: Please delete the source branch once it's merged to avoid cluttering the repository with unwanted branches.

##### Branches and the environments that they deploy to ####

**main**: Main deploy to Production environment. The workflows which reside in main branch are needed to be triggered manually and have some custom variables which are to be provided when trggering the workflow.

_screenshots needed_















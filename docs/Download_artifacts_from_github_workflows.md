## How to Download an artifact on Github

GitHub workflows can create artifacts after the workflow run is sucussefully completed

**Note**: An artifact will be available only after the entire workflow run is completed 

Follow the steps below to download an artifact:

* Go to the github repository, where the particualr workflow exists, in a web browser
  
* Click on Actions
  ![alt text][click_actions]
* Click on the workflow run from which the artifact is needed to be downloaded
  ![alt text][click_workflow_run]
* Click on the number shown below **Artifacts**
  ![alt text][click_artifacts]
* This shall take you to artfacts. Click the name of the artifact to download it
  ![alt text][click_artifacts_name]

[click_actions]: ./images/artifact_doc_1.png
[click_workflow_run]: ./images/artifact_doc_2.png
[click_artifacts]: ./images/artifact_doc_3.png
[click_artifacts_name]: ./images/artifact_doc_4.png


**Note**: The retention period of artifacts, set up by the Automation team, is one day currently.
Which means the artifact will only be available for download for a day since when the workflow was 
triggered. 


# Note Extraction
This is a project for the course of Automatic Speech Recognition. In this we predict the note of a piano key using machine learning techniques
### Data Generation
Data generation is done using scribbletune in nodeJS. In the shell make a new directory named 'data'
```shell
mkdir data # create a directory if it does not exist
node data_generation.js # to get the data with varing notes and accents in a midi format
```
The midi format files are converted to wav format using timidity.
```shell
cd data/
timidity *.mid -Ow # convert mid to wav format
rm *.mid # remove the original mid files if not needed
```
### Feature Extraction
Python
### Machine Learning
Python

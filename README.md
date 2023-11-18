# Sambo-Terminator

[Watch the Demo Video](https://www.youtube.com/watch?v=HWIMwm5B9ic)

## Abstract
In this project, we measure brainwaves using BIOPAC to collect data on left turns, right turns, and going straight. We then classify these three types of signals using a machine learning model. The presentation method involves simulating this process in the game Minecraft, where we record brainwaves, analyze the direction, and display the turn signals using a Python-based desktop application.


## Motivation
The rate of traffic accidents in Taiwan is significantly higher than in other countries, with a substantial portion involving motorcycles. Common causes of these accidents include not paying attention to the road conditions, failing to check mirrors before turning, and not signaling turns. Our goal is to reduce the rate of accidents caused by incorrect turning.

The initial idea was to control rearview mirror movement with brain and eye electrical signals (EEG and EOG) to address the issue of blind spots and eliminate the need to manually adjust the mirrors, which can be both inconvenient and dangerous. However, since eye electrical signals are a form of electromyography and hard to distinguish from brain electrical signals, we decided to focus on the issue of not signaling turns.

Many accidents occur because riders fail to signal before turning. We hope to detect changes in brain electrical signals before reaching an intersection and determine the intended direction of the turn or if the rider plans to go straight.

The original plan for this project was to design a rearview mirror that could rotate based on the position of the eyes (EOG) to choose the left or right mirror and use brainwave signals (EEG) to control the extent of the mirror's rotation. We then intended to employ Machine Learning for brainwave control (turning the rearview mirrors left or right). Initially, we expected to be able to control the mirrors as desired, expanding the field of view. If successful in a helmet, this application could potentially be miniaturized in the future for wearable devices suitable for car drivers.

## Methodology
Due to the high cost of wearable EEG devices, our experiments were confined to using the Biopac system, preventing outdoor cycling tests and real-time analysis. Our approach involved using Minecraft to create routes with numerous intersections. Test subjects played the game, thinking about turning left, right, or going straight before each intersection. We trained a machine learning model with the brainwave signals from this thought process. After training, we had subjects run random routes in the game, recording their gameplay. We fed this data into our trained model for prediction and then input these predictions into a turn signal module for analysis and comparison.

### Electrode Placement:

As shown in the left figure (T3, T4, A1), the accuracy is approximately 88% (validation).
As per the right figure (Experiment 1), the accuracy is around 92% (validation).

### Route Design:

Three files for Route One, representing left, center, right. Each includes thinking about turning or going straight 5 seconds before the intersection, followed by a 5-second rest. Each type of file requires different calibration values, affecting the validation set accuracy.
Route One, same file, turning or going straight 5 seconds before intersections, then a 5-second rest. This method avoids using different calibration values each time.
Route Two, same file, continuous turning or going straight for five seconds, in the order of center-left-center-right.
Results
a. Experimental Data: We only use the first five seconds of each turn/straight period for data, with the following five seconds being rest time and not used for training.
b. Demo: Using measurement method two, we asked participants to run Route One and recorded it. The actual video includes four instances each of left turns, straight movements, and right turns. The first twenty seconds are rest, followed by a 5-second action and 5-second rest pattern. The following page shows some of the comparison screens for these turns.

## Discussion
a. Factors Affecting Brainwaves:

Variations in signals from the same person on different days.
Position and type of electrode patches.
Continuous turning requires constant mouse movement, which might affect brainwaves. Therefore, the third measurement method had more noise and lower accuracy and was discarded.
b. Calibration across different files: We addressed this by using a calibration route. Before testing, we ran a fixed route to fine-tune our model using this short segment's data and correct answers. Although we used normalized data, further design improvements might be needed to solve the calibration issue, making it more practical for prediction.
Conclusion
Although the prediction accuracy is not very high, we observed significant changes in the predictions before intersections, proving that signals for thinking about turning left, right, or going straight are distinguishable. We hope to apply these concepts to wearable EEG devices in the future and conduct real-world tests, or even integrate these systems into helmets for enhanced practicality and convenience. With advancing computer technology and artificial intelligence, such applications could significantly improve road safety.

## Review
This course provided fundamental knowledge about physiological signal characteristics and measurement, enhancing our understanding of the biomedical field. The pilot experiments were particularly helpful; we learned about Biopac operation and signal characteristics in Experiment 1, and spent considerable time in Experiment 2 adjusting circuits and optimizing the mobile app. We are very satisfied with the outcome and feel a sense of achievement.

We found the Final Project topic interesting and unique. However, measuring brainwaves is not simple, and we spent a lot of time on repeated measurements and training. The physiological state of the participants on a given day was a major variable, with the same model and measurement method yielding vastly different results on different days. We hope to further explore this topic in the future.

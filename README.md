# class-Find_Out
Method class for finding out useful information in Maya (eg, face centers, distance between two points, etc.) for use in other scripts.
This will evolve over time as I add more to the library.

Currently enabled functions:

edge_length - parameters : (list of two vertices to be measured) - list
---finds the distance between to vertices (can be used to calculate distance between control points on curves too)

curve_length - parameters : (name of curve) - str
---finds the total length of a curve (uses Maya's arclen command)

face_center - parameters : not required
---returns dictionary of coordinates of face centers from selected faces. no parameters required, but needs a selection before hand.

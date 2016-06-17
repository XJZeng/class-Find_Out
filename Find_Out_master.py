import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMaya as OpenMaya
import math
import re
from string import Template, zfill
from functools import partial

class Find_Out():
    '''
    multipurpose class for finding length of anything. Well, work in progress
    '''
    
    def edge_length(self, vertex_list):
        #find distance between two points. numpy required. need to rework this so numpy not required
        vtx_p=cmds.xform(vertex_list,q=True,t=True,ws=True)
        '''
        this is numpy version. reuse for machines with numpy for quicker calculations:
            
        vtx_p_array_a = np.array([[vtx_p[0]], [vtx_p[1]], [vtx_p[2]]])
        vtx_p_array_b = np.array([[vtx_p[3]], [vtx_p[4]], [vtx_p[5]]])
        dist = np.linalg.norm(vtx_p_array_a-vtx_p_array_b)
        
        '''
        dist = math.sqrt((vtx_p[3] - vtx_p[0])**2 + (vtx_p[4] - vtx_p[1])**2 + (vtx_p[5] - vtx_p[2])**2)
        return dist
        
    def curve_length(self, curve_sel):
        #find length of curve
        find_curve_length = cmds.arclen(curve_sel)
        return find_curve_length
        
    def face_center():
        # This finds the face center of each face and uploads data to the global dictionary
        Face_Center_Dict = {}
        face_center = []

        selection = OpenMaya.MSelectionList()
        OpenMaya.MGlobal.getActiveSelectionList(selection)

        iter_sel = OpenMaya.MItSelectionList (selection, OpenMaya.MFn.kMeshPolygonComponent)

        while not iter_sel.isDone():
            dag_path = OpenMaya.MDagPath()
            component = OpenMaya.MObject()

            iter_sel.getDagPath(dag_path, component)

            poly_iter = OpenMaya.MItMeshPolygon(dag_path, component)

            while not poly_iter.isDone():
                # enumerates the faces in selection
                i = 0
                i = poly_iter.index()
                face_info = ("face %s" %i)
                    
                # finds the face center of enumerated face                
                center = OpenMaya.MPoint
                center = poly_iter.center(OpenMaya.MSpace.kWorld)
                point = [0.0,0.0,0.0]
                point[0] = center.x
                point[1] = center.y
                point[2] = center.z
                face_center = point
                    
                # uploads face to global dictionary
                Face_Center_Dict.update({face_info:face_center})
                    
                #goes to next face
                poly_iter.next()
                    
            iter_sel.next()
            
            return Face_Center_Dict

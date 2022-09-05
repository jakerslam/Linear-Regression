#!/usr/bin/env python3  Line 1
# -*- coding: utf-8 -*- Line 2
#----------------------------------------------------------------------------
# Created By  : Jacob Haslam  Line 3
# Created Date: 01/09/20 ..etc
# version ='1.0'
# ---------------------------------------------------------------------------
""" A program to calulate the most efficient trend from a set of data points"""  #Line 4
# ---------------------------------------------------------------------------
# Imports Line 5
# ---------------------------------------------------------------------------
#from ... import ...  #Line 6

def get_y(m, b, x):
  y = m*x + b
  return y


def calculate_error(m,b,point):
    valueX = point[0]
    valueY = point[1]
    differenceY = abs(get_y(m,b,valueX) - valueY)
    return differenceY


def calculate_all_error(m,b,points):
    error = 0
    for point in points:
        error += calculate_error(m,b,point)
    return error

# gets aprox slope to reduce complexity of looping unnessearrily
# set some margine room to find the more acurate slope
def GetPossible_ms(accuracy, dataPoints):
    AproxM = int( (dataPoints[0][0] + dataPoints[-1][0]) / (dataPoints[0][1] + dataPoints[-1][1]) ) 
    print(AproxM)
    margin = 10
    possible_ms = []
    for i in range(AproxM - margin, AproxM + margin):
        possible_ms.append(i*accuracy)
    return possible_ms

def GetPossible_bs(accuracy, datapoints):
    yRange = 0
    for i in range(len(datapoints)):
        if abs(datapoints[i][1]) > yRange:
            yRange = abs(datapoints[i][1])
    possible_bs = []
    for i in range(-yRange,yRange+1):
        possible_bs.append(i*accuracy)
    return possible_bs

def main():
    datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)] ##sample data
    smallest_error = float('inf')
    best_m = 0
    best_b = 0
    accuracy = 0.1
    for m in GetPossible_ms(accuracy, datapoints):
        for b in GetPossible_bs(accuracy, datapoints):
            error = calculate_all_error(m,b,datapoints)
            if error < smallest_error:
                smallest_error = error
                best_m = m
                best_b = b

    print("y = ", round(best_m,2),"x +",round(best_b,2))
    print("Error: ",round(smallest_error,2))

if __name__ == "__main__":
    main()